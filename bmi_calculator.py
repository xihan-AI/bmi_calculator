import streamlit as st

st.title("BMI Calculator")

name = st.text_input("Enter Your name: ",placeholder = "eg  Zehan")
weight = st.number_input("Enter your weight (in kgs)",value = None)
height_format = st.radio("Select your height format:",("feet","meter","cms"))

if height_format == "cms":
    height = st.number_input("Centimeter",value = None, placeholder = "eg  180 😏")
    if weight and height:
        bmi = weight / ((height*0.01) ** 2)

elif height_format == "feet":
    height = st.number_input("Feet",value = None, placeholder = "eg  5.11 😏")
    if weight and height:
        bmi = weight / ((height*0.3048) ** 2)

elif height_format == "meter":
    height = st.number_input("Meters",value = None, placeholder = "eg  1.8 😏")
    if weight and height:
        bmi = weight / (height ** 2)

if st.button("Calculate BMI") and weight and height:
    st.write(f"{name} Your BMI index in {bmi:.2f}")

    if bmi <= 18.5:
        st.info("Underweight")

    elif 18.5 < bmi <= 24.9:
        st.success("Normal Weight")

    elif 24.9 < bmi <= 29.9:
        st.warning("Overweight")

    elif 29.9 < bmi <= 34.9:
        st.error("Obese")


