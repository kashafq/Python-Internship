# data_visualizer.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import logging
import os

# Setup logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create plots directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

# Custom Exception
class DatasetNotFoundError(Exception):
    pass

def load_data(filepath):
    if not os.path.exists(filepath):
        logging.error(f"Dataset file not found: {filepath}")
        raise DatasetNotFoundError("CSV file not found.")
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        logging.error(f"Error loading CSV: {e}")
        raise

def preprocess_data(data):
    try:
        data['Order Date'] = pd.to_datetime(data['Order Date'])
        data['Year-Month'] = data['Order Date'].dt.to_period('M').astype(str)
        return data
    except Exception as e:
        logging.error(f"Date conversion failed: {e}")
        raise

def generate_plots(data):
    try:
        # Line Chart – Monthly Revenue
        monthly_revenue = data.groupby('Year-Month')['Amount'].sum()
        plt.figure(figsize=(10, 5))
        monthly_revenue.plot(marker='o', color='teal')
        plt.title("Monthly Revenue")
        plt.xlabel("Month")
        plt.ylabel("Total Revenue")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("plots/Line Chart.png")
        plt.close()

        # Bar Chart – Sub-Category
        subcat_sales = data.groupby('Sub-Category')['Amount'].sum().sort_values()
        plt.figure(figsize=(10, 4))
        subcat_sales.plot(kind='barh', color='green')
        plt.title("Sales by Sub-Category")
        plt.xlabel("Revenue")
        plt.tight_layout()
        plt.savefig("plots/Bar Chart.png")
        plt.close()

        # Pie Chart – Category Market Share
        category_share = data.groupby('Category')['Amount'].sum()
        plt.figure(figsize=(5, 5))
        category_share.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title("Market Share by Category")
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig("plots/Pie Chart.png")
        plt.close()

        # Heatmap
        plt.figure(figsize=(8, 5))
        sb.heatmap(data[['Amount', 'Profit', 'Quantity']].corr(), annot=True, cmap='YlGnBu')
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.savefig("plots/Heatmap.png")
        plt.close()
    except Exception as e:
        logging.error(f"Error generating plots: {e}")
        raise

def generate_summary(data, monthly_revenue):
    try:
        total_revenue = data['Amount'].sum()
        total_profit = data['Profit'].sum()
        top_category = data.groupby('Category')['Amount'].sum().idxmax()
        top_subcat = data.groupby('Sub-Category')['Amount'].sum().idxmax()
        best_month = monthly_revenue.idxmax()
        best_month_amt = monthly_revenue.max()

        with open("Summary_Report.txt", "w") as f:
            f.write("Summary Report\n\n")
            f.write(f"Total Revenue: Rs. {total_revenue:,.0f}\n")
            f.write(f"Total Profit: Rs. {total_profit:,.0f}\n")
            f.write(f"Top Category: {top_category}\n")
            f.write(f"Top Sub-Category: {top_subcat}\n")
            f.write(f"Best Month: {best_month} (Rs. {best_month_amt:,.0f})\n")

        print("✅ Summary report generated.")
    except Exception as e:
        logging.error(f"Error writing summary: {e}")
        raise

def main():
    try:
        filepath = "Sales Dataset.csv"
        data = load_data(filepath)
        data = preprocess_data(data)
        generate_plots(data)
        monthly_revenue = data.groupby('Year-Month')['Amount'].sum()
        generate_summary(data, monthly_revenue)
    except DatasetNotFoundError as e:
        print(f"❌ {e}")
    except Exception as e:
        print("❌ An unexpected error occurred. Check error_log.txt.")

if __name__ == "__main__":
    main()
