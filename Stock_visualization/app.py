import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
import altair as alt
import datetime

st.title('株価可視化アプリ')
st.sidebar.write("""
# 株価
こちらは株価可視化ツールです、以下のオプションから表示日数を指定
""")

st.sidebar.write("""
## 表示日数選択
""")

days = st.sidebar.slider("日数", 1, 365, 100)

st.write(f"""
### 過去**{days}日間**の株価
""")

tickers = {
    'apple': 'AAPL',
    'microsoft': 'MSFT',
    'google': 'GOOGL',
    'netflix': 'NFLT',
    'amazon': 'AMZN',
    'facebook':'META'
}

@st.cache_data
def get_data(days, tickers):
  end_date = datetime.datetime.now()
  start_date = end_date - datetime.timedelta(days)

  df = pd.DataFrame()
  for company in tickers.keys():
    tkr = yf.Ticker(tickers[company])
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days)

    hist = tkr.history(start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    hist.index = hist.index.strftime('%d %B %Y')
    hist = hist[['Close']]
    hist.columns = [company]
    hist = hist.T
    hist.index.name = 'Name'
    df = pd.concat([df, hist])

  return df

try:
    st.sidebar.write("""
    ## 株価の範囲指定
    """)

    ymin, ymax = st.sidebar.slider('範囲を指定して下さい。', 0.0 , 2000.0, (0.0, 2000.0))

    df = get_data(days, tickers)

    companies = st.multiselect(
        '会社名を選択して下さい。',
        list(df.index),
        ['google', 'amazon', 'facebook', 'apple']
    )

    if not companies:
        st.error('少なくとも１社は選択して下さい。')
    else:
        data = df.loc[companies]
        st.write('### 株価(USD)', data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
            columns={'value': 'Stock Prices(USD)'}
        )

    chart = (
        alt.Chart(data)
        .mark_line(opacity=0.8, clip=True)
        .encode(
            x = "Date:T",
            y = alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
            color = "Name:N"
        )
    )

    st.altair_chart(chart, use_container_width=True)

except:
    st.error(
        "エラーが発生しました。"
    )
