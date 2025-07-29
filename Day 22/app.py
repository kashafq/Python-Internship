#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import PyPDF2
from transformers import pipeline

# Summarizer pipeline
summarizer = pipeline("summarization")

# Extract text from uploaded PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Streamlit App UI
st.set_page_config(page_title="PDF to Notes – Auto Summarizer", layout="centered")
st.title("PDF to Notes – Auto Summarizer")
st.markdown("Upload your lecture or assignment PDF and get summarized notes in seconds!")

pdf_file = st.file_uploader("Upload your PDF file", type=["pdf"])

if pdf_file:
    with st.spinner("Extracting text..."):
        pdf_text = extract_text_from_pdf(pdf_file)
    
    if len(pdf_text.strip()) == 0:
        st.error("Could not extract text. Try a different file.")
    else:
        st.success("Text extracted successfully!")
        st.markdown("#### Original Text Preview")
        st.text_area("Raw Text", pdf_text[:2000] + "..." if len(pdf_text) > 2000 else pdf_text, height=200)

        if st.button("Summarize"):
            with st.spinner("Summarizing..."):
                # Truncate to max model length
                input_text = pdf_text[:3000]  # 3000 chars = ~800 tokens
                summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
                st.markdown("### Summary:")
                st.success(summary)






