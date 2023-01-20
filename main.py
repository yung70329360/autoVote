import streamlit as st
import loreal
import time
from joblib import Parallel, delayed, cpu_count
st.image('image.png')
st.write('Click "Start" to generate votes')
t = st.empty()
col1, col2 = st.columns(2)
with col1:
    start = st.button('Start', key=1)


def loop(i):
    try:
        loreal.main()
        t.write(f'第{i}個票數已產生完成')
    except:
        tt2.write('發生錯誤, 重新嘗試')
        loop(i)

tt = st.empty()
tt2 = st.empty()

i = 0

if start:
    with col2:
            stop = st.button('Stop', key=2)
    while True:
        if stop:
            tt.write('正在停止')
            break
        i += 1
        loop(1)
    tt.write('已停止')
    




