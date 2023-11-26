import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from app_home import home_app




def main():
    st.title('Netflix 추천영화')

    menu = ['Home','Choice','Data']

    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == menu[0] :
        home_app()
    elif choice == menu[1] :
        pass
    elif choice == menu[2] :
        pass

if __name__=='__main__' :
    main()