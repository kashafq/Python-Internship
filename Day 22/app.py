#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
from PyPDF2 import PdfReader
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Check and download NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    with st.spinner("Downloading language resources..."):
        nltk.download('punkt')
        nltk.download('stopwords')

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    return " ".join([page.extract_text() for page in pdf_reader.pages])

def clean_and_preprocess(text):  # Renamed this function
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'\[.*?\]', '', text)
    return text

def generate_summary(text, num_sentences=5):  # Fixed typo in function name
    sentences = sent_tokenize(text)
    if len(sentences) < 2:
        return text[:500] + "..." if len(text) > 500 else text
    
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english') + ['.', ',', '!', '?'])
    words = [word for word in words if word not in stop_words]
    
    freq_dist = nltk.FreqDist(words)
    sentence_scores = {}
    
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                sentence_scores[i] = sentence_scores.get(i, 0) + freq_dist[word]
    
    if not sentence_scores:
        return sentences[0]
    
    top_sentences = sorted(sentence_scores.items(), 
                         key=lambda x: x[1], reverse=True)[:num_sentences]
    top_sentences = sorted(top_sentences, key=lambda x: x[0])
    
    return ' '.join([sentences[i] for i, _ in top_sentences])

def main():
    st.title("PDF Summarizer Pro")
    st.markdown("Extracts key information from PDF documents")
    
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    
    if uploaded_file:
        with st.spinner("Processing document..."):
            raw_text = extract_text_from_pdf(uploaded_file)
            processed_text = clean_and_preprocess(raw_text)  # Using new function name
            
            if len(processed_text.split()) < 30:
                st.warning("Document is too short for summarization")
                st.text_area("Extracted Text", processed_text, height=200)
            else:
                summary = generate_summary(processed_text)
                st.subheader("Summary")
                st.write(summary)
                
                st.download_button(
                    "Download Summary",
                    summary,
                    file_name="summary.txt"
                )

if __name__ == "__main__":
    main()
