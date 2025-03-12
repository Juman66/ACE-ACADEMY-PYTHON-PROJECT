# Sales Data Analysis

## 📌 Overview
This project analyzes sales data from a CSV file (`sales_data.csv`). The script cleans the data, generates summary statistics, and visualizes sales trends to gain insights into business performance.

## 🛠 Features
### 🔹 Data Cleaning
- Converts `ORDERDATE` to datetime format.
- Drops unnecessary columns (`ADDRESSLINE1`, `ADDRESSLINE2`, `PHONE`, `CONTACTLASTNAME`, `CONTACTFIRSTNAME`).
- Fills missing values in `STATE`, `POSTALCODE`, and `TERRITORY` with `"Unknown"`.

### 🔹 Statistical Summary
- Computes descriptive statistics (`mean`, `min`, `max`, `std`, etc.) for:
  - `SALES`
  - `QUANTITYORDERED`
  - `PRICEEACH`
- Calculates mode for these numerical columns.

### 🔹 Data Visualization
- **Annual Sales Trend:** Line chart displaying yearly sales growth.
- **Monthly Sales Trend:** Bar chart showing total sales per month.
- **Top-Performing Product Lines:** Bar chart ranking product categories by revenue.

## 📂 Dataset
- **Input File:** `sales_data.csv`
- **Expected Columns:** 
  - `ORDERDATE`, `SALES`, `QUANTITYORDERED`, `PRICEEACH`, `YEAR_ID`, `MONTH_ID`, `PRODUCTLINE`, `STATE`, `POSTALCODE`, `TERRITORY`
- **Format:** CSV (Comma-Separated Values)

## ⚙️ Requirements
Ensure you have the following dependencies installed:

```sh
pip install pandas matplotlib seaborn


🚀 Usage
Place the sales_data.csv file in the same directory as the script.
Run the script using:
sh
Copy
Edit
python script.py
The script will display:
Cleaned dataset info
Summary statistics
Sales trend visualizations
📊 Sample Visualizations
🔹 Annual Sales Trend
A line chart illustrating yearly sales performance.

🔹 Monthly Sales Trend
A bar chart showing sales distribution across months.

🔹 Top-Performing Product Lines
A bar chart highlighting the highest revenue-generating product categories.

🛠 Customization
Update the file_path variable to specify a different dataset location.
Modify visualizations or add new ones based on business needs.
📄 License
This project is open-source and can be freely modified and distributed.

Let me know if you need any modifications! 🚀
