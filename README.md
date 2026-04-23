# 📊 Sales Performance Analysis

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)

---

## 📌 Project Overview

This project performs an end-to-end Sales Performance Analysis on the Kaggle Superstore dataset. The goal is to analyze sales trends, identify top-performing regions, categories, and customers, and present the findings through an interactive Power BI dashboard.

---

## 🎯 Objectives

- Analyze sales performance across regions, categories, and customer segments
- Identify top 10 customers by total sales
- Track monthly and yearly sales trends
- Discover which product categories and sub-categories drive the most revenue
- Build an interactive Power BI dashboard for business decision-making

---

## 🗂️ Dataset Information

| Detail | Value |
|--------|-------|
| **Source** | Kaggle Superstore Dataset |
| **File Name** | train.csv |
| **Total Rows** | 9,800 |
| **Total Columns** | 18 |
| **Time Period** | 2015 to 2018 |
| **Missing Values** | 11 (Postal Code only) |

### Columns Available
```
Row ID | Order ID | Order Date | Ship Date | Ship Mode |
Customer ID | Customer Name | Segment | Country | City |
State | Postal Code | Region | Product ID | Category |
Sub-Category | Product Name | Sales
```

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python 3.13** | Data cleaning and analysis |
| **Pandas** | Data manipulation |
| **Matplotlib** | Chart generation |
| **Seaborn** | Advanced visualizations |
| **OpenPyXL** | Excel export |
| **Power BI Desktop** | Interactive dashboard |
| **Excel** | Data review and storage |
| **VS Code** | Code editor |

---

## 📁 Project Structure

```
Sales-Performance-Analysis/
│
├── 📄 main code.py                  # Python analysis script
├── 📄 Sales_Analysis_Report.xlsx    # Excel output with all analysis
├── 📄 Sales_Dashboard.pbix          # Power BI dashboard file
├── 📄 train.csv                     # Raw dataset
├── 📄 README.md                     # Project documentation
│
└── 📁 charts/
     ├── 01_region_sales.png         # Region wise sales bar chart
     ├── 02_category_sales.png       # Category wise sales chart
     ├── 03_monthly_trend.png        # Monthly sales trend line chart
     ├── 04_top_customers.png        # Top 10 customers bar chart
     ├── 05_segment_pie.png          # Segment distribution pie chart
     ├── 06_top_states.png           # Top 10 states bar chart
     ├── 07_subcategory_sales.png    # Sub-category sales chart
     ├── 08_yearly_trend.png         # Yearly sales trend chart
     └── 09_ship_mode.png            # Ship mode analysis chart
```

---

## ⚙️ How to Run This Project

### Step 1 — Clone the Repository
```bash
git clone https://github.com/yourusername/Sales-Performance-Analysis.git
cd Sales-Performance-Analysis
```

### Step 2 — Install Required Libraries
```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

### Step 3 — Run the Python Script
```bash
python "main code.py"
```

### Step 4 — View the Dashboard
```
Open Sales_Dashboard.pbix in Power BI Desktop
```

---

## 📊 Analysis Performed

### 1. Data Cleaning
- Removed 11 missing values from Postal Code column
- Removed duplicate records
- Converted Order Date and Ship Date to datetime format
- Extracted Year, Month, Quarter from dates
- Calculated Delivery Days for each order

### 2. Sales Analysis
- **Region Wise Sales** — Compared total sales across 4 regions
- **Category Wise Sales** — Analyzed Furniture, Technology, Office Supplies
- **Monthly Sales Trend** — Tracked sales pattern across 12 months
- **Yearly Sales Trend** — Year over year sales growth 2015-2018
- **Top 10 Customers** — Identified highest revenue customers
- **Segment Analysis** — Consumer, Corporate, Home Office comparison
- **Sub-Category Analysis** — 17 sub-categories ranked by sales
- **Top 10 States** — Geographic sales distribution
- **Ship Mode Analysis** — Delivery method performance

---

## 📈 Key Findings

| Finding | Detail |
|---------|--------|
| 🥇 **Top Region** | West Region has highest sales |
| 🥇 **Top Category** | Technology — 36.66% of total sales |
| 🥇 **Top Segment** | Consumer — 50.91% of total orders |
| 🥇 **Top Customer** | Sean Miller |
| 📅 **Peak Month** | November and December |
| 📈 **Sales Trend** | Growing year over year 2015 to 2018 |
| 💰 **Total Sales** | $2 Million across all years |
| 📦 **Total Orders** | 4,916 unique orders |
| 👥 **Total Customers** | 793 unique customers |
| 💵 **Avg Order Value** | $230.13 per order |

---

## 📉 Power BI Dashboard

The interactive dashboard includes:

- **4 KPI Cards** — Total Sales, Total Orders, Total Customers, Avg Order Value
- **Region Wise Sales** — Horizontal bar chart
- **Monthly Sales Trend** — Line chart with markers
- **Category Wise Sales** — Donut chart
- **Yearly Sales Trend** — Column chart (2015-2018)
- **Top 10 Customers** — Horizontal bar chart
- **Segment Distribution** — Pie chart
- **4 Slicers** — Filter by Region, Year, Category, Segment

---

## 🧠 Skills Demonstrated

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization using Python
- Dashboard Design in Power BI
- Excel Report Generation
- Business Insight Communication

---

## 👨‍💻 Author

**Jatin**
MCA Student — Himachal Pradesh University, Shimla (Batch 2024-2026)
Intern at Lecorb India Private Limited, Parwanoo

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- Dataset: [Kaggle Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- Tools: Python, Power BI Desktop, Microsoft Excel
