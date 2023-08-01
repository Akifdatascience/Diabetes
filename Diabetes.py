#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[7]:


import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
with open("reg.pkl", 'rb') as file:
    model = pickle.load(file)

def main():
    st.title('Diabetes Prediction App')
    st.write('Enter the following information to predict diabetes:')

    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=17, value=1)
    glucose = st.number_input('Glucose', min_value=0, max_value=200, value=100)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=122, value=70)
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=99, value=20)
    insulin = st.number_input('Insulin', min_value=0, max_value=846, value=79)
    bmi = st.number_input('BMI', min_value=0.0, max_value=67.1, value=30.0)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.078, max_value=2.42, value=0.3725)
    age = st.slider('Age', 21, 81, 30)

    data = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': diabetes_pedigree_function,
        'Age': age
    }

    features = pd.DataFrame([data])

    if st.button('Predict'):
        prediction = model.predict(features)
        if prediction[0] == 1:
            st.error('The person is predicted to be diabetic.')
        else:
            st.success('The person is predicted to be non-diabetic.')

if __name__ == '__main__':
    main()


# In[ ]:




