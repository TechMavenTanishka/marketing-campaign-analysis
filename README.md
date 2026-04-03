# 📊 Marketing Campaign Analysis Project

##  About the Project

This project analyzes customer data from a marketing campaign to understand customer behavior and improve business decisions.

The goal is to find:

* Who are the valuable customers
* Who spends more
* Who responds to campaigns
* How to improve marketing strategy

---

## 🛠️ Tools Used

* Python (Pandas, Matplotlib, Seaborn)
* SQL (SQLite)
* Streamlit (for dashboard)
* Plotly (for interactive charts)

---

## 📁 Project Structure

```
marketing_project/
│
├── app/            → Dashboard code (Streamlit)
├── data/           → Dataset files
├── notebooks/      → Data analysis (EDA)
├── sql/            → SQL scripts
├── report/         → Project report
├── README.md
├── requirements.txt
```
---

##  What I Did in This Project

### 1. Data Analysis
* Loaded and cleaned the dataset
* Checked missing values
* Explored customer data

### 2. Feature Engineering

Created new useful columns:

* Age
* Total Spend
* Total Purchases
* Customer Tenure

### 3. Data Visualization

* Age distribution
* Income distribution
* Spending patterns
* Campaign response

### 4. Customer Segmentation

Identified:
* High income customers
* High spenders
* Campaign responders
* Family customers

### 5. SQL Work
* Created table (DDL)
* Loaded data using Python (DML)
* Wrote queries for insights

### 6. Dashboard
Built an interactive dashboard using Streamlit with:

* Filters (Country, Education)
* KPI metrics
* Charts and graphs
* Automatic insights
---

## Key Insights

* Most customers are middle-aged
* Campaign response rate is low
* Many users visit website but don’t buy
* Only few customers spend a lot
---

## 💡 Business Suggestions

* Target high-income customers
* Improve marketing campaigns
* Focus on converting website visitors
* Design offers for family customers
---

## ▶️ How to Run the Project

### Step 1: Install dependencies
```
pip install -r requirements.txt
```

### Step 2: Run dashboard
```
streamlit run app/app.py
```

## 🧠 Conclusion

This project shows how data analysis can help businesses understand customers and improve marketing performance.

