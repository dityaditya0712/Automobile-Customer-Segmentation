import streamlit as st
import streamlit.components.v1 as stc
import eda_app
import ml_app

html_temp = """
            <div style="">
                <h1> Automobile Customer Segmentation App</h1>
            </div>
            """

desc_temp = """
                ### Automobile Customer Segmentation App
                This app is used to predict customer segmentation

                ### App Content
                - Exploratory Data Analysis
                - Machine Learning Section 
            """

def main():
    stc.html(html_temp)

    menu = ["Home", "EDA", "ML Section"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "EDA":
       eda_app.perform_eda()
    elif choice == "ML Section":
        ml_app.show_predict_page()

if __name__ == '__main__':
    main()