# ACE-ACADEMY-PYTHON-PROJECT
README: Sales Data Analysis
Overview
This project performs data cleaning and exploratory data analysis (EDA) on a sales dataset. It utilizes Pandas for data manipulation, Matplotlib and Seaborn for visualization.

Features
Data Cleaning:
Converts ORDERDATE to datetime format.
Drops unnecessary columns (ADDRESSLINE1, ADDRESSLINE2, PHONE, etc.).
Fills missing values in categorical columns (STATE, POSTALCODE, TERRITORY).
Data Analysis:
Displays cleaned dataset information and first few rows.
Provides summary statistics (mean, standard deviation, min, max, etc.).
Computes mode values for numerical columns.
Data Visualization:
Annual Sales Trend – Line plot of total sales per year.
Monthly Sales Trend – Bar chart of total sales per month.
Top-Performing Product Lines – Bar chart of sales by product line.
Requirements
Ensure the following Python libraries are installed before running the script:
pip install pandas matplotlib seaborn
Usage
Place your sales_data.csv file in the same directory.
Update file_path in the script if needed.
Run the script using:
python script.py
View data insights printed in the console and displayed as visualizations.
Output
Console: Dataset summary, mode values, and key statistics.
Plots:
Annual sales trend (line plot).
Monthly sales trend (bar plot).
Sales performance of product lines (bar plot).
Notes
Ensure sales_data.csv has the expected columns.
Modify or extend the analysis as needed.
Happy Analyzing! 🚀
