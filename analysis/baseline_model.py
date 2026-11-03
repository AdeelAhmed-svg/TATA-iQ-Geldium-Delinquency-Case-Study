"""Baseline delinquency model from the Tata iQ / Forage simulation (Task 2).

The dataset belongs to Forage / Tata iQ and is NOT included in this repository.
If you have access through the simulation, pass your local copy:

    python analysis/baseline_model.py path/to/Delinquency_prediction_dataset.csv

Outputs cross-validated metrics to the console only.
"""
import sys
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import roc_auc_score, recall_score, precision_score

path = sys.argv[1]
df = pd.read_excel(path) if path.endswith(".xlsx") else pd.read_csv(path)

# Clean inconsistent labels (EMP / employed / Employed -> employed)
df["Employment_Status"] = df["Employment_Status"].str.lower().replace({"emp": "employed"})

# Count late / missed months from the six-month payment history
months = [f"Month_{i}" for i in range(1, 7)]
df["late_n"] = (df[months] == "Late").sum(axis=1)
df["missed_n"] = (df[months] == "Missed").sum(axis=1)

num = ["Income", "Credit_Score", "Credit_Utilization", "Missed_Payments", "Loan_Balance",
       "Debt_to_Income_Ratio", "Account_Tenure", "late_n", "missed_n"]
cat = ["Employment_Status", "Credit_Card_Type"]  # Age and Location kept OUT of the model
X, y = df[num + cat], df["Delinquent_Account"]

prep = ColumnTransformer([
    ("num", Pipeline([("impute", SimpleImputer(strategy="median")),
                      ("scale", StandardScaler())]), num),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])
model = Pipeline([("prep", prep),
                  ("clf", LogisticRegression(class_weight="balanced", max_iter=1000))])

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
score = cross_val_predict(model, X, y, cv=cv, method="predict_proba")[:, 1]
flag = (score >= 0.5).astype(int)

print(f"Rows: {len(df)}  delinquent: {int(y.sum())} ({y.mean():.1%})")
print(f"Trivial 'nobody delinquent' accuracy: {1 - y.mean():.1%}")
print(f"AUC: {roc_auc_score(y, score):.2f}")
print(f"Recall: {recall_score(y, flag):.0%}  Precision: {precision_score(y, flag):.0%}")
print(f"Flagged: {int(flag.sum())}, true delinquent among flagged: {int(((flag==1)&(y==1)).sum())}")
