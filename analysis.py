# Libraries
import pandas as pd
import matplotlib.pyplot as plt


# Load dataset

df = pd.read_csv("dataset/SampleSuperstore.csv")

print("FIRST 5 ROWS")
print(df.head())

# Data

print("\nSHAPE OF DATA")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATA INFORMATION")
df.info()

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# Clean the data

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDATA TYPES AFTER CLEANING")
print(df.dtypes)

# Basic sales analysis

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

print("\nTOTAL SALES")
print(total_sales)

print("\nTOTAL PROFIT")
print(total_profit)

print("\nTOTAL QUANTITY SOLD")
print(total_quantity)

# Sales by category

category_sales = df.groupby("Category")["Sales"].sum()
print("\nSALES BY CATEGORY")
print(category_sales)

# Profit by category

category_profit = df.groupby("Category")["Profit"].sum()
print("\nPROFIT BY CATEGORY")
print(category_profit)

# Sales by region

region_sales = df.groupby("Region")["Sales"].sum()
print("\nSALES BY REGION")
print(region_sales)

# Profit by region

region_profit = df.groupby("Region")["Profit"].sum()
print("\nPROFIT BY REGION")
print(region_profit)

# Sales by sub-category

subcategory_sales = df.groupby("Sub-Category")["Sales"].sum()
print("\nSALES BY SUB-CATEGORY")
print(subcategory_sales)

# Profit by sub-category

subcategory_profit = df.groupby("Sub-Category")["Profit"].sum()
print("\nPROFIT BY SUB-CATEGORY")
print(subcategory_profit)

# Sales by segment

segment_sales = df.groupby("Segment")["Sales"].sum()
print("\nSALES BY CUSTOMER SEGMENT")
print(segment_sales)

# Profit by segment

segment_profit = df.groupby("Segment")["Profit"].sum()
print("\nPROFIT BY CUSTOMER SEGMENT")
print(segment_profit)

# Sales by state

state_sales = df.groupby("State")["Sales"].sum()
print("\nTOP 10 STATES BY SALES")
print(state_sales.sort_values(ascending=False).head(10))

# Profit by state

state_profit = df.groupby("State")["Profit"].sum()
print("\nTOP 10 STATES BY PROFIT")
print(state_profit.sort_values(ascending=False).head(10))

# Profit margin

profit_margin = (total_profit / total_sales) * 100
print("\nPROFIT MARGIN")
print(profit_margin)

# Average sales

average_sales = df["Sales"].mean()
print("\nAVERAGE SALES")
print(average_sales)

# Average profit

average_profit = df["Profit"].mean()
print("\nAVERAGE PROFIT")
print(average_profit)


# Bar chart - Sales by category

category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


# Bar chart - Sales by region

region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


# Bar chart - Profit by category

category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()


# Bar chart - Sales by sub-category

subcategory_sales.sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


# Bar chart - Profit by region

region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()


# Pie chart - Sales by customer segment

segment_sales.plot(kind="pie")
plt.title("Sales by Customer Segment")
plt.ylabel("")
plt.tight_layout()
plt.show()


# Final summary

print("\n========== FINAL SUMMARY ==========")

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Quantity Sold:", total_quantity)
print("Profit Margin:", profit_margin)
print("Average Sales:", average_sales)
print("Average Profit:", average_profit)


