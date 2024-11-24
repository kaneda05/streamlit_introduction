import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('Interactive Widgets')

# インタラクティブなウィジェット
"""
## サイドバーの作成
```python
## checkbox
if st.sidebar.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Humster', use_column_width=100)


#st.sidebar
number = st.sidebar.selectbox(
    'あなたが好きな数字を教えて下さい. ',
    list(range(1,11)),
)
text = st.sidebar.text_input('あなたの趣味を教えて下さい')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'好きな数字:',number
'あなたの趣味:',text
'コンディション:', condition
```
"""
## checkbox
if st.sidebar.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Humster', use_column_width=100)


#st.sidebar
number = st.sidebar.selectbox(
    'あなたが好きな数字を教えて下さい. ',
    list(range(1,11)),
)
text = st.sidebar.text_input('あなたの趣味を教えて下さい')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'好きな数字:',number
'あなたの趣味:',text
'コンディション:', condition

"""
---
## 2カラムの作成
動画ではst.beta_columns(2)だったが、バージョン違いによっては、st.columns(2)で良さそう
```python

#st.columns()
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
"""

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


"""
---
## expander
動画ではst.beta_expander(2)だったが、バージョン違いによっては、st.expander(2)で良さそう
```python

#st.expander()
expander1 = st.expander('問い合わせ内容1')
expander1.write('問い合わせ内容1の回答')
expander2 = st.expander('問い合わせ内容2')
expander2.write('問い合わせ内容2の回答')
expander3 = st.expander('問い合わせ内容3')
expander3.write('問い合わせ内容3の回答')
"""

expander1 = st.expander('問い合わせ内容1')
expander1.write('問い合わせ内容1の回答')
expander2 = st.expander('問い合わせ内容2')
expander2.write('問い合わせ内容2の回答')
expander3 = st.expander('問い合わせ内容3')
expander3.write('問い合わせ内容3の回答')

"""
## progress bar の作成
```python
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
```
"""

st.write('progress bar の表示')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Dane'