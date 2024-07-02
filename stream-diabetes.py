import pickle
import streamlit as st

#untuk membaca model
diabetes_model = pickle.load(open('diabetes_model_.sav', 'rb'))

#judul web
st.title('Perediksi Diabetes')

#Pembagian kolom
col1, col2 = st.columns(2)

with col1 :
    pregnancies = st.text_input ('Input Nilai Pregnancies')

with col2:
    glucose = st.text_input ('Input Nilai Glucose')

with col1:
    bloodpressure = st.text_input ('Input Nilai Blood Pressure')

with col2:
    skinthickness = st.text_input ('Input Nilai Skinthickness')

with col1:
    insulin = st.text_input ('Input Nilai Insulin')

with col2:
    bmi = st.text_input ('Input Nilai BMI')

with col1:
    DiabetesPedigreeFunction = st.text_input ('Input Nilai Diabetes Pedigree Function')
 
with col2:
    age = st.text_input ('Input Nilai AGE')
 
 #code untuk predikisi
diab_diagnosa = ''
 
 #tombol prediksi
if st.button('Test Prediksi Diabetes') :
    diab_prediction = diabetes_model.predict([[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, Diabetespedigreefungtion, age]])
    
    if(diab_prediction[0] == 1) :
        diab_diagnosis = 'Pasien Terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien Terkena Diabetes'
        
    st.success(diab_diagnosis)