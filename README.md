# 💼 E-Commerce Data Pipeline & Intelligence Dashboard

🚀 An end-to-end analytics project that transforms raw e-commerce data into business decisions — combining **Python, SQL, and Power BI** into a single workflow.

---

## 📌 Why This Project Exists

Most dashboards answer *what happened*.
Few explain *why it happened* or *what to do next*.

This project was built to bridge that gap.

Instead of treating Power BI as the starting point, I approached this like a real-world analytics problem:

* Raw, unstructured data
* Multiple sources
* No predefined insights

The goal was simple — **build a full pipeline and extract meaningful business signals from it.**

---

## 🧱 From Raw Data to Insight (End-to-End Workflow)

This project follows a structured data pipeline:

**Data Collection → Cleaning → Transformation → Modeling → Visualization → Insights**

Each step is handled using a specific tool, chosen for its strength.

---

## 🐍 Data Collection — Python

Using Python, raw datasets were gathered and structured into a consistent format.

* Used **pandas** for data manipulation and structuring
* Used **requests / BeautifulSoup** (where applicable) for data extraction
* Ensured schema consistency before downstream processing

👉 This stage focuses on **data acquisition and initial structuring**, ensuring the dataset is usable.

---

## 📊 Data Cleaning — Excel

Before moving into heavy transformations, the dataset was validated and cleaned in Excel.

* Removed duplicates and inconsistencies
* Standardized formats (dates, categories)
* Performed quick sanity checks

👉 Excel was used intentionally for **fast inspection and lightweight cleaning**, reducing noise early.

---

## 🗄️ Data Transformation — Microsoft SQL Server

SQL plays a critical role in shaping raw data into analysis-ready datasets.

* Joined multiple tables (Orders, Customers, Products)
* Created aggregated views (revenue, order counts)
* Filtered and structured data for reporting

👉 This is where raw data becomes **business-ready data**.

SQL ensures:

* Scalability
* Clarity in logic
* Reproducible transformations

---

## 🧠 Data Modeling — Microsoft Power BI

Inside Power BI, the data model was designed using a **star schema**.

* Fact table: Orders
* Dimension tables: Customers, Products, Date
* Relationships optimized for performance and filtering

👉 A strong data model ensures:

* Accurate calculations
* Efficient visuals
* Scalable reporting

---

## 🧮 Business Logic — DAX

DAX was used to translate business questions into measurable metrics.

Key measures include:

* Total Revenue
* Average Order Value (AOV)
* Revenue Growth % (MoM)
* Repeat Customer Rate
* Revenue per Customer

👉 DAX enables **context-aware calculations**, making insights dynamic and interactive.

---

## 📊 Visualization — Power BI

The final layer transforms data into a decision-making tool.

The dashboard is structured into three perspectives:

### Sales Performance

Understanding how revenue evolves over time and what drives it

### Customer Behavior

Analyzing retention, repeat purchases, and geographic distribution

### Product Performance

Evaluating which products generate value and how quality impacts sales

👉 Focus was placed on:

* Clear visual hierarchy
* KPI-driven storytelling
* Interactive filtering

---

## 🧠 What the Analysis Reveals

At a surface level, the business appears strong — revenue is growing, customers are returning, and high-value products are performing well.

But deeper analysis reveals structural patterns.

Growth exists, but it is uneven and driven by specific segments rather than broad expansion.
A single category contributes a large share of revenue, making the business dependent on it.
Even more critically, a small group of products dominates total sales.

Customer behavior suggests strong retention, but raises questions about new user acquisition.
Geographically, demand is concentrated in major cities, leaving expansion opportunities untapped.

---

## 🚨 Interpreting the Signals

This is not just a high-performing business — it is a **highly concentrated one**.

Its success depends on:

* A few key products
* A dominant category
* A loyal but potentially limited customer base

That combination creates both **strength and fragility**.

---

## 🚀 Where Data Points to Action

The analysis suggests clear next steps:

* Expand product diversity to reduce dependency
* Strengthen underperforming categories
* Invest in new customer acquisition channels
* Explore growth in non-metro regions
* Improve data collection to enable full funnel analysis

---

## 🛠️ Skills Demonstrated

This project showcases:

* **Python** → Data extraction and structuring
* **Excel** → Data cleaning and validation
* **SQL** → Data transformation and querying
* **Power BI** → Data modeling and visualization
* **DAX** → Business metric creation and time intelligence

---

## 📁 Project Structure

data → raw and processed datasets
dashboard → Power BI (.pbix) file
docs → requirements, insights, documentation
assets → dashboard screenshots

---

## 🎯 Final Perspective

This project demonstrates more than tool usage.

It shows how data can be:

* Collected
* Structured
* Transformed
* Interpreted

to uncover **not just what is happening, but why it matters**.

---

## 👤 Author

**Yusuf M**

Aspiring Data Analyst | SQL • Power BI • Python

---
