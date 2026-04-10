#  Big Data Customer Satisfaction Analysis

##  Overview
This project analyzes a large-scale e-commerce dataset to identify the key factors that influence customer satisfaction. It combines **data preprocessing, big data processing (MapReduce), machine learning (PySpark), and Tableau dashboards** to generate actionable business insights.

---

##  Objective
To understand what affects customer satisfaction the most and build a predictive model to classify customer sentiment.

---

## ⚙️ Project Workflow

###  1. Data Preparation
- Cleaned and merged multiple datasets  
- Handled missing values and inconsistencies  
- Converted semi-structured data into structured format  
- Created new features:
  - `satisfaction_category`
  - `delay_category`
  - `total_price`, `total_freight`
  - `num_items`

  File:
- `preparing_for_classification.ipynb`

---

###  2. Big Data Processing (MapReduce)
Used Hadoop-style MapReduce to aggregate customer satisfaction across key factors:
- Delay category  
- Price bins  
- Freight bins  
- Number of items  

 Files:
- `mapper.py` → emits key-value pairs for analysis :contentReference[oaicite:0]{index=0}  
- `reducer.py` → aggregates satisfaction counts :contentReference[oaicite:1]{index=1}  

---

###  3. Machine Learning (PySpark)
- Built a **Random Forest classification model**
- Created a full ML pipeline:
  - Encoding categorical variables  
  - Handling missing values  
  - Feature vector assembly  
- Evaluated using:
  - Accuracy  
  - Precision  
  - Recall  
  - F1-score  

 File:
- `classification.ipynb`

---

##  Dashboards (Tableau)

###  Customer Satisfaction Drivers
![Customer Satisfaction Drivers](images/dashboard1)

### 🔹 Feature Impact Analysis
![Feature Impact](images/dashboard2.png)

### 🔹 Prediction Accuracy Dashboard
![Prediction Accuracy](images/dashboard3.png)

---

## 📈 Key Findings

###  Delivery Impact
- Delayed deliveries are the **main cause of dissatisfaction**
- On-time deliveries strongly correlate with satisfied customers  

---

###  Pricing & Freight
- High freight costs reduce satisfaction  
- Customers are sensitive to pricing changes  
- Medium pricing levels show better satisfaction  

---

###  Order Size
- Very small or very large orders tend to reduce satisfaction  
- Balanced orders perform better  

---

###  Model Performance
- Most predictions are correct  
- The **“satisfied” category is hardest to predict**  
- Misclassifications mostly occur between similar categories  

---

##  Business Recommendations
- Improve delivery speed and logistics  
- Reduce or optimize shipping costs  
- Adjust pricing strategies based on customer expectations  
- Use predictive models to identify unhappy customers early  

---

##  Tech Stack
- Python (Pandas, NumPy)  
- PySpark (MLlib)  
- Hadoop MapReduce  
- Tableau  

---

## 📁 Project Structure
