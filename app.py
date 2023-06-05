import os
import streamlit as st
import pandas as pd

st.title("తాళపత్ర నిధి - మైథిలీ వెంకటేశ్వరరావు")
st.sidebar.title("Topics")

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def browse_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    for file_name in files:
        if file_name.endswith(".txt") and file_name != "requirements.txt":
            file_path = os.path.join(folder_path, file_name)
            button_label = os.path.splitext(file_name)[0]
            if st.sidebar.button(button_label):
                content = read_file(file_path)
                st.text_area("File Content", value=content, height=300)
                
# Get the current folder path
current_folder = os.getcwd()




st.sidebar.divider()
browse_files_in_folder(current_folder)

def browse_files_in_folderCSV(folder_path):
    files = os.listdir(folder_path)
    for file_name in files:
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            button_label = os.path.splitext(file_name)[0]
            if st.sidebar.button(button_label):
                df = read_csv(file_path)
                st.dataframe(df)

# Get the current folder path
# current_folder = os.getcwd()

# Display the file browsing section using Streamlit
# st.title("Browse CSV Files")
browse_files_in_folderCSV(current_folder)
