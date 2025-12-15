# ======================================================
# 1) SETUP & DATA ENGINE
# ======================================================
import streamlit as st
import pandas as pd
import statistics as stats
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Mini Home Annual Report", layout="wide")

def get_annual_data():
    CATEGORIES = ['Bedroom Sets', 'Sofas', 'Dining Tables', 'Office Chairs', 'Decor']
    START_DATE = datetime(2025, 1, 1)
    TRANSACTIONS = 1000
    data = []

    for i in range(TRANSACTIONS):
        date = START_DATE + timedelta(days=random.randint(0, 365))
        category = random.choice(CATEGORIES)
        
        if category == 'Bedroom Sets':
            price = random.randint(25000, 60000)
            cost = price * 0.65
        elif category == 'Sofas':
            price = random.randint(15000, 40000)
            cost = price * 0.60
        elif category == 'Dining Tables':
            price = random.randint(10000, 30000)
            cost = price * 0.60
        elif category == 'Office Chairs':
            price = random.randint(2000, 8000)
            cost = price * 0.50
        else:
            price = random.randint(500, 3000)
            cost = price * 0.40

        profit = price - cost
        data.append([date, category, price, cost, profit])

    return pd.DataFrame(data, columns=['Date', 'Category', 'Sales', 'Cost', 'Profit'])



# ======================================================
# 2) SIDEBAR & HEADER
# ======================================================
st.sidebar.title("MINI HOME 🇹🇷")
st.sidebar.markdown("---")

st.sidebar.write("Team Leader:")
st.sidebar.markdown("## 👑 ABDULILAH AL RIFAI")

st.sidebar.markdown("---")
st.sidebar.write("Team Members:")
st.sidebar.write("1. 👑 SHAMS BUKHARI")
st.sidebar.write("2. 👑 JUWAN ALQARNI")
st.sidebar.write("3. 👑 SARAH ALZUBAIRI")
st.sidebar.write("4. 👑 RAHAF ALI")

st.sidebar.markdown("---")
st.sidebar.caption("Fiscal Year: 2025 | Branch: Istanbul")

st.title("📑 Annual Performance Report (2025)")
st.markdown("### 🇹🇷 Turkey Branch | Final Year Analysis")



# ======================================================
# 3) ANALYTICS & VISUALIZATIONS
# ======================================================
df = get_annual_data()
df['Date'] = pd.to_datetime(df['Date'])

sales_list = df['Sales'].tolist()
total_revenue = sum(sales_list)
total_profit = sum(df['Profit'].tolist())
avg_sale = stats.mean(sales_list)
sales_count = len(sales_list)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue (YTD)", f"{total_revenue:,.0f} TL", "Target Met ✅")
col2.metric("Net Profit (2025)", f"{total_profit:,.0f} TL", "+8% vs 2024")
col3.metric("Total Transactions", f"{sales_count}")
col4.metric("Avg Ticket Size", f"{avg_sale:,.0f} TL")

st.markdown("---")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Sales Performance by Category")
    category_perf = (
        df.groupby('Category')[['Sales']]
        .sum()
        .sort_values(by='Sales', ascending=False)
    )
    st.bar_chart(category_perf, color="#ffaa00")

with col_right:
    st.subheader("Monthly Revenue Stream")
    df['Month'] = df['Date'].dt.month_name()
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    monthly_trend = df.groupby('Month')['Sales'].sum().reindex(month_order)
    st.line_chart(monthly_trend)



# ======================================================
# 4) DATA OUTPUT
# ======================================================
st.markdown("---")
st.subheader("📋 Transaction Ledger (Last 10 Records)")
st.dataframe(df.head(10), use_container_width=True)
