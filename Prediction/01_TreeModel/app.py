import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

st.markdown('# データ分析アプリ')
st.text('予測モデルを作成するウェブアプリケーション')