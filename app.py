from flask import Flask, render_template, request


import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = joblib.load("model/salary_model.pkl")
le_education = joblib.load("model/le_education.pkl")
le_role = joblib.load("model/le_role.pkl")
le_location = joblib.load("model/le_location.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    experience = float(request.form["experience"])
    age = int(request.form["age"])
    education = request.form["education"]
    role = request.form["role"]
    location = request.form["location"]

    education_encoded = le_education.transform([education])[0]
    role_encoded = le_role.transform([role])[0]
    location_encoded = le_location.transform([location])[0]

    features = np.array([[experience, age, education_encoded, role_encoded, location_encoded]])
    prediction = model.predict(features)[0]
    prediction = max(0, prediction)  # ✅ prevent negative salary

    

    return render_template("index.html", prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)
