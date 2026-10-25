"""
Skill Nexis Week 2 – Python for Data Analysis
Dataset: SQL_Sales_Dataset_200_Rows.xlsx.xlsx
Install if needed: pip install pandas openpyxl
Place this script and the Excel dataset in the same folder before running.
"""
import pandas as pd

FILE = "SQL_Sales_Dataset_200_Rows.xlsx.xlsx"

# Q1. Load the dataset and display basic information
df = pd.read_excel(FILE)
print("\nQ1: First five rows")
print(df.head())
print("\nDataset shape (rows, columns):", df.shape)
print("\nColumn information:")
df.info()
print("\nNumerical summary:")
print(df.describe(numeric_only=True))

# Q2. Handle missing values and duplicates
print("\nQ2: Missing values before cleaning")
print(df.isna().sum())
print("Duplicate rows before cleaning:", df.duplicated().sum())

df = df.drop_duplicates()
# Fill numeric missing values with median; text/date values with mode if available.
for col in df.select_dtypes(include="number").columns:
    if df[col].isna().any():
        df[col] = df[col].fillna(df[col].median())
for col in df.select_dtypes(include=["object", "category"]).columns:
    if df[col].isna().any() and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])
for col in df.select_dtypes(include=["datetime"]).columns:
    if df[col].isna().any() and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after cleaning")
print(df.isna().sum())
print("Duplicate rows after cleaning:", df.duplicated().sum())

# Q3. Group by category and calculate total revenue.
# In this dataset, total_price represents the total amount per order line.
print("\nQ3: Total revenue by category")
revenue = (df.groupby("category", as_index=False)["total_price"]
             .sum().rename(columns={"total_price": "total_revenue"})
             .sort_values("total_revenue", ascending=False))
print(revenue.to_string(index=False))

# Q4. Sort by multiple columns: category A-Z, then total_price high-to-low
print("\nQ4: Sorted by category ascending, total_price descending")
print(df.sort_values(by=["category", "total_price"],
                     ascending=[True, False]).to_string(index=False))

# Q5. Correlation matrix for numeric columns
print("\nQ5: Correlation matrix")
print(df.corr(numeric_only=True).round(3))

# Save useful outputs for submission/review
df.to_csv("cleaned_sales_dataset.csv", index=False)
revenue.to_csv("revenue_by_category.csv", index=False)
df.sort_values(by=["category", "total_price"], ascending=[True, False]).to_csv(
    "sorted_sales_data.csv", index=False)
df.corr(numeric_only=True).to_csv("correlation_matrix.csv")
print("\nSaved cleaned_sales_dataset.csv, revenue_by_category.csv, "
      "sorted_sales_data.csv, and correlation_matrix.csv")
