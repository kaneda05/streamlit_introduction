import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('Display Image')
"""
## 画像の表示
```python
img = Image.open('sample.jpg')
st.image(img, caption='Humster', use_column_width=100)
```
"""

img = Image.open('sample.jpg')
st.image(img, caption='Humster', use_column_width=100)

df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})


"""
---
## データの表示
```python
df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

st.write('DataFrame')
st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)

st.write('write')
st.write(df)

st.write('table')
st.table(df)
```
"""
st.write('DataFrame')
st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)

st.write('write')
st.write(df)

st.write('table')
st.table(df)


# マジックコマンドの作成
"""
---
## マジックコマンドの作成
# 章
## 節
### 項

```python
import streamlit
import numpy as np
import pandas as pd
```
"""


"""
---
## チャートの作成
### API reference Display charts参照

```python
df2 = pd.DataFrame(
    np.random.rand(10, 3),
    columns = ['a', 'b', 'c']
    )
st.line_chart(df2)
st.line_area(df2)
st.line_bar(df2)
```
"""

df2 = pd.DataFrame(
    np.random.rand(10, 3),
    columns = ['a', 'b', 'c']
    )
# 折れ線グラフ
st.write('折れ線グラフ（st.line_chart）')
st.line_chart(df2)

# エリアチャート
st.write('エリアチャート（st.area_chart）')
st.area_chart(df2)

# 棒グラフ
st.write('棒グラフ（st.bar_chart）')
st.bar_chart(df2)

# MAP
"""
---
### マッピング

```python
# 新宿付近の緯度経度を標準正規分布で周辺にマッピングするようにdf3を変形
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon'] # 緯度,経度
)
st.map(df3)
```
"""
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon'] # 緯度,経度
)

st.map(df3)

st.write('Interactive Widgets')

# インタラクティブなウィジェット
"""
---
## インタラクティブなウィジェット
### checkbox / selectbox / text_input の活用
```python
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
```
"""

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

#st.sidebar
number = st.sidebar.selectbox(
    'あなたが好きな数字を教えて下さい. ',
    list(range(1,11)),
    key = 'select_box1'
)
text = st.sidebar.text_input('あなたの趣味を教えて下さい')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50, key='silider1')

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