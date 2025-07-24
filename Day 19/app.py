#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data(uploaded_file):
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("! Unsupported file format.")
            return None
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def calculate_revenue(df):
    df["Revenue"] = df["Units Sold"] * df["Unit Price"]
    return df

def generate_report(df):
    report_lines = ["---< Sales Summary >---"]
    product_revenue = df.groupby("Product")["Revenue"].sum()

    for product, revenue in product_revenue.items():
        report_lines.append(f"Product: {product} – Revenue: {int(revenue)}")

    total_revenue = int(product_revenue.sum())
    top_product = product_revenue.idxmax()

    report_lines.append(f"\n-- Total Revenue: {total_revenue}")
    report_lines.append(f"-- Top Product: {top_product}")

    return "\n".join(report_lines), product_revenue

#App UI
st.set_page_config(page_title="Sales Report Generator", layout="centered")
st.title("Sales Report Generator")

uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    
    if df is not None:
        st.subheader("Data Preview")
        st.dataframe(df)

        df = calculate_revenue(df)

        report_text, product_revenue = generate_report(df)

        st.subheader("Generated Report")
        st.text(report_text)

        st.subheader("Product Revenue Chart")
        fig, ax = plt.subplots()
        product_revenue.plot(kind="bar", color="skyblue", ax=ax)
        ax.set_title("Product Revenue")
        ax.set_xlabel("Product")
        ax.set_ylabel("Revenue")
        st.pyplot(fig)

        st.download_button("Download Report", data=report_text, file_name="report.txt", mime="text/plain")


# In[ ]:




