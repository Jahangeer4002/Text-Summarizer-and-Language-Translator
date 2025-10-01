import tkinter as tk
from tkinter import ttk, messagebox
from summarizer import extractive_summary
from translator import detect_language, translate_text

class TextProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Summarizer & Translator")
        self.root.geometry("1000x700")
        self.root.configure(bg="#e6f3ff")
        self.languages = {
            'English': 'en', 'Hindi': 'hi', 'Telugu': 'te', 'Tamil': 'ta',
            'Kannada': 'kn', 'Malayalam': 'ml', 'Urdu': 'ur', 'Bengali': 'bn',
            'Chinese (Simplified)': 'zh-cn', 'Japanese': 'ja', 'Russian': 'ru',
            'French': 'fr'
        }
        self.create_gui()

    def create_gui(self):
        title = tk.Label(self.root, text="Text Summarizer & Translator",
                         font=("Arial", 20, "bold"), bg="#4a90e2", fg="white", pady=10)
        title.pack(fill="x")

        main_frame = tk.Frame(self.root, bg="#e6f3ff")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        left_frame = tk.Frame(main_frame, bg="#e6f3ff")
        left_frame.grid(row=0, column=0, sticky="ns", padx=10)

        self.summarize_btn = tk.Button(left_frame, text="Summarize", command=self.summarize_text,
                                       bg="#2ecc71", fg="#ffffff", font=("Arial", 11, "bold"),
                                       activebackground="#27ae60", activeforeground="#ffffff",
                                       relief="raised", bd=3, padx=12, pady=6, width=15)
        self.summarize_btn.pack(pady=5)

        self.translate_btn = tk.Button(left_frame, text="Translate", command=self.translate_text,
                                       bg="#3498db", fg="#ffffff", font=("Arial", 11, "bold"),
                                       activebackground="#2980b9", activeforeground="#ffffff",
                                       relief="raised", bd=3, padx=12, pady=6, width=15)
        self.translate_btn.pack(pady=5)

        self.clear_btn = tk.Button(left_frame, text="Clear", command=self.clear_text,
                                   bg="#e74c3c", fg="#ffffff", font=("Arial", 11, "bold"),
                                   activebackground="#c0392b", activeforeground="#ffffff",
                                   relief="raised", bd=3, padx=12, pady=6, width=15)
        self.clear_btn.pack(pady=5)

        lang_frame = tk.Frame(left_frame, bg="#e6f3ff")
        lang_frame.pack(pady=5)
        tk.Label(lang_frame, text="Translate to:", font=("Arial", 12, "bold"),
                 bg="#e6f3ff", fg="#333333").pack(anchor="w")
        self.translate_lang_var = tk.StringVar()
        style = ttk.Style()
        style.configure("TCombobox", fieldbackground="#ffffff", background="#4a90e2",
                        foreground="#333333", arrowcolor="white")
        translate_lang_menu = ttk.Combobox(lang_frame, textvariable=self.translate_lang_var,
                                           values=list(self.languages.keys()), state="readonly",
                                           style="TCombobox", width=15)
        translate_lang_menu.pack()
        translate_lang_menu.set("English")

        summary_lang_frame = tk.Frame(left_frame, bg="#e6f3ff")
        summary_lang_frame.pack(pady=5)
        tk.Label(summary_lang_frame, text="Summarize in:", font=("Arial", 12, "bold"),
                 bg="#e6f3ff", fg="#333333").pack(anchor="w")
        self.summary_lang_var = tk.StringVar()
        summary_lang_menu = ttk.Combobox(summary_lang_frame, textvariable=self.summary_lang_var,
                                         values=list(self.languages.keys()), state="readonly",
                                         style="TCombobox", width=15)
        summary_lang_menu.pack()
        summary_lang_menu.set("English")

        right_frame = tk.Frame(main_frame, bg="#e6f3ff")
        right_frame.grid(row=0, column=1, sticky="nsew")
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_columnconfigure(1, weight=1)
        right_frame.grid_rowconfigure(0, weight=1)

        input_frame = tk.Frame(right_frame, bg="#e6f3ff")
        input_frame.grid(row=0, column=0, sticky="nsew", padx=5)
        tk.Label(input_frame, text="Enter Your Text:", font=("Arial", 12, "bold"),
                 bg="#e6f3ff", fg="#333333").pack(anchor="w", pady=5)
        self.input_text = tk.Text(input_frame, height=20, width=40,
                                  font=("Arial", 11), wrap="word", bg="#ffffff", fg="#333333",
                                  borderwidth=2, relief="flat")
        self.input_text.pack(fill="both", expand=True)

        output_frame = tk.Frame(right_frame, bg="#e6f3ff")
        output_frame.grid(row=0, column=1, sticky="nsew", padx=5)
        tk.Label(output_frame, text="Result:", font=("Arial", 12, "bold"),
                 bg="#e6f3ff", fg="#333333").pack(anchor="w", pady=5)
        self.output_text = tk.Text(output_frame, height=20, width=40,
                                   font=("Arial", 11), wrap="word", bg="#ffffff", fg="#333333",
                                   borderwidth=2, relief="flat")
        self.output_text.pack(fill="both", expand=True)

        self.status = tk.Label(self.root, text="Ready", bd=1, relief="sunken",
                               anchor="w", bg="#4a90e2", fg="white", font=("Arial", 10))
        self.status.pack(side="bottom", fill="x")

        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

    def summarize_text(self):
        try:
            self.status.config(text="Processing...")
            self.root.update()
            input_text = self.input_text.get("1.0", "end-1c")
            if not input_text:
                messagebox.showwarning("Warning", "Please enter some text first!")
                return

            detected_lang = detect_language(input_text)
            target_lang = self.languages[self.summary_lang_var.get()]

            if detected_lang != 'en':
                self.status.config(text="Translating to English for summarization...")
                self.root.update()
                english_text = translate_text(input_text, 'en')
            else:
                english_text = input_text

            input_word_count = len(english_text.split())
            target_word_count = max(5, int(input_word_count * 0.25))

            self.status.config(text="Summarizing in English...")
            self.root.update()
            english_summary = extractive_summary(english_text, target_word_count)

            if target_lang != 'en':
                self.status.config(text=f"Translating summary to {self.summary_lang_var.get()}...")
                self.root.update()
                final_summary = translate_text(english_summary, target_lang)
            else:
                final_summary = english_summary

            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", final_summary)
            self.status.config(text=f"Summary generated in {self.summary_lang_var.get()} ({len(final_summary.split())} words)")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status.config(text="Error occurred")

    def translate_text(self):
        try:
            self.status.config(text="Translating...")
            self.root.update()
            input_text = self.input_text.get("1.0", "end-1c")
            if not input_text:
                messagebox.showwarning("Warning", "Please enter some text first!")
                return
            target_lang = self.languages[self.translate_lang_var.get()]
            translated = translate_text(input_text, target_lang)
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", translated)
            self.status.config(text="Translation completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status.config(text="Error occurred")

    def clear_text(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.status.config(text="Text cleared")