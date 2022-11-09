import streamlit as st
import preprocessor
import helper

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('notification')
    user_list.sort()
    user_list.insert(0, 'Overall')
    selected_user = st.sidebar.selectbox('Show analysis wrt', user_list)

    if st.sidebar.button('Show analysis'):
        gaali_df = helper.fetch_gaali(selected_user, df)
        st.dataframe(gaali_df)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header('Total Messages')
            st.title(helper.fetch_no_messages(selected_user, df))
        with col2:
            print(helper.fetch_gaali(selected_user, df))
            st.header('Number of Gaalis')
            st.title(gaali_df['count'].sum())