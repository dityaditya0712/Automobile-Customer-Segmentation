# Automobile Customer Segmentation

This project aims to predict customer segments for an automobile company using a machine learning model. The goal is to classify potential customers into four segments (A, B, C, D) based on demographic and behavioral data. The project utilizes Python, Streamlit, and scikit-learn to build and deploy the model.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Machine Learning Model](#machine-learning-model)
- [Deployment](#deployment)

## Overview

The automobile company plans to enter new markets with their existing products. They intend to use a customer segmentation strategy that has worked well in existing markets. This project helps to predict the appropriate customer segment for new potential customers.

## Dataset

The dataset used for this project is sourced from Kaggle and contains the following features:

- Gender
- Age
- Ever Married
- Graduated
- Profession
- Work Experience
- Spending Score
- Family Size
- Var_1
- Segmentation

## Project Structure
    Automobile-Customer-Segmentation/
    ├── app.py
    ├── eda_app.py
    ├── ml_app.py
    ├── model/
    │   └── gbm_model.pkl
    ├── Train.csv
    ├── Test.csv
    ├── requirements.txt
    └── README.md
- `app.py`: Main application file for navigation.
- `eda_app.py`: Script for exploratory data analysis.
- `ml_app.py`: Script for machine learning model prediction.
- `gbm_model`.pkl: Trained machine learning model.
- `Train.csv`: Dataset used for training
- `Test.csv`: Dataset used for testing.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## Exploratory Data Analysis
The EDA script (eda_app.py) includes the following analysis:

- Descriptive statistics of the dataset using data.describe().
- Pie charts and bar charts for categorical features:
    - Gender
    - Ever Married
    - Graduated
    - Profession
    - Spending Score
    - Var_1
    - Segmentation

- Box plots and histograms for numerical features:
    - Age
    - Work Experience
    - Family Size

- Analysis of the distribution of features across different customer segments using box plots.

## Machine Learning Model
The machine learning script (ml_app.py) includes:

- Loading the trained model from model/your_model.pkl.
- Preprocessing the input data.
- Making predictions based on user inputs.
- Displaying the predicted customer segment.

## Deployment
The application is deployed using Streamlit Cloud. You can access the deployed application https://automobile-customer-segmentation-egregium.streamlit.app