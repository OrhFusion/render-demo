import warnings 
warnings.filterwarnings('ignore')

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingRegressor, RandomForestClassifier, GradientBoostingClassifier

from sklearn.metrics import classification_report, precision_score, confusion_matrix
import mlflow
import mlflow.sklearn

import pickle
import joblib

path = '/Volumes/Macbook Drive/Dataset/diabetes_prediction_dataset.csv'
df = pd.read_csv(path)
df.head(4)

mlflow.set_experiment('Diabetesj Predication')

gender_encode = LabelEncoder()
smoking_history_encode = LabelEncoder()
df['gender'] = gender_encode.fit_transform(df['gender'])
df['smoking_history'] = smoking_history_encode.fit_transform(df['smoking_history'])

X = df.iloc[:, :-1]
y = df.iloc[:,-1]

X_train , X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model with mlflow

with mlflow.start_run():
    model = RandomForestClassifier(
    max_depth=None,
    min_samples_split=4,
    min_samples_leaf=3,)
    
    model.fit(X_train, y_train)

mlflow.end_run(status="FINISHED")

joblib.dump(gender_encode,'gender_encode')
joblib.dump(smoking_history_encode,'smoking_history_encode')
joblib.dump(model, 'model.pkl')


