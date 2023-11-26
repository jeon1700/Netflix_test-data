import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




def data_app():
    st.header('*Netflix Data 분석*')

    st.subheader('총 데이터 프레임')
    df = pd.read_csv('./data/imdb_movies_shows.csv')
    st.dataframe(df)

    st.text('평균데이터 통계')
    if st.checkbox('통계 보기') :
        st.dataframe(df.describe())
    else :
        st.text('')
    

    selected_column = st.selectbox('데이터 확인', df.select_dtypes(include=['number']).columns)
    st.text(selected_column + ' 데이터 최소값')
    st.dataframe(df.loc[df[selected_column] == df[selected_column].min(), :])
    st.text(selected_column + ' 데이터 최대값')
    st.dataframe(df.loc[df[selected_column] == df[selected_column].max(), :])


    st.text(selected_column + ' 데이터의 차트')
    fig1 = plt.figure()
    df[selected_column].hist(bins = 100)
    st.pyplot(fig1)