import streamlit as st
import numpy as np
import pandas as pd




import streamlit as st
import pandas as pd

def choice_app():
    st.subheader('추천장르 찾기')

    netfl = pd.read_csv('./data/imdb_movies_shows.csv')

    # 컬럼 이름을 소문자로 변환
    netfl.columns = netfl.columns.str.lower()

    # 선택 옵션
    type_option = st.radio('Choice', ['영화', '다큐멘터리'])
    runtime_option = st.slider('상영 시간', min_value=0, max_value=300, step=1, value=(0, 300))
    imdb_score_option = st.slider('종합 점수', min_value=0.0, max_value=10.0, step=0.1, value=(0.0, 10.0))
    imdb_votes_option = st.slider('시청자 추천', min_value=0, max_value=1000000, step=1000, value=(0, 1000000))

    # 조건에 맞는 데이터 필터링
    filtered_data = netfl[
        (netfl['type'].str.lower() == type_option) &
        (netfl['runtime'] >= runtime_option[0]) & (netfl['runtime'] <= runtime_option[1]) &
        (netfl['imdb_score'] >= imdb_score_option[0]) & (netfl['imdb_score'] <= imdb_score_option[1]) &
        (netfl['imdb_votes'] >= imdb_votes_option[0]) & (netfl['imdb_votes'] <= imdb_votes_option[1])
    ]

    # 결과 표시
    if not filtered_data.empty:
        st.write('추천 영화 목록:')
        st.dataframe(filtered_data)
    else:
        st.write('추천 영화가 없습니다.')
