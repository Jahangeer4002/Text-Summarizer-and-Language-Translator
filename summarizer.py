import nltk
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


nltk.download('punkt')
nltk.download('punkt_tab')

def extractive_summary(text, target_word_count):
    sentences = nltk.sent_tokenize(text)
    if len(sentences) <= 1:
        return text

    cleaned_sentences = [re.sub(r'\W+', ' ', s).strip() for s in sentences]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(cleaned_sentences)
    sentence_scores = np.array(tfidf_matrix.sum(axis=1)).flatten().tolist()

    paragraphs = text.split('\n\n')
    thematic_sections = []
    for para in paragraphs:
        para_sentences = nltk.sent_tokenize(para.strip())
        if para_sentences:
            thematic_sections.append(para_sentences)

    total_words = len(text.split())
    avg_words_per_sentence = total_words / len(sentences) if len(sentences) > 0 else 1
    num_sentences = max(len(thematic_sections), int(target_word_count / avg_words_per_sentence))

    sentences_per_theme = max(1, num_sentences // len(thematic_sections))
    remaining = num_sentences % len(thematic_sections)

    summary_sentences = []
    sentence_offset = 0
    for section in thematic_sections:
        section_size = len(section)
        section_scores = sentence_scores[sentence_offset:sentence_offset + section_size]
        scored_sentences = [(score, idx + sentence_offset, sent) for idx, (score, sent) in enumerate(zip(section_scores, section))]
        scored_sentences.sort(reverse=True)
        num_to_take = sentences_per_theme + (1 if remaining > 0 else 0)
        for i in range(min(num_to_take, len(scored_sentences))):
            summary_sentences.append((scored_sentences[i][1], scored_sentences[i][2]))
        remaining = max(0, remaining - 1)
        sentence_offset += section_size

    summary_sentences.sort(key=lambda x: x[0])
    summary = " ".join(sent for _, sent in summary_sentences)
    return summary