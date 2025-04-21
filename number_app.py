import streamlit as st

# 小六壬卦象解释
liuren_map = {
    1: "大安：平稳顺利，万事如意，适合静守。",
    2: "留连：事情拖延、反复、难有结果。",
    3: "速喜：有喜事来临，适合行动，速战速决。",
    4: "赤口：口舌是非，容易有冲突，不利交际。",
    5: "小吉：小有收获，吉中带平，可顺势而为。",
    6: "空亡：事情落空，计划落空，适合避开风险。"
}

# 页面设置
st.set_page_config(page_title="小六壬取数占卜", page_icon="🎲")
st.title("🎲 小六壬取数占卜（方法二）")
st.markdown("输入你第一反应想到或看到的一组数字，例如：1325、888、03")

# 输入数字
input_str = st.text_input("请输入数字：", value="1325")

# 开始按钮
if st.button("开始占卜"):
    if not input_str.isdigit():
        st.error("❌ 请输入纯数字，例如 1325、100、888 等")
    else:
        # 每位数字相加
        digits = [int(ch) for ch in input_str]
        total = sum(digits)
        digit_count = len(digits)

        # 按位数减法
        if digit_count == 3:
            total -= 2
        elif digit_count == 4:
            total -= 3
        # 1~2 位数不减

        # 除以6取余，0视为6
        remainder = total % 6
        if remainder == 0:
            remainder = 6

        result = liuren_map[remainder]

        # 输出
        st.markdown(f"### 🧮 结果计算过程：")
        st.code(f"""
输入数字：{input_str}
各位相加：{' + '.join(str(d) for d in digits)} = {sum(digits)}
减去位数规则：{total + (3 if digit_count==4 else 2 if digit_count==3 else 0)} - {'3' if digit_count==4 else '2' if digit_count==3 else '0'} = {total}
除以 6：{total} ÷ 6 → 余数 = {remainder}
        """)
        st.markdown(f"### 🧿 卦象结果：**{remainder} → {result}**")