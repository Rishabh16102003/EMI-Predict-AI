import pickle
import numpy as np
import pandas as pd

def load_model(path):
    with open(path, "rb") as f:
        return pickle.load(f)

# Load once (efficient)
reg_model = load_model("pipelines/reg_model.pkl")
clf_model = load_model("pipelines/class_model.pkl")

def predict_regression(df: pd.DataFrame):
    return reg_model.predict(df)[0]


def predict_classification(df: pd.DataFrame):
    return clf_model.predict(df)[0]