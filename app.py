import streamlit as st
import json
from model import probe_model_5l_profit

# Page 1: Upload Data File
def upload_data():
    st.title("Upload Financial Data File")
    
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")
    
    if uploaded_file is not None:
        if st.button("Submit"):
            data = json.load(uploaded_file)
            st.session_state['financial_data'] = data
            st.success("File uploaded successfully!")
        else:
            st.warning("Please click the Submit button after uploading.")

# Page 2: Display Results
def display_results():
    st.title("Financial Analysis Results")
    
    if 'financial_data' in st.session_state:
        data = st.session_state['financial_data']
        results = probe_model_5l_profit(data["data"])
        
        st.json(results)  # Display the results as JSON
    
    else:
        st.warning("Upload a data file on the Upload Data page.")

# Main Streamlit App
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page:", ["Upload Data", "View Results"])
    
    if page == "Upload Data":
        upload_data()
    elif page == "View Results":
        display_results()

if __name__ == "__main__":
    main()
