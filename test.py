import streamlit as st
with st.form("financial_form"):
    employment_type = st.selectbox(
            "Employment Type",
            options=["Government", "Self-Employed",
                      'Private'],
            index=None,
            placeholder='select_option'
        )
    submitted = st.form_submit_button("Calculate Eligibility")

print(employment_type)
ls=[]
if employment_type=="Government":
    ls=[1,0,0]

print(ls)

