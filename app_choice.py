import streamlit as st
import numpy as np
import joblib
import pandas as pd




def choice_app() :
    st.subheader('추천장르 찾기')

    netfl = joblib.load('./model/netfl.pkl')
    type = st.radio('Choice', ['영화','다큐멘터리'])
    if type == '영화' :
        type = 0
    else :
        type = 1

    runtime = st.slider('상영 시간', 30, 60, (30, 60), step=1)
    imdb_score = st.slider('종합 점수', 5.0, 8.0, (5.0, 8.0), step=0.1)
    imdb_votes = st.slider('시청자 추천', 0, 100000, (0, 100000), step=1000)

    runtime_start, runtime_end = runtime
    imdb_score_start, imdb_score_end = imdb_score
    imdb_votes_start, imdb_votes_end = imdb_votes

    if st.button('추천 장르') :
        new_data = np.array([type, runtime_start, runtime_end, imdb_score_start, imdb_score_end, imdb_votes_start, imdb_votes_end])
        print(new_data)
        new_data = new_data.reshape(1, -1)
        y_pred = netfl.predict(new_data)
        st.text( y_pred )
        price = y_pred[0]

        if price > 5 :
            st.text('이 장르를 추천합니다.')
        else:
            st.text('죄송합니다. 현재 추천 장르가 없습니다.')