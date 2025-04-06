import streamlit as st

# Function to calculate and display BMI result with styling
def bmiCalculator(weight, height):
    BMI = weight / (height ** 2)  # BMI formula
    st.markdown(f"### Your BMI is: **{BMI:.2f}**")  # Display BMI in bold with size change

    # Categorize BMI result with colors and bold
    if BMI < 18.5:
        st.markdown('<p style="color:blue; font-size: 18px; font-weight: bold;">Underweight</p>', unsafe_allow_html=True)
    elif 18.5 <= BMI < 24.9:
        st.markdown('<p style="color:green; font-size: 18px; font-weight: bold;">Normal weight</p>', unsafe_allow_html=True)
    elif 25 <= BMI < 29.9:
        st.markdown('<p style="color:orange; font-size: 18px; font-weight: bold;">Overweight</p>', unsafe_allow_html=True)
    elif BMI >= 30:
        st.markdown('<p style="color:red; font-size: 18px; font-weight: bold;">Obese</p>', unsafe_allow_html=True)
    else:
        st.write("Invalid input.")

# Streamlit app UI
st.title("BMI CALCULATOR")

# User inputs with customized font size
weight = st.number_input("Enter your weight in (kilogram):", min_value=1, max_value=300)
height = st.number_input("Enter your height in (meters):", min_value=0.1, max_value=3.0)

# Calculate BMI when the button is pressed
if st.button("Get Body Mass Index"):
    if weight > 0 and height > 0:  # Ensure valid inputs
        bmiCalculator(weight, height)
    else:
        st.write("Please enter valid weight and height.")
