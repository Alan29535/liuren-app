import streamlit as st
from zhdate import ZhDate
from datetime import datetime

def get_shichen_from_time(hour, minute):
    time_decimal = hour + minute / 60
    if 23 <= time_decimal or time_decimal < 1:
        return "子"
    elif 1 <= time_decimal < 3:
        return "丑"
    elif 3 <= time_decimal < 5:
        return "寅"
    elif 5 <= time_decimal < 7:
        return "卯"
    elif 7 <= time_decimal < 9:
        return "辰"
    elif 9 <= time_decimal < 11:
        return "巳"
    elif 11 <= time_decimal < 13:
        return "午"
    elif 13 <= time_decimal < 15:
        return "未"
    elif 15 <= time_decimal < 17:
        return "申"
    elif 17 <= time_decimal < 19:
        return "酉"
    elif 19 <= time_decimal < 21:
        return "戌"
    elif 21 <= time_decimal < 23:
        return "亥"

def liuren_step(start, steps):
    liuren = ['大安', '留连', '速喜', '赤口', '小吉', '空亡']
    return liuren[(start + steps - 1) % 6]

def get_liuren_result(lunar_month, lunar_day, shichen_index):
    step1 = (lunar_month - 1) % 6
    step2 = (lunar_day - 1) % 6
    final = liuren_step(step2, shichen_index + 1)
    return final

dizhi_map = {
    "子": 0, "丑": 1, "寅": 2, "卯": 3,
    "辰": 4, "巳": 5, "午": 6, "未": 7,
    "申": 8, "酉": 9, "戌": 10, "亥": 11
}

st.title("🔮 小六壬占卜")
st.markdown("请输入阳历日期与时间（如 12:30），查看吉凶卦象")

col1, col2 = st.columns(2)
with col1:
    input_date = st.date_input("阳历日期")

with col2:
    input_time = st.time_input("预测时间")

if st.button("开始占卜"):
    lunar = ZhDate.from_datetime(datetime.combine(input_date, datetime.min.time()))
    lunar_month = lunar.lunar_month
    lunar_day = lunar.lunar_day
    hour = input_time.hour
    minute = input_time.minute
    shichen = get_shichen_from_time(hour, minute)
    shichen_index = dizhi_map[shichen]
    result = get_liuren_result(lunar_month, lunar_day, shichen_index)

    st.success(f"🌙 阴历：{lunar_month}月{lunar_day}日，当前时辰为：{shichen}时")
    st.markdown(f"### 🧿 占卜结果：{result}")

    meaning_map = {
        "大安": "大安：平稳顺利，万事如意，适合静守。",
        "留连": "留连：事情拖延、反复、难有结果。",
        "速喜": "速喜：有喜事来临，适合行动，速战速决。",
        "赤口": "赤口：口舌是非，容易有冲突，不利交际。",
        "小吉": "小吉：小有收获，吉中带平，可顺势而为。",
        "空亡": "空亡：事情落空，计划落空，适合避开风险。"
    }

    st.info(meaning_map[result])
