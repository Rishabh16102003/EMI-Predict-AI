import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from feature_engineering import feature_encoder,feature_select_classification
from sklearn.pipeline import Pipeline
import pickle

data=pd.read_csv('../data/emi_cleaned.csv')

encoded_data=feature_encoder(data)

selected_features=feature_select_classification(encoded_data)

X=selected_features.drop(columns=['emi_eligibility'])
y=selected_features['emi_eligibility']

st = StandardScaler()
X_scaled=st.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X_scaled, y, test_size=0.2,
                                                     random_state=42)

def train_xgboost_c(X_train,X_test,y_train,y_test):
    xgb = XGBClassifier(
    n_estimators=100,
    learning_rate=0.05,
    max_depth=9,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1,
    eval_metric='logloss'
    )
    xgb.fit(X_train,y_train)
    y_pred=xgb.predict(X_test)
    accuracy=accuracy_score(y_test,y_pred)
    return xgb,accuracy

def train_random_forest_c(X_train,X_test,y_train,y_test):
    rf = RandomForestClassifier(
    random_state=42,
    n_jobs=-1,
    min_samples_split=7,
    min_samples_leaf=5,
    max_depth=9,
    max_samples=0.7,
    n_estimators=150
    )
     # Train
    rf.fit(X_train, y_train)

    # Predict
    y_pred = rf.predict(X_test)
    accuracy=accuracy_score(y_test,y_pred)
    return rf,accuracy

rf_model,rf_accuracy=train_random_forest_c(X_train,X_test,y_train,y_test)
xgb_model,xgb_accuracy=train_xgboost_c(X_train,X_test,y_train,y_test)

if rf_accuracy>xgb_accuracy:
    pipline=Pipeline([
        ('class_scaler',StandardScaler()),
        ('class_model',rf_model)
    ])
    pipline.fit(X,y)
    pickle.dump(pipline,open('class_model.pkl','wb'))

else:
    pipline=Pipeline([
        ('class_scaler',StandardScaler()),
        ('class_model',xgb_model)
    ])
    pipline.fit(X,y)
    pickle.dump(pipline,open('class_model.pkl','wb'))
    

