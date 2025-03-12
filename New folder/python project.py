import pandas as pd
# Load dataset
file_path = "sales_data.csv"  # Update this path if needed
df = pd.read_csv(file_path, encoding="latin1")
# Convert ORDERDATE to datetime format
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")
# Drop unnecessary columns
df_cleaned = df.drop(columns=["ADDRESSLINE1", "ADDRESSLINE2", "PHONE", "CONTACTLASTNAME", "CONTACTFIRSTNAME"])
# Fill missing values in categorical columns
for col in ["STATE", "POSTALCODE", "TERRITORY"]:
    df_cleaned[col] = df_cleaned[col].fillna("Unknown")
# Display dataset info
print("Dataset Info After Cleaning:")
print(df_cleaned.info())
print("\nFirst 5 Rows:\n", df_cleaned.head())
# Summary statistics
summary_stats = df_cleaned[["SALES", "QUANTITYORDERED", "PRICEEACH"]].describe()

# Compute mode separately (since describe() does not include mode)
mode_values = df_cleaned[["SALES", "QUANTITYORDERED", "PRICEEACH"]].mode().iloc[0]

# Print summary statistics
print("Summary Statistics:\n", summary_stats)
print("\nMode Values:\n", mode_values)
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set_style("whitegrid")

# Annual Sales Trend
annual_sales = df_cleaned.groupby("YEAR_ID")["SALES"].sum()
plt.figure(figsize=(8, 5))
sns.lineplot(x=annual_sales.index, y=annual_sales.values, marker="o", linewidth=2)
plt.title("Annual Sales Trend", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.xticks(annual_sales.index)
plt.show()

# Monthly Sales Trend
monthly_sales = df_cleaned.groupby("MONTH_ID")["SALES"].sum()
plt.figure(figsize=(10, 5))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values, palette="viridis")
plt.title("Monthly Sales Trend", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.xticks(range(1, 13))
plt.show()

# Top Performing Product Lines
product_sales = df_cleaned.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=product_sales.values, y=product_sales.index, palette="coolwarm")
plt.title("Top-Performing Product Lines", fontsize=14)
plt.xlabel("Total Sales ($)", fontsize=12)
plt.ylabel("Product Line", fontsize=12)
plt.show()
