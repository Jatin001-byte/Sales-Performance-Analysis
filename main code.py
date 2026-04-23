# ============================================
# SALES PERFORMANCE ANALYSIS
# Dataset: train.csv (Superstore)
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ============================================
# PART 1 — LOAD DATA
# ============================================

df = pd.read_csv(
    r'C:\Users\jg657\Desktop\sales analysis dashboard\train.csv',
    encoding='latin-1'
)

print("✅ Data Loaded Successfully")
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# ============================================
# PART 2 — CLEAN DATA
# ============================================

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# ✅ Fix 1 — Date format fixed with dayfirst=True
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date']  = pd.to_datetime(df['Ship Date'],  dayfirst=True)

# Extract useful date parts
df['Order Year']       = df['Order Date'].dt.year
df['Order Month']      = df['Order Date'].dt.month
df['Order Month Name'] = df['Order Date'].dt.strftime('%B')
df['Order Quarter']    = df['Order Date'].dt.quarter

# Delivery Days calculation
df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days

print("\n✅ Data Cleaned Successfully")
print("Clean Data Shape:", df.shape)

# ============================================
# PART 3 — ANALYSIS
# ============================================

# Overall Summary
total_sales     = df['Sales'].sum()
total_orders    = df['Order ID'].nunique()
total_customers = df['Customer Name'].nunique()
avg_order_value = df['Sales'].mean()

print("\n========== OVERALL SUMMARY ==========")
print(f"Total Sales       : $ {total_sales:,.2f}")
print(f"Total Orders      : {total_orders}")
print(f"Total Customers   : {total_customers}")
print(f"Avg Order Value   : $ {avg_order_value:,.2f}")

# Analysis 1 — Region Wise Sales
print("\n========== REGION WISE SALES ==========")
region_sales = df.groupby('Region')['Sales'].sum() \
                 .reset_index() \
                 .sort_values('Sales', ascending=False)
print(region_sales)

# Analysis 2 — Category Wise Sales
print("\n========== CATEGORY WISE SALES ==========")
category = df.groupby('Category')['Sales'].sum() \
             .reset_index() \
             .sort_values('Sales', ascending=False)
print(category)

# Analysis 3 — Monthly Sales Trend
print("\n========== MONTHLY SALES TREND ==========")
monthly = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().reset_index()
print(monthly)

# Analysis 4 — Top 10 Customers
print("\n========== TOP 10 CUSTOMERS ==========")
top_customers = df.groupby('Customer Name')['Sales'].sum() \
                  .reset_index() \
                  .sort_values('Sales', ascending=False) \
                  .head(10)
print(top_customers)

# Analysis 5 — Segment Wise Sales
print("\n========== SEGMENT WISE SALES ==========")
segment = df.groupby('Segment').agg({
    'Sales'   : 'sum',
    'Order ID': 'count'
}).reset_index()
segment.columns = ['Segment', 'Total Sales', 'Total Orders']
print(segment)

# Analysis 6 — Ship Mode Analysis
print("\n========== SHIP MODE ANALYSIS ==========")
ship_mode = df.groupby('Ship Mode').agg({
    'Sales'        : 'sum',
    'Delivery Days': 'mean'
}).reset_index()
ship_mode.columns = ['Ship Mode', 'Total Sales', 'Avg Delivery Days']
print(ship_mode)

# Analysis 7 — Sub Category Wise Sales
print("\n========== SUB CATEGORY WISE SALES ==========")
sub_cat = df.groupby('Sub-Category')['Sales'].sum() \
            .reset_index() \
            .sort_values('Sales', ascending=False)
print(sub_cat)

# Analysis 8 — Top 10 States
print("\n========== TOP 10 STATES ==========")
top_states = df.groupby('State')['Sales'].sum() \
               .reset_index() \
               .sort_values('Sales', ascending=False) \
               .head(10)
print(top_states)

# Analysis 9 — Yearly Sales
print("\n========== YEARLY SALES ==========")
yearly = df.groupby('Order Year')['Sales'].sum().reset_index()
print(yearly)

# ============================================
# PART 4 — CHARTS
# ============================================

# Create charts folder
os.makedirs('charts', exist_ok=True)
sns.set_style("whitegrid")

