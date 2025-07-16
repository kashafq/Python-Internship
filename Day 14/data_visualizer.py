#!/usr/bin/env python
# coding: utf-8

# # **Data Visualization**

# ### Importing libraries

# In[3]:


import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import datetime


# ### Loading the Dataset

# In[5]:


data=pd.read_csv(r"C:\Users\PMYLS\Documents\Sales Dataset.csv")
data


# ### Exploring the data

# In[9]:


data.info()


# In[11]:


data.isnull()


# In[13]:


data[data.duplicated()] 


# ### Convert Dates 

# In[16]:


data['Order Date']= pd.to_datetime(data['Order Date'])
data['Year-Month'] = data['Order Date'].dt.to_period('M').astype(str)
data


# ### Line Chart – Monthly Revenue

# In[19]:


import matplotlib.pyplot as plt

monthly_revenue=data.groupby('Year-Month')['Amount'].sum()

plt.figure(figsize=(10,5))
monthly_revenue.plot(marker='o',color='teal')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/Line Chart.png")
plt.show()


# ### Bar Chart – Sales by Sub-Category

# In[23]:


subcat_sales = data.groupby('Sub-Category')['Amount'].sum().sort_values()

plt.figure(figsize=(10,4))
subcat_sales.plot(kind='barh', color='green')
plt.title("Sales by Sub-Category")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig("plots/Bar Chart.png")
plt.show()


# ### Pie Chart – Market Share by Category

# In[21]:


category_share = data.groupby('Category')['Amount'].sum()

plt.figure(figsize=(5,5))
category_share.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Market Share by Category")
plt.ylabel('')
plt.tight_layout()
plt.savefig("plots/Pie Chart.png")
plt.show()


# ### Correlation Heatmap

# In[27]:


plt.figure(figsize=(8,5))
sb.heatmap(data[['Amount', 'Profit', 'Quantity']].corr(), annot=True, cmap='YlGnBu')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("plots/Heatmap.png")
plt.show()


# ### Summary Report Generation

# In[32]:


total_revenue=data['Amount'].sum()
total_profit=data['Profit'].sum()
top_category=data.groupby('Category')['Amount'].sum().idxmax()
top_subcat=data.groupby('Sub-Category')['Amount'].sum().idxmax()
best_month=monthly_revenue.idxmax()
best_month_amt=monthly_revenue.max()

print("---< Summary Report >---\n")
print(f"Total Revenue: Rs. {total_revenue:,.0f}")
print(f"Total Profit: Rs. {total_profit:,.0f}")
print(f"Top Category: {top_category}")
print(f"Top Sub-Category: {top_subcat}")
print(f"Best Month: {best_month} (Rs. {best_month_amt:,.0f})")

with open("Summary_Report.txt", "w") as f:
    f.write("Summary Report\n\n")
    f.write(f"Total Revenue: Rs. {total_revenue:,.0f}\n")
    f.write(f"Total Profit: Rs. {total_profit:,.0f}\n")
    f.write(f"Top Category: {top_category}\n")
    f.write(f"Top Sub-Category: {top_subcat}\n")
    f.write(f"Best Month: {best_month} (Rs. {best_month_amt:,.0f})\n")


# In[ ]:




