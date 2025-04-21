import streamlit as st
from zhdate import ZhDate
from datetime import datetime

# 将时间（小时+分钟）转换为地支时辰
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

# 小六壬顺序步进
def liuren_step(start, steps):
    liuren = ['大安', '留连', '速喜', '赤口', '小吉', '空亡']
    return (start + steps - 1) % 6, liuren[(start + steps - 1) % 6]

# 修正后的三步推理逻辑（附带 debug 起点显示）
def get_liuren_result(lunar_month, lunar_day, shichen_index):
    month_start_index, month_start_name = liuren_step(0, lunar_month)
    day_start_index, day_start_name = liuren_step(month_start_index, lunar_day)
    final_index, final_name = liuren_step(day_start_index, shichen_index + 1)
    return final_name, month_start_name, day_start_name

# 地支映射表
dizhi_map = {
    "子": 0, "丑": 1, "寅": 2, "卯": 3,
    "辰": 4, "巳": 5, "午": 6, "未": 7,
    "申": 8, "酉": 9, "戌": 10, "亥": 11
}

# 页面设置
st.set_page_config(page_title="小六壬占卜", page_icon="🔮")
st.title("🔮 小六壬占卜工具")
st.markdown("请输入你要占卜的阳历日期，以及你看到的时间（例如：12:30）")

# 输入阳历日期
input_date = st.date_input("阳历日期")

# 手动输入时间字符串
input_time_str = st.text_input("请输入你预测当时的时间（格式：HH:MM，例如 12:30）", value="12:30")

# 开始按钮
if st.button("开始占卜"):
    try:
        # 检查格式
        if ":" not in input_time_str:
            st.error("时间格式错误，请输入形如 12:30 的格式")
            st.stop()

        # 时间拆解
        hour, minute = map(int, input_time_str.strip().split(":"))
        shichen = get_shichen_from_time(hour, minute)
        shichen_index = dizhi_map[shichen]

        # 阳历 → 阴历
        lunar = ZhDate.from_datetime(datetime.combine(input_date, datetime.min.time()))
        lunar_month = lunar.lunar_month
        lunar_day = lunar.lunar_day

        # 获取卦象结果 + 每步起点
        result, step1, step2 = get_liuren_result(lunar_month, lunar_day, shichen_index)

        # 输出结果
        st.success(f"🌙 阴历：{lunar_month}月{lunar_day}日，当前时辰为：{shichen}时")
        st.markdown(f"### 🧿 最终占卜结果：**{result}**")

        # 解释含义
        meaning_map = {
            "大安": "大安：平稳顺利，万事如意，适合静守。",
            "留连": "留连：事情拖延、反复、难有结果。",
            "速喜": "速喜：有喜事来临，适合行动，速战速决。",
            "赤口": "赤口：口舌是非，容易有冲突，不利交际。",
            "小吉": "小吉：小有收获，吉中带平，可顺势而为。",
            "空亡": "空亡：事情落空，计划落空，适合避开风险。"
        }

        st.info(meaning_map[result])

        # 🛠 Debug 显示每一步
        with st.expander("🔍 显示三步推理过程"):
            st.write(f"第一步（月份起点）：{step1}")
            st.write(f"第二步（日期起点）：{step2}")
            st.write(f"第三步（从“{step2}”数 {shichen_index + 1} 下）→ **{result}**")

    except Exception as e:
        st.error(f"⚠️ 出现错误：{e}\n\n请确保你输入的是正确的时间格式（例如 12:30）")
