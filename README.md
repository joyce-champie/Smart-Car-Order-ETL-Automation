# Smart-Car-Order-ETL-Automation
Automates data collection from Google Forms into MySQL using Python. Eliminates manual spreadsheet handling and enables real-time access to structured order data. Lays the foundation for future dashboard integration and business intelligence.

# 📦 Live Google Form to MySQL ETL Pipeline

This project simulates a real-world data infrastructure solution built for a growing company that was facing operational inefficiencies due to **manual data collection**. 

The company relied on **Google Forms** to gather live order data but had no structured backend to store, query, or analyze the submissions. As a result, they were manually copying responses into spreadsheets — a process prone to delay, inconsistency, and human error.

This project solves that by implementing a **live ETL (Extract, Transform, Load) pipeline** using **Python and MySQL**.

---

## 🧠 Problem Statement

The organization needed a simple but effective solution to:
- Eliminate manual spreadsheet handling
- Store data securely in a relational database
- Enable real-time querying and analysis

There was **no dashboard**, no **central SQL database**, and **no automated process** to keep records updated.

---

## 🎯 Business Intelligence Objective

To automate the data collection pipeline from Google Forms to SQL, ensuring that business stakeholders have:
- Clean, structured order data
- Centralized storage for querying
- A scalable foundation for dashboards using tools like Tableau or Excel

---

## 🛠️ My Approach

1. **Google Form** created to simulate live order entry  
2. **Google Sheets** linked for real-time response capture  
3. **CSV Link Published** to access the sheet programmatically  
4. **Python Script** developed to:
   - Read the sheet with `pandas`
   - Clean and transform the data
   - Load into a MySQL table via `SQLAlchemy` and `PyMySQL`
5. **MySQL Workbench** used to verify that the records arrived as expected

---

## 💻 Tools & Libraries

| Tool / Library | Purpose |
|----------------|---------|
| Google Forms   | Data collection interface |
| Google Sheets  | Live form responses |
| Python (pandas) | Data extraction and transformation |
| SQLAlchemy + PyMySQL | Database connection & write |
| MySQL Workbench | Data verification and exploration |

---

## 🔁 ETL Pipeline Code Snippet

```python
import pandas as pd
from sqlalchemy import create_engine

# Step 1: Read the Google Sheet as CSV
sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTHocZE_g_tNtsvHxTL30x1fShYFQnAvy6WKTXQxbXgsOzd47E9iH7Hzw9gg0ZhiiiiOjscXmHMAemK/pub?output=csv'
df = pd.read_csv(sheet_url)

# Step 2: Connect to MySQL
engine = create_engine('mysql+pymysql://root:Root2025!@localhost:3306/mydb')

# Step 3: Upload to MySQL
df.to_sql('google_form_data', engine, if_exists='replace', index=False)

print("✅ Data loaded to MySQL")
