import streamlit as st
import numpy as np
import joblib
import os

# Attribute Information
attribute_info = """
                - Gender: Male and Female
                - Age: 18-89
                - Ever Married: 0. No, 1. Yes
                - Graduated: 0. No, 1. Yes
                - Profession: Artist, Doctor, Engineer, Entertainment, Executive, Healthcare, Homemaker, Lawyer, Marketing, Unknown
                - Work Experience: 0-14
                - Spending Score: Low, Average, and High
                - Family Size: 1-9
                - Var_1: Cat_1, Cat_2, ..., Cat_7, and Unknown
                - Segmentation: A, B, C, and D
                 """

# Feature Dictionaries
gender_dict = {"Male": 1, "Female": 0}
married_dict = {"No": 0, "Yes": 1}
graduated_dict = {"No": 0, "Yes": 1}
profession_dict = {
    "Artist": 0, "Doctor": 1, "Engineer": 2, "Entertainment": 3, "Executive": 4,
    "Healthcare": 5, "Homemaker": 6, "Lawyer": 7, "Marketing": 8, "Unknown": 9
}
spending_score_dict = {"Low": 2, "Average": 0, "High": 1}
var_1_dict = {"Cat_1": 0, "Cat_2": 1, "Cat_3": 2, "Cat_4": 3, "Cat_5": 4, "Cat_6": 5, "Cat_7": 6, "Unknown": 7}
segmentation_dict = {"A": 0, "B": 1, "C": 2, "D": 3}

# Load the model from the pickle file
model_path = "gbm_model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file not found!")

def preprocess_input(data):
    # Convert input data to the format your model expects
    input_data = [
        gender_dict[data['gender']],
        int(data['age']),
        married_dict[data['ever_married']],
        graduated_dict[data['graduated']],
        profession_dict[data['profession']],
        int(data['work_experience']),
        spending_score_dict[data['spending_score']],
        int(data['family_size']),
        var_1_dict[data['var_1']]
    ]
    input_array = np.array(input_data).reshape(1, -1)
    return input_array

def show_predict_page():
    st.title("Customer Segmentation Prediction")

    st.write("Enter customer details to predict the segment.")
    
    st.write(attribute_info)

    gender = st.selectbox("Gender", list(gender_dict.keys()))
    age = st.slider("Age", 18, 89, 30)
    ever_married = st.selectbox("Ever Married", list(married_dict.keys()))
    graduated = st.selectbox("Graduated", list(graduated_dict.keys()))
    profession = st.selectbox("Profession", list(profession_dict.keys()))
    work_experience = st.slider("Work Experience", 0, 14, 5)
    spending_score = st.selectbox("Spending Score", list(spending_score_dict.keys()))
    family_size = st.slider("Family Size", 1, 9, 4)
    var_1 = st.selectbox("Var_1", list(var_1_dict.keys()))

    if st.button("Predict"):
        data = {
            'gender': gender,
            'age': age,
            'ever_married': ever_married,
            'graduated': graduated,
            'profession': profession,
            'work_experience': work_experience,
            'spending_score': spending_score,
            'family_size': family_size,
            'var_1': var_1
        }
        input_data = preprocess_input(data)
        prediction = model.predict(input_data)
        prediction_segment = [key for key, value in segmentation_dict.items() if value == prediction[0]][0]
        st.success(f"The predicted customer segment is: {prediction_segment}")