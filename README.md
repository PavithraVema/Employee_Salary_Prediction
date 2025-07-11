# Employee_Salary_Prediction
<img width="1600" height="836" alt="{D5D4C1C4-2F1A-4361-9F8A-156B4CC9D0E8}" src="https://github.com/user-attachments/assets/9bbb90d9-d4b5-48f2-95e5-a43ca98cb9d8" />




# 🧑‍💼 Employee Salary Prediction System

A machine learning-based web application that predicts an employee's salary based on multiple features such as experience, education level, job role, location, and age.

---

## 🎯 Project Objective

To build an intelligent system that helps HR departments and job seekers estimate fair salary expectations using historical data and regression techniques.

---

## 📊 Features Used for Prediction

- Experience (years)
- Age
- Education (Bachelor, Master, PhD)
- Role (e.g., Data Analyst, Backend Developer)
- Location (Tier 1 / Tier 2 city)

---

## 🤖 Machine Learning Model

The following regression models can be used:

### ✅ Linear Regression (default)
- Simple, fast, interpretable
- May predict negative values (clamped to ₹0 in the app)

### 🟡 Random Forest Regressor (optional upgrade)
- Non-linear model, better accuracy
- Handles feature interaction better than Linear Regression

📁 Model and encoders are saved as `.pkl` files using `joblib`.

---

## 🧱 Project Structure

employee_salary_prediction/
│
├── data/
│ └── employeedata.csv # Main dataset
│
├── model/
│ ├── salary_model.pkl # Trained ML model
│ ├── le_education.pkl # Label encoder for education
│ ├── le_role.pkl # Label encoder for role
│ └── le_location.pkl # Label encoder for location
│
├── static/
│ └── style.css # CSS styling
│
├── templates/
│ └── index.html # Web form UI
│
├── notebooks/
│ ├── salary_prediction.ipynb # Model training notebook
│ └── adddata.ipynb # Add new data to CSV
│
├── app.py # Flask web application
├── train_model.py # Script to train and save model
├── requirements.txt # Python dependencies
└── README.md



**2. Install Dependencies**
bash
Copy
Edit
pip install -r requirements.txt





**3. Train the Model**
bash
Copy
Edit
python train_model.py



**4. Start the Flask App**
bash
Copy
Edit
python app.py
Then open your browser at:
🌐 http://127.0.0.1:5000


**Web App Features**
Interactive HTML form
CSS-styled modern UI
Predicts salary in ₹ INR
Prevents negative salary values
Easy model retraining with new data

**🛠 Tools & Technologies**
Python
Pandas
scikit-learn
Flask
HTML5 / CSS3
Jupyter Notebooks
