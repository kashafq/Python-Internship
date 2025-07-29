#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
from PyPDF2 import PdfReader
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import re
import nltk

# Download required NLTK data
nltk.download('punkt')

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def clean_text(text):
    # Remove excessive whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def generate_summary(text, sentences_count=5):
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentences_count)
        return ' '.join([str(sentence) for sentence in summary])
    except Exception as e:
        st.error(f"Error generating summary: {str(e)}")
        return "Could not generate summary. The text might be too short."

def main():
    st.title("PDF Text Extractor & Summarizer")
    st.write("Upload a PDF file to extract text and get a summary")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        
        # Extract text
        with st.spinner("Extracting text..."):
            raw_text = extract_text_from_pdf(uploaded_file)
            cleaned_text = clean_text(raw_text)
        
        # Display raw text
        st.subheader("Extracted Text")
        with st.expander("View raw extracted text"):
            st.text(cleaned_text)
        
        # Generate and display summary
        if len(cleaned_text.split()) > 50:  # Only summarize if enough text
            st.subheader("Summary")
            with st.spinner("Generating summary..."):
                summary = generate_summary(cleaned_text)
            st.write(summary)
            
            # Download button for summary
            st.download_button(
                label="Download Summary as TXT",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )
        else:
            st.warning("The document doesn't contain enough text to generate a meaningful summary.")

if __name__ == "__main__":
    main()

