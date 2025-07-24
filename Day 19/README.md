# Sales Report Generator

A simple web-based tool built with Streamlit that allows users to upload a CSV or Excel file and generate a visual and text summary of sales data.

## Features

- Upload `.csv` or `.xlsx` sales data file
- Calculates total revenue and revenue by product
- Identifies the top-performing product
- Generates a downloadable summary report
- Displays a bar chart of product-wise revenue

## How to Use

1. Go to the live app link (if deployed)
2. Upload your CSV or Excel file using the uploader
3. View the auto-generated report and bar chart
4. Optionally, download the text summary

## Sample Dataset Format

Date,Product,Units Sold,Unit Price
2025-07-01,Keyboard,5,1200
2025-07-01,Mouse,10,700
2025-07-02,Laptop,2,85000
2025-07-03,Monitor,3,15000
2025-07-03,Mouse,4,700

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib

## File Structure

Day 19/
├── app.py # Streamlit application
├── README.md # Project instructions
├── sample_data.csv 

## Deployment

This app can be deployed using [Streamlit Cloud](https://streamlit.io/cloud).  
To run locally:
1. Install required packages:
    pip install streamlit pandas matplotlib openpyxl

2. Run the app:
   streamlit run app.py

---
