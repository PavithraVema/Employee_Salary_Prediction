import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib
import os

df = pd.read_csv("data/employeedata.csv")

# Label encoding
le_education = LabelEncoder()
le_role = LabelEncoder()
le_location = LabelEncoder()

df["education_encoded"] = le_education.fit_transform(df["education"])
df["role_encoded"] = le_role.fit_transform(df["role"])
df["location_encoded"] = le_location.fit_transform(df["location"])

X = df[["experience", "age", "education_encoded", "role_encoded", "location_encoded"]]
y = df["salary"]

model = LinearRegression()
model.fit(X, y)

# Save model and encoders
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/salary_model.pkl")
joblib.dump(le_education, "model/le_education.pkl")
joblib.dump(le_role, "model/le_role.pkl")
joblib.dump(le_location, "model/le_location.pkl")
