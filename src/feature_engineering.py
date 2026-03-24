import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.preprocessing import StandardScaler


def feature_encoder(df):
    # gender_column ()
    gender_map={
        'M':'0',
        'F':'1',
    }
    df['gender']=df['gender'].replace(gender_map)
    df['gender']=df['gender'].astype(int)


    #marital_status column
    marital_status_map={
        'Single':'0',
        'Married':'1'
    }
    df['marital_status']=df['marital_status'].replace(marital_status_map)
    df['marital_status']=df['marital_status'].astype(int)

    #education column
    education_map={
        'Unknown':'0',
        'High School':'1',
        'Post Graduate':'3',
        'Professional':'4',
        'Graduate':'2',
    }
    df['education']=df['education'].replace(education_map)
    df['education']=df['education'].astype(int)

    # company_column
    company_map={
        'Small':'0',
        'Startup':'1',
        'Mid-size':'2',
        'Large Indian':'3',
        'MNC':'4'
    }
    df['company_type']=df['company_type'].replace(company_map)
    df['company_type']=df['company_type'].astype(int)

    #existing_loan column
    existing_loan_map={
        'No':'0',
        'Yes':'1'
    }
    df['existing_loans']=df['existing_loans'].replace(existing_loan_map)
    df['existing_loans']=df['existing_loans'].astype(int)

    # one_hot_encoding for ['house_type','employment_type','emi_scenario']
    cols_to_encode=['house_type','employment_type','emi_scenario']
    df=pd.get_dummies(df,columns=cols_to_encode,prefix=cols_to_encode,dtype=int)

    #emi eligibility column
    target_map={
        'Not_Eligible':'0',
        'High_Risk':'1',
        'Eligible':'2'
    }
    df['emi_eligibility']=df['emi_eligibility'].replace(target_map)
    df['emi_eligibility']=df['emi_eligibility'].astype(int)

    return df


def feature_select_classification(df):
    df['expense_salary_ratio']=(df['groceries_utilities']+df['college_fees']+
                                df['current_emi_amount']+df['school_fees']+
                                df['monthly_rent']+df['other_monthly_expenses']+
                                df['travel_expenses'])/df['monthly_salary']
    
    class_df=df[['education','credit_score','monthly_salary','bank_balance',
          'emergency_fund','requested_amount','requested_tenure',
          'employment_type_Government','employment_type_Private',
          'employment_type_Self-employed','emi_scenario_E-commerce Shopping EMI',
          'emi_scenario_Education EMI','emi_scenario_Home Appliances EMI',
          'emi_scenario_Personal Loan EMI','emi_scenario_Vehicle EMI',
          'expense_salary_ratio','emi_eligibility']]
    return class_df

def feature_select_regression(df):
    df['expense_salary_ratio']=(df['groceries_utilities']+df['college_fees']+
                                df['current_emi_amount']+df['school_fees']+
                                df['monthly_rent']+df['other_monthly_expenses']+
                                df['travel_expenses'])/df['monthly_salary']
      
    reg_df=df[['education','credit_score','monthly_salary',
                 'bank_balance','emergency_fund','existing_loans',
                 'expense_salary_ratio','max_monthly_emi']]
    
    return reg_df



