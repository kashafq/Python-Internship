#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import PyPDF2
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import traceback

# Page title and intro
st.set_page_config(page_title="PDF to Notes – Auto Summarizer")
st.title("PDF to Notes – Auto Summarizer")
st.markdown("Upload a PDF file and get a summarized version of its content in seconds.")

# Upload section
pdf = st.file_uploader("Upload your PDF file", type='pdf')

# If a file is uploaded
if pdf:
    try:
        # Extract text from the uploaded PDF
        reader = PyPDF2.PdfReader(pdf)
        extracted_text = ""

        for page in reader.pages:
            extracted_text += page.extract_text() or ""

        # Check if there's any text
        if not extracted_text.strip():
            st.warning("No readable text found in the PDF. Please upload a text-based PDF.")
        else:
            st.success("Text extracted successfully!")
            with st.expander("View Extracted Text"):
                st.text_area("Extracted Text", extracted_text[:3000] + "...", height=300)

            # Let user choose how much summary they want
            num_sentences = st.slider("Number of Sentences in Summary", min_value=1, max_value=10, value=3)

            # Summarize on button click
            if st.button("Summarize"):
                try:
                    parser = PlaintextParser.from_string(extracted_text, Tokenizer("english"))
                    summarizer = LsaSummarizer()
                    summary = summarizer(parser.document, num_sentences)

                    st.subheader("Summary:")
                    for i, sentence in enumerate(summary, 1):
                        st.write(f"{i}. {sentence}")

                except Exception:
                    st.error("An error occurred during summarization.")
                    st.code(traceback.format_exc())

    except Exception:
        st.error("Something went wrong while processing the file.")
        st.code(traceback.format_exc())