# Chart 1 — Region Wise Sales
plt.figure(figsize=(8, 5))
sns.barplot(data=region_sales, x='Region', y='Sales', palette='Blues_d')
plt.title('Region Wise Sales', fontsize=16, fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('charts/01_region_sales.png')
plt.show()
print("✅ Chart 1 Done — Region Wise Sales")

# Chart 2 — Category Wise Sales
plt.figure(figsize=(8, 5))
sns.barplot(data=category, x='Category', y='Sales', palette='Greens_d')
plt.title('Category Wise Sales', fontsize=16, fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('charts/02_category_sales.png')
plt.show()
print("✅ Chart 2 Done — Category Wise Sales")

# Chart 3 — Monthly Sales Trend
plt.figure(figsize=(12, 5))
monthly_all = df.groupby('Order Month')['Sales'].sum().reset_index()
sns.lineplot(data=monthly_all, x='Order Month', y='Sales',
             marker='o', color='blue', linewidth=2.5)
plt.title('Monthly Sales Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(range(1, 13),
           ['Jan','Feb','Mar','Apr','May','Jun',
            'Jul','Aug','Sep','Oct','Nov','Dec'])
plt.tight_layout()
plt.savefig('charts/03_monthly_trend.png')
plt.show()
print("✅ Chart 3 Done — Monthly Trend")

# Chart 4 — Top 10 Customers
plt.figure(figsize=(10, 6))
sns.barplot(data=top_customers, x='Sales', y='Customer Name', palette='Oranges_d')
plt.title('Top 10 Customers by Sales', fontsize=16, fontweight='bold')
plt.xlabel('Total Sales ($)')
plt.ylabel('Customer Name')
plt.tight_layout()
plt.savefig('charts/04_top_customers.png')
plt.show()
print("✅ Chart 4 Done — Top Customers")

# Chart 5 — Segment Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(segment['Total Sales'],
        labels=segment['Segment'],
        autopct='%1.1f%%',
        colors=['#FF6B6B', '#4ECDC4', '#45B7D1'],
        startangle=90)
plt.title('Segment Wise Sales Distribution', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/05_segment_pie.png')
plt.show()
print("✅ Chart 5 Done — Segment Pie")

# Chart 6 — Top 10 States
plt.figure(figsize=(10, 6))
sns.barplot(data=top_states, x='Sales', y='State', palette='Purples_d')
plt.title('Top 10 States by Sales', fontsize=16, fontweight='bold')
plt.xlabel('Total Sales ($)')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('charts/06_top_states.png')
plt.show()
print("✅ Chart 6 Done — Top States")

# Chart 7 — Sub Category Sales
plt.figure(figsize=(12, 7))
sns.barplot(data=sub_cat, x='Sales', y='Sub-Category', palette='coolwarm')
plt.title('Sub-Category Wise Sales', fontsize=16, fontweight='bold')
plt.xlabel('Total Sales ($)')
plt.ylabel('Sub-Category')
plt.tight_layout()
plt.savefig('charts/07_subcategory_sales.png')
plt.show()
print("✅ Chart 7 Done — Sub Category")

# Chart 8 — Yearly Sales
plt.figure(figsize=(8, 5))
sns.barplot(data=yearly, x='Order Year', y='Sales', palette='Blues_d')
plt.title('Yearly Sales Trend', fontsize=16, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('charts/08_yearly_trend.png')
plt.show()
print("✅ Chart 8 Done — Yearly Trend")

# Chart 9 — Ship Mode Sales
plt.figure(figsize=(9, 5))
sns.barplot(data=ship_mode, x='Ship Mode', y='Total Sales', palette='Set2')
plt.title('Ship Mode Wise Sales', fontsize=16, fontweight='bold')
plt.xlabel('Ship Mode')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('charts/09_ship_mode.png')
plt.show()
print("✅ Chart 9 Done — Ship Mode")

# ============================================
# PART 5 — EXPORT TO EXCEL
# ============================================

with pd.ExcelWriter('Sales_Analysis_Report.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer,            sheet_name='Clean Data',       index=False)
    region_sales.to_excel(writer,  sheet_name='Region Sales',     index=False)
    category.to_excel(writer,      sheet_name='Category Sales',   index=False)
    monthly.to_excel(writer,       sheet_name='Monthly Trend',    index=False)
    top_customers.to_excel(writer, sheet_name='Top Customers',    index=False)
    segment.to_excel(writer,       sheet_name='Segment Analysis', index=False)
    sub_cat.to_excel(writer,       sheet_name='Sub Category',     index=False)
    top_states.to_excel(writer,    sheet_name='Top States',       index=False)
    ship_mode.to_excel(writer,     sheet_name='Ship Mode',        index=False)
    yearly.to_excel(writer,        sheet_name='Yearly Sales',     index=False)

print("\n✅ Excel Report Created — Sales_Analysis_Report.xlsx")
print("\n🎉 ALL ANALYSIS COMPLETE!")
print("📁 Charts saved in 'charts' folder")
print("📊 Excel report saved in project folder")