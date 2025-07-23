#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(file):
    try:
        if file.endswith(".csv"):
            df=pd.read_csv(file)
        elif file.endswith(".xlsx"):
            df=pd.read_excel(file)
        else:
            print("Unsupported file format.")
            return None
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None

def calculate_revenue(df):
    df["Revenue"]= df["Units Sold"]*df["Unit Price"]
    return df

def generate_report(df):
    report_lines =["--< Sales Summary >---"]
    product_revenue=df.groupby("Product")["Revenue"].sum()
    
    for product, revenue in product_revenue.items():
        report_lines.append(f"Product: {product} – Revenue: {int(revenue)}")

    total_revenue=int(product_revenue.sum())
    top_product=product_revenue.idxmax()

    report_lines.append(f"\n-- Total Revenue: {total_revenue}")
    report_lines.append(f"-- Top Product: {top_product}")
    
    return "\n".join(report_lines), product_revenue

def save_report(report_text, filename="report.txt"):
    with open(filename, "w") as f:
        f.write(report_text)
    print(f"+ Report saved to {filename}")

def create_bar_chart(product_revenue, filename="bar_chart.png"):
    product_revenue.plot(kind="bar", color="skyblue")
    plt.title("Product Revenue")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Chart saved to {filename}")

if __name__=="__main__":
    file=input("Enter the filename (CSV or Excel): ").strip()
    
    df = load_data(file_name)
    if df is not None:
        df = calculate_revenue(df)
        report_text, product_revenue = generate_report(df)
        save_report(report_text)
        create_bar_chart(product_revenue)


# In[ ]:




