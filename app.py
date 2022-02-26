import streamlit as st

st.title('PFCカリキュレーター')

sex = st.sidebar.selectbox('性別', ['男性', '女性'])
age = st.sidebar.slider('年齢', 0, 100, 30)
height = st.sidebar.slider('身長（cm）', 100, 200, 150)
weight = st.sidebar.slider('体重（kg）', 30, 150, 50)
activity = st.sidebar.selectbox('活動レベル', ['低い', '中程度', '高い'])
purpose = st.sidebar.selectbox('体重を', ['維持したい', '減らしたい', '増やしたい'])

def calc_base_metabolism(age, sex, height, weight):
    if sex == '男性':
        return 13.397*weight+4.799*height-5.677*age+88.362
    else:
        return 9.247*weight+3.098*height-4.33*age+447.593

def calc_metabolism(base_metabolism, activity):
    if activity == '高い':
        return base_metabolism * 1.725
    elif activity == '中程度':
        return base_metabolism * 1.55
    else:
        return base_metabolism * 1.2

def calc_additional_calorie(weight, purpose):
    if purpose == '減らしたい':
        return weight * -0.02 * (7200/30)
    elif purpose == '増やしたい':
        return weight * 0.01 * (5000/30)
    else:
        return 0

base_metabolism = int(calc_base_metabolism(age, sex, height, weight))
metabolism = int(calc_metabolism(base_metabolism, activity) + calc_additional_calorie(weight, purpose))
protein = int(metabolism/10*2/4)
fat = int(metabolism/10*2/9)
carbo = int(metabolism/10*6/4)

st.write('### あなたの基礎代謝')
st.write(f'{base_metabolism}kcal')
st.write('### 目標摂取カロリー')
st.write(f'{metabolism}kcal')
st.write('### おすすめPFCバランス')
st.write(f"""
炭水化物{carbo}g

タンパク質{protein}g

脂質{fat}g
""")

