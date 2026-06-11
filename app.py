import streamlit as st
from summarizer import extractive_summary
from translator import detect_language, translate_text

st.set_page_config(
    page_title="AI Text Summarizer & Translator",
    page_icon="🤖",
    layout="wide"
)

languages = {
    'English': 'en',
    'Hindi': 'hi',
    'Telugu': 'te',
    'Tamil': 'ta',
    'Kannada': 'kn',
    'Malayalam': 'ml',
    'Urdu': 'ur',
    'Bengali': 'bn',
    'Chinese (Simplified)': 'zh-cn',
    'Japanese': 'ja',
    'Russian': 'ru',
    'French': 'fr'
}

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #eaf4ff;
}

.title-box {
    background:#4a90e2;
    padding:15px;
    border-radius:10px;
    text-align:center;
    color:white;
    font-size:32px;
    font-weight:bold;
    margin-bottom:20px;
}

.stButton>button {
    width:100%;
    border-radius:8px;
    height:45px;
    font-weight:bold;
    font-size:16px;
}

textarea {
    border-radius:10px !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title-box">🤖 AI Powered Text Summarizer & Language Translator</div>',
    unsafe_allow_html=True
)

# Session state
if "output" not in st.session_state:
    st.session_state.output = ""

# Layout
left_panel, right_panel = st.columns([1, 4])

with left_panel:

    st.subheader("Options")

    summary_lang = st.selectbox(
        "Summarize In",
        list(languages.keys())
    )

    translate_lang = st.selectbox(
        "Translate To",
        list(languages.keys())
    )

    summarize_btn = st.button("📝 Summarize")

    translate_btn = st.button("🌍 Translate")

    clear_btn = st.button("🗑 Clear")

with right_panel:

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input Text")

        input_text = st.text_area(
            "Input Text",
            height=450,
            key="input_area",
            label_visibility="collapsed"
        )

    with col2:
        st.subheader("Result")

        st.text_area(
            "Output Text",
            value=st.session_state.output,
            height=450,
            disabled=True,
            label_visibility="collapsed"
        )

# Summarize
if summarize_btn:

    if input_text.strip():

        with st.spinner("Generating Summary..."):

            detected_lang = detect_language(input_text)
            target_lang = languages[summary_lang]

            if detected_lang != "en":
                english_text = translate_text(
                    input_text,
                    "en"
                )
            else:
                english_text = input_text

            words = len(english_text.split())

            summary = extractive_summary(
                english_text,
                max(5, int(words * 0.25))
            )

            if target_lang != "en":
                summary = translate_text(
                    summary,
                    target_lang
                )

            st.session_state.output = summary

        st.rerun()

# Translate
if translate_btn:

    if input_text.strip():

        with st.spinner("Translating..."):

            result = translate_text(
                input_text,
                languages[translate_lang]
            )

            st.session_state.output = result

        st.rerun()

# Clear
if clear_btn:
    st.session_state.output = ""
    st.rerun()

st.markdown("---")
st.success("Ready")