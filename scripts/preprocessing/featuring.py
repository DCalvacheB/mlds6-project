# -*- coding: utf-8 -*-
"""Processed Data.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1_9cnzcUqr22w5wzQVkC1IGvXrdv0WCzQ
"""

import pandas as pd
import datetime as dt
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer, MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

data = pd.read_csv("processtrainbank.csv", sep="\,")

categorical = ["Job", "Marital.Status", 'Education', 'Contact','Last.Contact.Month','Poutcome']
ordinal = ["Age",'Last.Contact.Day','Campaign','Previous', 'Pdays']
numeric = ["Balance..euros.", 'Last.Contact.Duration']
binary = ["Credit",'Housing.Loan','Personal.Loan']
    
transformer = ColumnTransformer(
        transformers=[
            ("categorical", OneHotEncoder(), categorical),
            ("ordinal", MinMaxScaler(), ordinal),
            ("counts", MinMaxScaler(), make_column_selector(pattern=r"Mnt|Num")),
            ("numeric", StandardScaler(), numeric),
            ("binary", FunctionTransformer(lambda x: x), binary)
            ]
        )
data.to_csv("featuretrainbank.csv",index=False)
