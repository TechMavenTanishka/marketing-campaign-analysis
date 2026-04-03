import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Marketing Dashboard", layout="wide")

# Title
st.title("📊 Marketing Campaign Dashboard")

# Load data
df = pd.read_csv('data/marketing_campaign_data.csv')

# Create features
df['Total_Spend'] = (
    df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] +
    df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
)

df['Age'] = 2024 - df['Year_Birth']

# Sidebar
st.sidebar.header("🔎 Filters")

country = st.sidebar.selectbox("Select Country", df['Country'].unique())
education = st.sidebar.multiselect("Select Education", df['Education'].unique(), default=df['Education'].unique())

# Filter data
filtered_df = df[(df['Country'] == country) & (df['Education'].isin(education))]

# ---------------- KPI SECTION ----------------
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Customers", len(filtered_df))
col2.metric("💰 Avg Income", int(filtered_df['Income'].mean()))
col3.metric("🛒 Total Spend", int(filtered_df['Total_Spend'].sum()))
col4.metric("📈 Response Rate", f"{round(filtered_df['Response'].mean()*100,2)}%")

# ---------------- CHARTS ----------------
st.subheader("📊 Insights")

col1, col2 = st.columns(2)

# Age Distribution
fig1 = px.histogram(filtered_df, x='Age', nbins=30, title="Age Distribution")
col1.plotly_chart(fig1, use_container_width=True)

# Income Distribution
fig2 = px.histogram(filtered_df, x='Income', nbins=30, title="Income Distribution")
col2.plotly_chart(fig2, use_container_width=True)

# Spend vs Age
fig3 = px.scatter(filtered_df, x='Age', y='Total_Spend', title="Age vs Total Spend")
st.plotly_chart(fig3, use_container_width=True)

# Education Distribution
edu_df = filtered_df['Education'].value_counts().reset_index()
edu_df.columns = ['Education', 'Count']

fig4 = px.bar(
    edu_df,
    x='Education',
    y='Count',
    title="Education Distribution"
)

st.plotly_chart(fig4, use_container_width=True)

# Response Count
fig5 = px.pie(filtered_df, names='Response', title="Campaign Response")
st.plotly_chart(fig5, use_container_width=True)

st.subheader("🎯 Customer Segmentation")

col1, col2, col3 = st.columns(3)

high_income = filtered_df[filtered_df['Income'] > 75000]
high_spenders = filtered_df[filtered_df['Total_Spend'] > filtered_df['Total_Spend'].quantile(0.9)]
responders = filtered_df[filtered_df['Response'] == 1]

col1.metric("💰 High Income", len(high_income))
col2.metric("🛒 High Spenders", len(high_spenders))
col3.metric("📈 Responders", len(responders))

st.subheader("🏆 Top 10 High Spending Customers")

top_spenders = filtered_df.sort_values(by='Total_Spend', ascending=False).head(10)

fig6 = px.bar(top_spenders, x='ID', y='Total_Spend',
              title="Top 10 Customers by Spend")

st.plotly_chart(fig6, use_container_width=True)

st.subheader("🧠 Key Insights")

avg_income = filtered_df['Income'].mean()
response_rate = filtered_df['Response'].mean() * 100

st.write(f"👉 Average income of selected customers is **{int(avg_income)}**")

if response_rate < 20:
    st.warning("⚠️ Campaign response rate is low → Improve targeting strategy")
else:
    st.success("✅ Campaign performing well")

if len(high_spenders) < len(filtered_df) * 0.15:
    st.info("💡 Only few high spenders → Focus marketing on premium customers")

if filtered_df['NumWebVisitsMonth'].mean() > 5:
    st.info("🌐 High web visits but low conversion → Improve website offers")