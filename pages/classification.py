import streamlit as st
from src.predic import predict_classification
import pandas as pd


st.set_page_config(page_title="Detailed Loan Application", layout="centered")

st.title("📊 Enhanced Loan Eligibility Form")
st.write("Please provide your employment and monthly expense details.")

with st.form("financial_form"):
    # --- Part 1: Employment & Loan Context ---
    st.subheader("Employment & Scenario")
    col_emp, col_loan = st.columns(2)
        
    with col_emp:
        employment_type = st.selectbox(
            "Employment Type",
            options=['Government', 'Self-Employed',
                    'Private'],
            index=None,
            placeholder='select_option'
        )

        emi_scenario = st.selectbox(
            "EMI Scenario",
            options=['Online Shopping Emi','Education Loan','Home Applainces Emi',
                    'Personal Loan','Car Loan'],
            index=None,
            placeholder='select_option'

        )
        monthly_salary = st.number_input("Salary", min_value=0, step=50)
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
        bank_balance = st.number_input("Bankbalance", min_value=0, step=50)
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

    # --- Part 3: Core Financials ---
    st.subheader("Requested Loan Details")
    c1, c2 = st.columns(2)
    with c1:
        req_amount = st.number_input("Requested Amount", min_value=100)
    with c2:
        req_tenure = st.number_input("Tenure (Months)", 3, 84, 12)

        # Submit
    submitted = st.form_submit_button("Calculate Eligibility")

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
    
    emp_type=[]
    if employment_type=='Government':
        emp_type=[1,0,0]
    elif employment_type=='Self-Employed':
        emp_type=[0,0,1]
    elif employment_type=='Private':
        emp_type=[0,1,0]                   
    emi_scene=[]
    if emi_scenario=='Online Shopping Emi':
        emi_scene=[1,0,0,0,0]
    elif emi_scenario=='Education Loan':
        emi_scene=[0,1,0,0,0]
    elif emi_scenario=='Home Applainces Emi':
        emi_scene=[0,0,1,0,0]
    elif emi_scenario=='Personal Loan':
        emi_scene=[0,0,0,1,0]
    elif emi_scenario=='Car Loan':
        emi_scene=[0,0,0,0,1]
                    
                    
                                    
    

    input_df = pd.DataFrame({
    "education": [edu],
    "credit_score": [credit_score],
    "monthly_salary": [monthly_salary],
    "bank_balance": [bank_balance],
    "emergency_fund": [emergency_fund],
    "requested_amount": [req_amount],
    "requested_tenure": [req_tenure],
    "employment_type_Government": [emp_type[0]],
    "employment_type_Private": [emp_type[1]],
    "employment_type_Self-employed": [emp_type[2]],
    "emi_scenario_E-commerce Shopping EMI": [emi_scene[0]],
    "emi_scenario_Education EMI": [emi_scene[1]],
    "emi_scenario_Home Appliances EMI": [emi_scene[2]],
    "emi_scenario_Personal Loan EMI": [emi_scene[3]],
    "emi_scenario_Vehicle EMI": [emi_scene[4]],
    "expense_salary_ratio": [expense_salary_ratio]
    })

    result = predict_classification(input_df)
    
    if result==1:
        st.success('Eligible with high risk')
    elif result==2:
        st.success('Eligible')

    elif result==0:
        st.error('not eligible')
    
    print(result)

    print(employment_type)
    print(emi_scenario)
    print(existing_loans)
    print(education)

        
        # You can now pass these variables to your ML model's .predict() function
