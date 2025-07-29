#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from PyPDF2 import PdfReader
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

nltk.download('punkt')

#App Setup
st.set_page_config(page_title="PDF to Notes", layout="centered")
st.title("PDF to Notes – Auto-Summarize Your Lecture PDFs")
st.markdown("Upload your class notes or assignments in PDF form and get clean, bullet-style summaries!")

#Upload PDF
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

#Extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    return full_text

#Summarize Text
def summarize_text(text, num_sentences=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return [str(sentence) for sentence in summary]

#Main Logic
if uploaded_file:
    st.success("PDF uploaded successfully!")
    with st.spinner("Extracting and summarizing..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
        if len(pdf_text.strip()) == 0:
            st.error("Could not extract text. Try a different file.")
        else:
            summary = summarize_text(pdf_text, num_sentences=7)
            st.markdown("###Summary:")
            for sentence in summary:
                st.write(f"• {sentence}")

            # Optional Download
            if st.button("Download Summary as .txt"):
                summary_text = "\n".join(summary)
                st.download_button("Download Notes", summary_text, file_name="summary_notes.txt")
else:
    st.info("Upload a PDF file to begin1")





