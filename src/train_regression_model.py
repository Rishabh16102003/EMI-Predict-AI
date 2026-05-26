import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score ,mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
import xgboost as xgb
from feature_engineering import feature_encoder,feature_select_regression
import pickle
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

data=pd.read_csv('/data/emi_cleaned.csv')

encoded_data=feature_encoder(data)
selected_features=feature_select_regression(encoded_data)

X=selected_features.drop(columns=['max_monthly_emi'])
y=selected_features['max_monthly_emi']

st = StandardScaler()
X_scaled=st.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X_scaled, y, test_size=0.2,
                                                random_state=42)
#training   logistic regression                                                   
def train_logistic_regression():
    log_reg=LogisticRegression()
    log_reg.fit(X_train,y_train)
    y_pred=log_reg.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    return log_reg,rmse

#training xgboost
def train_xgboost_r(X_train,X_test,y_train,y_test):
    xgb_regressor = xgb.XGBRegressor(tree_method='hist',
                                  device='cpu',
                                #   reg_lamda=0.1,
                                 reg_alpha=0.15,
                                 n_estimators=150,
                                 min_child_weight=11,
                                 max_depth=9,
                                 learning_rate=0.1)
    xgb_regressor.fit(X_train,y_train)
    y_pred=xgb_regressor.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    return xgb_regressor,rmse 

#training random forest

def train_random_forest_r(X_train,X_test,y_train,y_test):
    rf = RandomForestRegressor(
    n_estimators=150,      # number of trees
    max_depth=9,        # depth of trees
    min_samples_split=3,
    min_samples_leaf=5,
    random_state=42,
    n_jobs=-1              # use all CPU cores
    )
    rf.fit(X_train,y_train)
    y_pred=rf.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    return rf,rmse

#training random_forest

rf_model,rf_rmse=train_random_forest_r(X_train,X_test,y_train,y_test)
xgb_model,xgb_rmse=train_xgboost_r(X_train,X_test,y_train,y_test)

if rf_rmse>xgb_rmse:
    pipline=Pipeline([
        ('reg_scaler',StandardScaler()),
        ('reg_model',rf_model)
    ])
    pipline.fit(X,y)
    pickle.dump(pipline,open('reg_model.pkl','wb'))

else:
    pipline=Pipeline([
        ('reg_scaler',StandardScaler()),
        ('reg_model',xgb_model)
    ])
    pipline.fit(X,y)
    pickle.dump(pipline,open('reg_model.pkl','wb'))