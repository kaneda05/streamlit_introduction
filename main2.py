import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('Interactive Widgets')

# インタラクティブなウィジェット
## checkbox
if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Humster', use_column_width=100)

#指定した値が表示される
option = st.selectbox(
    'あなたが好きな数字を教えて下さい. ',
    list(range(1,11)),
)

'あなたの好きな数字は、 ', option, 'です'

#テキストボックス
option2 = st.text_input('あなたの趣味は何ですか？')
'あなたの趣味は、',option2, 'です'

#スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション:', condition

# インタラクティブ　＝　動的な値の変化に応じて表示が変更されるものの仕組み