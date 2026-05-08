# FastAPI + Streamlit Student Predictor

## Overview

This project is a simple machine learning style application using:

- FastAPI for backend
- Streamlit for frontend
- Python for logic

The application predicts whether a student will pass or fail based on study hours.

---

## Technologies Used

- Python
- FastAPI
- Streamlit
- Requests
- Uvicorn

---

## Project Structure

project/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── .gitignore
└── README.md

---

## Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload