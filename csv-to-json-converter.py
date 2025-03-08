import streamlit as st
import pandas as pd
import json
import pyperclip

# Streamlit page configuration
st.set_page_config(page_title="CSV to JSON Converter", page_icon=":guardsman:", layout="wide")

# Title of the app
st.title("CSV to JSON Converter")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Remove columns with "Unnamed" in the name (typically empty or missing columns)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Remove completely empty columns
    df = df.dropna(axis=1, how='all')

    # Display the cleaned DataFrame to the user
    st.write("CSV Content Preview:")
    st.dataframe(df)

    # Convert the cleaned DataFrame to JSON (entire file in one go)
    json_data = df.to_json(orient='records', lines=False)
    
    # Load json data into a Python object
    parsed_json = json.loads(json_data)

    # Convert the parsed JSON back into a formatted string (single block of JSON)
    formatted_json = json.dumps(parsed_json, indent=4)

    # Display the entire JSON content in a scrollable text area (for easy copy-pasting)
    st.write("Converted JSON Output (Formatted):")
    json_text_area = st.text_area("Your JSON", formatted_json, height=300)

    # Add a Copy Button to copy the JSON
    if st.button("Copy JSON"):
        pyperclip.copy(formatted_json)
        st.success("JSON copied to clipboard!")

    # Provide a download button for the JSON file
    json_filename = uploaded_file.name.replace(".csv", ".json")
    st.download_button(
        label="Download JSON",
        data=formatted_json,  # JSON formatted string for download
        file_name=json_filename,
        mime="application/json"
    )

else:
    st.info("Please upload a CSV file to get started.")
