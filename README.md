# 🏠 Buy vs Rent Prediction App

This project is an end-to-end Machine Learning application that predicts whether a user should **buy or rent a house** based on financial inputs.

It uses:

* **Machine Learning (Logistic Regression)**
* **FastAPI** for backend API
* **Streamlit** for frontend UI
* **Docker** for deployment

---

## 🚀 Features

* Predict Buy 🏡 vs Rent 🏠 decision
* Interactive UI using Streamlit
* REST API using FastAPI
* Dockerized for easy deployment
* Model saved using `.pkl` (no retraining needed)

---

## 📊 Dataset Features

The model uses the following inputs:

* Monthly Salary
* Age
* House Price
* Down Payment
* Loan Amount
* Running EMI

---

## 🧠 Model

* Algorithm: Logistic Regression
* Library: scikit-learn
* Model saved as: `model.pkl`

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Streamlit
* scikit-learn
* Docker

---

## 📁 Project Structure

```
project/
│
├── app.py                # FastAPI backend
├── streamlit_app.py      # Streamlit frontend
├── train_model.py        # Model training script
├── model.pkl             # Saved model
├── columns.pkl           # Feature order
├── requirements.txt
├── Dockerfile
├── start.sh
├── buy_vs_rent_data_project.csv
```

---

## ⚙️ Installation (Local)

### 1. Clone repository

```
git clone <your-repo-link>
cd project
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run FastAPI

```
uvicorn app:app --reload
```

---

### 4. Run Streamlit

```
streamlit run streamlit_app.py
```

---

## 🐳 Docker Setup

### Build Image

```
docker build -t buy_rent .
```

---

### Run Container

```
docker run -p 8000:8000 -p 8501:8501 buy_rent
```

---

## 🌐 Access

* FastAPI → http://localhost:8000
* Swagger Docs → http://localhost:8000/docs
* Streamlit UI → http://localhost:8501

---

## 🔥 API Example

### POST /predict

```
{
  "monthly_salary": 50000,
  "age": 30,
  "house_price": 5000000,
  "down_payment": 500000,
  "loan_amount": 4500000,
  "running_emi": 20000
}
```

---

## 🎯 Future Improvements

* Add model evaluation metrics (F1, Accuracy)
* Add data preprocessing pipeline
* Deploy on AWS EC2 with domain
* Add CI/CD pipeline

---

## 👨‍💻 Author

Avadhesh

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
