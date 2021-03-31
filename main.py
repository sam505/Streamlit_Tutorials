import streamlit as st
import pandas as pd


def main():
    data = pd.read_csv("research-and-development-survey-2019-csv.csv")
    data_1 = pd.read_csv("greenhouse-gas-emissions-by-region-industry-and-household-year-ended-2018-csv.csv")
    st.dataframe(data)
    st.table(data.iloc[0:10])

    st.dataframe(data_1)
    st.table(data_1.iloc[0:10])
    st.line_chart(data_1[""])

    st.json({'foo': 'bar', 'fu': 'ba'})
    st.beta_container()
    st.beta_columns(4)
    col1, col2 = st.beta_columns(2)
    col1.subheader('Columnisation')
    st.beta_expander('Expander')
    with st.beta_expander('Expand'):
        st.write('Juicy deets')


    st.sidebar.write("# Noniot")
    a = st.sidebar.radio('R:', [1, 2])
    st.button('Hit me')
    st.checkbox('Check me out')
    st.radio('Radio', [1, 2, 3])
    st.selectbox('Select', [1, 2, 3])
    st.multiselect('Multiselect', [1, 2, 3])
    st.slider('Slide me', min_value=0, max_value=10)
    st.select_slider('Slide to select', options=[1, '2'])
    st.text_input('Enter some text')
    st.number_input('Enter a number')
    st.text_area('Area for textual entry')
    st.date_input('Date input')
    st.time_input('Time entry')
    st.file_uploader('File uploader')
    st.color_picker('Pick a color')


if __name__ == '__main__':
    main()
