import streamlit as st
import pandas as pd
import numpy as np

st.title("hello gugu!!!")
st.header("or kaisa hai ")
st.subheader("this is the website --->>")
st.write("https://schedule.vridhamma.org/courses/sikhara")
st.markdown("ye hai website and portal 60 days pehle khul jata he")
st.caption("meri taraf se ALL THE BEST !!!")
st.image("bhangulal.jpg")
st.video("guguallthebest.mp4")

st.select_slider('how excited are you bhangu',['very excited','thoda sa','bilkul nhi'])
st.slider('mummi papa ko kitna yad karoge',-100,0)
st.text_area('mere liye kuch ache shabad')
st.success("bhangu ap ek ache bache ho very disciplined and dedicated")
st.sidebar.title("mai apke sath hu bhangu all the best")
st.sidebar.image("crazybish.jpg")
with st.chat_message("user"):
    st.write("all the best bhaiiii")
