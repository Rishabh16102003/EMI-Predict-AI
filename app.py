import streamlit as st

st.set_page_config(page_title="ML App", layout="wide")

import streamlit as st

st.set_page_config(page_title="EMIPredict AI", page_icon="💰", layout="wide")

# Title
st.title("💰 EMIPredict AI")
st.subheader("Intelligent Financial Risk Assessment Platform")

st.markdown("---")

# About Project
st.header("📌 About the Project")

st.write("""
EMIPredict AI is a machine learning-powered platform designed to help users and financial institutions 
make smarter loan decisions by analyzing financial data and predicting EMI affordability.

This system combines classification and regression models to provide real-time insights into loan eligibility 
and safe EMI limits.
""")

# Key Features
st.header("🚀 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ✔ EMI Eligibility Prediction  
    ✔ Maximum EMI Estimation  
    ✔ Real-time Predictions  
    ✔ Multi-model ML system  
    """)

with col2:
    st.markdown(""" 
    ✔ 400K+ Data Processing  
    ✔ Feature Engineering  
    ✔ Interactive UI  
    """)

# How it works
st.header("⚙️ How It Works")

st.write("""
1. User enters financial details (salary, expenses, credit score, etc.)
2. Data is processed using feature engineering
3. ML models analyze risk and affordability
4. System provides:
   - EMI Eligibility Status
   - Maximum EMI Recommendation
""")

# Models Used
st.header("🧠 Machine Learning Models")

st.markdown("""
**Classification Models:**
- Logistic Regression  
- Random Forest  
- XGBoost  

**Regression Models:**
- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor  
""")

# Dataset Info
st.header("📊 Dataset Overview")

st.write("""
- Total Records: 400,000  
- Features: 22  
- Includes demographics, income, expenses, and credit data  
- Covers multiple EMI scenarios like personal loans, vehicles, education, etc.
""")

# Business Impact
st.header("💼 Business Impact")

st.markdown("""
- Faster loan approvals  
- Reduced financial risk  
- Data-driven decision making  
- Scalable for banks & fintech platforms  
""")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Machine Learning & Streamlit")
