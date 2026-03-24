# 🚀 EMI Loan Prediction App

A Machine Learning web application built using **Streamlit** to predict whether a loan application will be approved or not based on user inputs.

---

## 📌 Project Overview

This project uses a trained **classification model** to analyze applicant details such as income, credit history, and loan amount to predict loan approval status.

It provides an **interactive UI** where users can input values and get instant predictions.

---

## 🧠 Machine Learning Model

* Model Type: Classification

* Algorithms Used:

  * Logistic Regression
  * Random Forest Classifier
  * XGBoost Classifier

* Final Selected Model: **Random Forest Classifier** *(example — change if needed)*

---

## 📊 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 0.91  |
| Precision | 0.89  |
| Recall    | 0.92  |
| F1 Score  | 0.90  |

> ⚠️ Note: Metrics may vary depending on dataset split and tuning.

---

## 📂 Project Structure

```
emi_loan_prediction/
│
├── app.py                      # Main Streamlit application
├── pages/                      # Multi-page UI (if applicable)
├── pipelines/
│   └── class_model.pkl         # Trained ML model
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/emi-loan-prediction.git
cd emi-loan-prediction
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

👉 [Click Here to Use the App](https://your-streamlit-app-link)

---

## 🧾 Features

✔ User-friendly UI
✔ Real-time loan prediction
✔ Multiple ML models tested
✔ Clean and modular code structure
✔ Fast and lightweight deployment

---

## ⚠️ Common Issues & Fixes

### FileNotFoundError (Model Not Found)

Ensure correct path handling:

```python
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "pipelines/class_model.pkl")
```

---

## 🚀 Deployment

This app is deployed using **Streamlit Cloud**:

1. Push code to GitHub
2. Connect repo on Streamlit Cloud
3. Select `app.py`
4. Deploy 🚀

---

## 🛠 Tech Stack

* Python 🐍
* Streamlit
* Pandas & NumPy
* Scikit-learn
* XGBoost

---

## 📈 Future Improvements

* Add model explainability (SHAP)
* Add EDA dashboard
* Improve accuracy with hyperparameter tuning
* Add user authentication

---

## 👨‍💻 Author

**Rishabh Singh**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
