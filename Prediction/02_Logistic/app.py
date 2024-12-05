import streamlit as st
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# ロジスティック成長曲線（認知率を考慮したバージョン）
def logistic_curve_with_awareness(x, L, r, x0):
    return L / (1 + np.exp(-r * (x  - x0)))

st.markdown('**ロジスティック曲線**を使用したフィッティング')
st.latex('''y=\dfrac{L}{1+e^{-r(x-x_0)}}''')
"""
- $L$：上限・飽和ライン
- $r$：成長率
- $x_0$：成長曲線の傾きが変わる点
- $a$：広告認知率
"""

st.markdown('使用例')

"""
- $D$：ダウンロード数（上限・飽和ライン）
- $r$：成長率
- $x_0$：成長曲線の傾きが変わる点（変曲点）
- $a$：広告認知率
"""

# サンプルデータ
data = pd.DataFrame({
    'awareness_rate': [0.1, 0.15, 0.2, 0.25, 0.3, 0.35],
    'downloads': [100, 300, 600, 1200, 1800, 2500]
})

st.table(data)
xdata = data['awareness_rate']
ydata = data['downloads']
p0 = [max(ydata), 0.001, np.median(xdata)] # L, k, x0, a の初期値
# フィッティング
popt, _ = curve_fit(
    lambda x, L, k, x0: logistic_curve_with_awareness(x, L, k, x0),
    xdata, ydata, p0=p0, maxfev=10000
    )
# 決定係数の計算
residuals = ydata - logistic_curve_with_awareness(xdata, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata - np.mean(ydata))**2)
r_squared = 1 - (ss_res/ss_tot)

# フィッティング結果の予測カーブの計算
x_fit = np.linspace(min(xdata), max(xdata)*2, 1000)
y_fit = logistic_curve_with_awareness(x_fit, *popt)

# 結果のプロット
fig = plt.figure(figsize=(10, 6))
plt.scatter(xdata, ydata, label='Data', color='blue')
plt.plot(x_fit, y_fit, label='Logistic Fit', color='red')
plt.xlabel('awareness_rate')
plt.ylabel('downloads')
plt.text(0.05, 0.95, f'R^2 = {r_squared:.4f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.legend()
plt.title('Logistic Growth Curve')
st.write(fig)

# 最適パラメータの表示
L, r, x0 = popt
st.write("最適パラメータ")
st.write("L = ", L)
st.write("r = ", r)
st.write("x0 = ", x0)


if "target_column" not in st.session_state:
    st.session_state["target_column"] = "ターゲット指定なし"

uploaded_file = st.file_uploader('ファイルをアップロードして下さい。')
if uploaded_file is not None:
    st.info("ファイルが正しくアップロードされました")
    df = pd.read_csv(uploaded_file)
    st.table(df.head(10))
    column_names = [c for c in df.columns]
    target_column = st.selectbox("目的変数を選んでください。", column_names)
    example_column = st.selectbox("説明変数を選んでください。", column_names)

    if st.button('モデル作成開始') or st.session_state['target_column'] == target_column:
        st.session_state["target_column"] = target_column

        xdata = df[example_column]
        ydata = df[target_column]
        p0 = [max(ydata), 0.001, np.median(xdata)] # L, k, x0, a の初期値
        # フィッティング
        popt, _ = curve_fit(
            lambda x, L, k, x0: logistic_curve_with_awareness(x, L, k, x0),
            xdata, ydata, p0=p0, maxfev=10000
    )

        # フィッティング結果の予測カーブの計算
        x_fit = np.linspace(min(xdata), max(xdata)*1.5, 1000)
        y_fit = logistic_curve_with_awareness(x_fit, *popt)

        # 決定係数の計算
        residuals = ydata - logistic_curve_with_awareness(xdata, *popt)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((ydata - np.mean(ydata))**2)
        r_squared = 1 - (ss_res/ss_tot)

        # 結果のプロット
        fig = plt.figure(figsize=(10, 6))
        plt.scatter(xdata, ydata, label='Data', color='blue')
        plt.plot(x_fit, y_fit, label='Logistic Fit', color='red')
        plt.xlabel(f"{example_column}")
        plt.ylabel(f"{target_column}")
        plt.text(0.05, 0.95, f'R^2 = {r_squared:.4f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
        plt.legend()
        plt.title('Logistic Growth Curve')
        st.write(fig)

        # 最適パラメータの表示
        L, r, x0 = popt
        st.write("最適パラメータ")
        st.write("L = ", L)
        st.write("r = ", r)
        st.write("x0 = ", x0)