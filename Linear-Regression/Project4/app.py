import streamlit as st
import numpy as np
import pandas as pd
import pickle



model=pickle.load(open('model.pkl','rb'))
data = pd.read_csv('data//carprices.csv')
st.title("Car Price Prediction")
st.image("data//car.jpg", width=600)


nav = st.sidebar.radio("Navigation",["Aim","Prediction"])      

if nav == 'Aim':
    st.markdown(""" #### Aim of the Project """)
    st.markdown(
        """ 1) Predict price of a mercedes benz that is 4 yr old with mileage 45000
2) Predict price of a BMW X5 that is 7 yr old with mileage 86000
3) Tell me the score (accuracy) of your model. (Hint: use LinearRegression().score()) """)
    
    if st.checkbox("Show Table"):
        st.table(data)

def predict_forest(experience,testscore,interviewscore):
    input=np.array([[experience,testscore,interviewscore]]).astype(np.float64)
    prediction=model.predict(input)
    pred='{0:.{1}f}'.format(prediction[0], 2)
    return float(pred)

if nav == 'Prediction':
    
    st.header('Know Your Car Price')
    experience = st.text_input("Model")
    testscore = st.text_input("Miles")
    interviewscore = st.text_input("Age")



    if st.button("Predict"):
        output=predict_forest(experience,testscore,interviewscore)
        st.success('Your Predicted Salary is  {}'.format(output))