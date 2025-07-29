#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
from PyPDF2 import PdfReader
import re
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    return " ".join([page.extract_text() for page in pdf_reader.pages])

def preprocess_text(text):
    """Clean and prepare text for summarization"""
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    text = re.sub(r'\[.*?\]', '', text)  # Remove citations
    return text

def generate_quality_summary(text, num_sentences=5):
    """Improved summarization using key sentence extraction"""
    # Load modern summarization model
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Chunking for long documents (BART has 1024 token limit)
    max_chunk = 1000
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    
    # Generate summary for each chunk
    summary = []
    for chunk in chunks:
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary.append(result[0]['summary_text'])
    
    return " ".join(summary)

def main():
    st.title("📄 Smart PDF Summarizer")
    st.markdown("Upload a PDF for **coherent, well-structured** summaries")
    
    uploaded_file = st.file_uploader("Choose PDF", type="pdf")
    
    if uploaded_file:
        with st.spinner("Analyzing document..."):
            raw_text = extract_text_from_pdf(uploaded_file)
            clean_text = preprocess_text(raw_text)
            
            if len(clean_text.split()) < 50:
                st.warning("Document too short for meaningful summary")
                return
                
            summary = generate_quality_summary(clean_text)
        
        st.subheader("Key Points")
        st.write(summary)
        
        # Improved download option
        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="document_summary.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
