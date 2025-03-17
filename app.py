import streamlit as st
import pickle
import pandas as pd

# Streamlit app title
st.title('Random Forest Model Deployment')

# Load the saved model using pickle
try:
    with open('random_forest_model.pkl', 'rb') as file:
        model = pickle.load(file)
    st.success('Model loaded successfully!')
except Exception as e:
    st.error(f'Error loading model: {e}')

# Input fields for features
st.write("### Enter Values")
cea = st.number_input('CEA Value', value=0)  # Default value from your dataset
mthfr = st.number_input('MTHFR Value', value=0)  # Default value from your dataset

# Predict button
if st.button('Predict Tumor Value'):
    try:
        # Create a DataFrame with the input data
        input_data = pd.DataFrame({'cea': [cea], 'mthfr': [mthfr]})
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display the prediction
        st.write(f'**Predicted Tumor Value:** {prediction[0]:.2f}')
    except Exception as e:
        st.error(f'Error making prediction: {e}')
