import streamlit as st 
import pickle
import pandas as pd 

st.title("Lung Cancer Classification Using miRNA Expressions")
st.info("Please fill out the sections below")
st.sidebar.header("Diagnosis")

# Load the trained model
with open("LUAD1.sav", "rb") as file:
    clf = pickle.load(file)

# Input fields
hsa_miR_96_5p = st.text_input('Insert expression for hsa-miR-96-5p')
hsa_miR_135b_3p = st.text_input('Insert expression for hsa-miR-135b-3p')
hsa_miR_21_5p = st.text_input('Insert expression for hsa-miR-21-5p')
hsa_miR_135b_5p = st.text_input('Insert expression for hsa-miR-135b-5p')
hsa_miR_769_39 = st.text_input('Insert expression for hsa-miR-769-3p')
hsa_miR_21_3p = st.text_input('Insert expression for hsa-miR-21-3p')
hsa_miR_182_5p = st.text_input('Insert expression for hsa-miR-182-5p')
hsa_miR_1268a = st.text_input('Insert expression for hsa-miR-1268a')
hsa_miR_625_3p = st.text_input('Insert expression for hsa-miR-625-3p')
hsa_miR_200a_5p = st.text_input('Insert expression for hsa-miR-200a-5p')

# Create a DataFrame with user inputs
dataset = pd.DataFrame({
    'hsa-miR-96-5p': [hsa_miR_96_5p],
    'hsa-miR-135b-3p': [hsa_miR_135b_3p],
    'hsa-miR-21-5p': [hsa_miR_21_5p],
    'hsa-miR-135b-5p': [hsa_miR_135b_5p],
    'hsa-miR-769-39': [hsa_miR_769_39],
    'hsa-miR-21-3p': [hsa_miR_21_3p],
    'hsa-miR-182-5p': [hsa_miR_182_5p],
    'hsa-miR-1268a': [hsa_miR_1268a],
    'hsa-miR-625-3p': [hsa_miR_625_3p],
    'hsa-miR-200a-5p': [hsa_miR_200a_5p]
})

# Prediction button
confirm_button = st.sidebar.button('Confirm')
if confirm_button:
    result = clf.predict(dataset)
    st.write(result)
