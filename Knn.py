from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('การจำแนกข้อมูลด้วยเทคนิค Machine Learning')
st.image("./img/cat.jpg")
col1, col2, col3 = st.columns(3)