import streamlit as st
from src.predic import predict_regression
import pandas as pd


st.set_page_config(page_title="Max EMI Prediction", layout="centered")

st.title("📊 Max Eligible EMI Prediction")
st.write("Please provide your employment and monthly expense details.")

with st.form("financial_form"):
# --- Part 1: Employment & Loan Context ---
    st.subheader("Employment & Scenario")
    col_emp, col_loan = st.columns(2)

    with col_emp:
        monthly_salary = st.number_input("Salary", min_value=0, step=50)
        bank_balance = st.number_input("Bankbalance", min_value=0, step=50)
        credit_score = st.number_input("Credit Score", 300, 850, 650,
            placeholder='enter_credit_score')

    with col_loan:
        existing_loans = st.selectbox(
            "Do you have existing loans?",
            options=['Yes','No'],
            index=None,
            placeholder='select_option'
        )
        education = st.selectbox(
        "Education Level",
        options=['Not_to_disclose','High School','Post Graduate',
                'Professional','Graduate'],
        index=None,
        placeholder='select_option'
        
    )
        emergency_fund = st.number_input("Emergency Fund", min_value=0, step=50)


# --- Part 2: Monthly Expenses (Grouped for better UI) ---
    with st.expander("💳 Monthly Expense Details", expanded=True):
        st.info("Enter your average monthly expenditure for the following categories:")
    
        ex_col1, ex_col2 = st.columns(2)
    
        with ex_col1:
            groceries = st.number_input("Groceries", min_value=0, step=50)
            college_fees = st.number_input("College Fees", min_value=0, step=500)
            school_fees = st.number_input("School Fees", min_value=0, step=500)
            current_emi = st.number_input("Current EMI Amount", min_value=0, step=100)

        with ex_col2:
            rent = st.number_input("Rent/Mortgage", min_value=0, step=500)
            travel_expense = st.number_input("Travel/Fuel Expense", min_value=0, step=50)
            miscellaneous = st.number_input("Miscellaneous Expenses", min_value=0, step=50)

    # Submit
    submitted = st.form_submit_button("Calculate Monthly EMI")

if submitted:
# Totaling expenses for logic
    total_monthly_expenses = (
    groceries + college_fees + school_fees + 
    current_emi + rent + travel_expense + miscellaneous
    )
    expense_salary_ratio=total_monthly_expenses/monthly_salary

# st.success("Data Captured!")
# st.metric("Total Monthly Outflow", f"${total_monthly_expenses:,.2f}")
    edu=0
    if education=='Not_to_disclose':
        edu=0
    elif education=='High School':
        edu=1
    elif education=='Graduate':
        edu=2
    elif education=='Post Graduate':
        edu=3
    elif education=='Professional' :
        edu=4
    exist_loan=''
    if existing_loans=='Yes':
        exist_loan=1
    elif existing_loans=='No':
        exist_loan=0

    input_df = pd.DataFrame({
    "education": [edu],
    "credit_score": [credit_score],
    "monthly_salary": [monthly_salary],
    "bank_balance": [bank_balance],
    "emergency_fund": [emergency_fund],
    "existing_loans": [exist_loan],
    "expense_salary_ratio": [expense_salary_ratio]
    })

    result = predict_regression(input_df)
    st.success(f'Max Monthly Emi={result}')