#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from PyPDF2 import PdfReader
from fuzzywuzzy import fuzz

#App Title
st.set_page_config(page_title="ChatPDF Lite", layout="centered")
st.title("ChatPDF Lite – Ask Questions from Your PDF Notes!")
st.markdown("Upload your PDF, ask any question, and get smart answers based on the content inside.")

#Upload PDF
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

#Extract Text from PDF
def extract_pdf_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

#Find Best Matching Answer
def find_best_answer(text, question):
    paragraphs = [p.strip() for p in text.split("\n") if len(p.strip()) > 30]
    best_score = 0
    best_match = "Sorry, no relevant answer found!"
    for para in paragraphs:
        score = fuzz.partial_ratio(question.lower(), para.lower())
        if score > best_score:
            best_score = score
            best_match = para
    return best_match

#Main App Logic
if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_pdf_text(uploaded_file)
        st.success("Text extracted successfully!")
        st.markdown("Now ask your question")

        question = st.text_input("Your Question:")

        if question:
            with st.spinner("Searching for the best answer..."):
                answer = find_best_answer(pdf_text, question)
                st.markdown("### Best Answer Found:")
                st.info(answer)
else:
    st.warning("Please upload a PDF file to begin 💡")


# In[ ]:




