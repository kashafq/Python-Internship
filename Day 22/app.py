#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import PyPDF2
from transformers import pipeline

# Initialize summarizer
summarizer = pipeline("summarization")

# Extract text from PDF
def extract_text(pdf):
    reader = PyPDF2.PdfReader(pdf)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# UI Settings
st.set_page_config(page_title="PDF to Notes – Auto-Summarizer", layout="centered")
st.title("PDF to Notes – Auto-Summarizer")
st.markdown("Convert your lecture PDFs into quick notes using AI. Just upload, click, and get your summary.")

pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file:
    with st.spinner("Extracting text..."):
        text = extract_text(pdf_file)

    if not text.strip():
        st.error("Couldn't extract any text. Please try another PDF.")
    else:
        st.success("Text extracted successfully!")
        st.markdown("### Preview of PDF Content")
        st.text_area("Extracted Text", text[:2000] + ("..." if len(text) > 2000 else ""), height=200)

        if st.button("Summarize Now"):
            with st.spinner("Generating AI Summary..."):
                try:
                    trimmed_text = text[:3000]  # Transformers work best under ~800 tokens
                    summary = summarizer(trimmed_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
                    st.success("Summary Ready!")
                    st.markdown("### Summary")
                    st.write(summary)

                    # Downloadable summary
                    st.download_button("Download Summary", summary, file_name="summary.txt")

                except Exception as e:
                    st.error(f"Error during summarization: {str(e)}")






