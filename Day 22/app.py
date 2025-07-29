#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
from PyPDF2 import PdfReader
import re
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
    """Clean text for summarization"""
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    text = re.sub(r'\[.*?\]', '', text)  # Remove citations
    return text

def generate_summary(text, num_sentences=5):
    """Improved summarization using NLTK"""
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english') + ['.', ',', '!', '?'])
    words = [word for word in words if word not in stop_words]
    
    # Frequency analysis
    freq_dist = nltk.FreqDist(words)
    
    # Score sentences
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                if i not in sentence_scores:
                    sentence_scores[i] = freq_dist[word]
                else:
                    sentence_scores[i] += freq_dist[word]
    
    # Get top sentences
    if not sentence_scores:
        return "Could not generate meaningful summary."
    
    top_sentences = sorted(sentence_scores.items(), 
                          key=lambda x: x[1], reverse=True)[:num_sentences]
    top_sentences = sorted(top_sentences, key=lambda x: x[0])
    
    return ' '.join([sentences[i] for i, score in top_sentences])

def main():
    st.title("PDF Summarizer")
    st.markdown("Upload a PDF for **concise summaries** (Streamlit Cloud compatible)")
    
    uploaded_file = st.file_uploader("Choose PDF", type="pdf")
    
    if uploaded_file:
        with st.spinner("Processing document..."):
            raw_text = extract_text_from_pdf(uploaded_file)
            clean_text = preprocess_text(raw_text)
            
            if len(clean_text.split()) < 50:
                st.warning("Document too short for meaningful summary")
                return
                
            summary = generate_summary(clean_text)
        
        st.subheader("Summary")
        st.write(summary)
        
        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
