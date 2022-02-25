import streamlit as st

st.write('# PFC計算')

sex = st.sidebar.selectbox('性別', ['男性', '女性'])
age = st.sidebar.slider('年齢', 0, 100, 30)
height = st.sidebar.slider('身長（cm）', 100, 250, 150)
weight = st.sidebar.slider('体重（kg）', 30, 200, 50)
activity = st.sidebar.selectbox('活動レベル', ['低い', '中程度', '高い'])

def calc_base_metabolism(age, sex, height, weight):
    if sex == '男性':
        return 13.397*weight+4.799*height-5.677*age+88.362
    else:
        return 9.247*weight+3.098*height-4.33*age+447.593

base_metabolism = int(calc_base_metabolism(age, sex, height, weight))

def calc_metabolism(base_metabolism, activity):
    if activity == '高い':
        return base_metabolism * 1.725
    elif activity == '中程度':
        return base_metabolism * 1.55
    else:
        return base_metabolism * 1.2

metabolism = int(calc_metabolism(base_metabolism, activity))
protein = int(metabolism/10*2/4)
fat = int(metabolism/10*2/9)
carbo = int(metabolism/10*6/4)

st.write('## あなたの基礎代謝')
st.write(f'{base_metabolism}kcal')
st.write('## 維持カロリー')
st.write(f'{metabolism}kcal')
st.write('## 理想PFCバランス')
st.write(f"""
炭水化物{carbo}g

タンパク質{protein}ｇ

脂質{fat}g
""")

