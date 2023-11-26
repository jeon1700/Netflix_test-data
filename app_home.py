import streamlit as st

def home_app():
    st.subheader('*해당 사이트는 Netflix Movie & documentary를 추천합니다.*')
   
    img_url = 'https://cdn.eyesmag.com/content/uploads/posts/2021/12/10/Netflix-launches-website-Tudum-main-3402edc0-22ef-4394-804e-c4ce28015507.jpg'
   
    st.image(img_url)
   
    st.text('소비자의 취향에 맞춰 추천영화가 나옵니다.')
    st.info('데이터 출저 : https://www.kaggle.com/datasets/maso0dahmed/netflix-movies-and-shows/')
    