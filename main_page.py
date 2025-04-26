import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import pandas as pd
 
 
 
st.set_page_config(page_title="ANTEA EHS", layout="wide")

st.sidebar.title("Clients")


st.title("File Analyzing")

col1, col2 = st.columns(2)


country = st.sidebar.selectbox("Select Country", ['USA', 'Latam', 'Europe'])
template = st.sidebar.selectbox("Select Template", ['Template 1', 'Template 2', 'Template 3'])
owner = st.sidebar.selectbox("Select User/Owner", ['User 1', 'User 2', 'User 3'])
client = st.sidebar.selectbox("Select Client", ['Client 1', 'Client 2', 'Client 3'])
juristication = st.sidebar.selectbox("Select Juristication", ['J1', 'J2', 'J3'])




data = {
    'Id' : ['1','2','3'],
    'Registry Name' : ['Registry 1', 'Registry 2', 'Registry 3'],
    'Approval Status': ['Approved', 'Reproved', 'Reproved'],
    'Comments': ['Comment 1', 'Comment 2', 'Comment 3'],
    'Owner': ['Owner 1', 'Owner 2', 'Owner 3'] 
}
df = pd.DataFrame(data)

with col1:
    search_bar = st.text_input('Search by ID:')
    if search_bar:
        df_filter = df[df['Id'].str.contains(search_bar, case=False, na=False)]
    else:
        df_filter = df
        
    st.dataframe(df_filter)
    
    pass
with col2:
    st.write("Upload your file (.csv or .xlsx)")

    file = st.file_uploader("Choose your file", type=['csv', 'xlsx'])

    if file:
        
        try:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)
                
            st.success("successful loaded")
            st.dataframe(df)
        except Exception as e:
            st.error(f"erro {e}")
    else:
        st.info("none file")
        


button = st.button("submit data")

