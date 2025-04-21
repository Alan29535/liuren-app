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

st.set_page_config(page_title="小六壬取数占卜", page_icon="🎲")
st.title("🎲 小六壬取数占卜（方法二）")
st.markdown("请输入你第一反应想到的数字，每个数字之间用英文逗号隔开，如：`1,2,5`")

# 输入格式：1,2,5
input_str = st.text_input("请输入数字：", value="1,2,5")

if st.button("开始占卜"):
    try:
        # 拆分字符串 → 数字列表
        digits = [int(d.strip()) for d in input_str.split(",") if d.strip().isdigit()]
        digit_count = len(digits)

        if digit_count == 0:
            st.error("❌ 没有有效数字，请输入形如 1,2,5 的格式")
            st.stop()

        # 步骤 1：相加
        total = sum(digits)

        # 步骤 2：按位数减法
        if digit_count == 3:
            total -= 2
        elif digit_count == 4:
            total -= 3
        # 1~2位数不减

        # 步骤 3：除以6取余
        remainder = total % 6
        if remainder == 0:
            remainder = 6

        result = liuren_map[remainder]

        # 显示详细计算过程
        st.markdown(f"### 🧮 计算过程：")
        st.code(f"""
输入数字：{input_str}
各位相加：{' + '.join(str(d) for d in digits)} = {sum(digits)}
减法规则：位数 {digit_count} → 减去 {3 if digit_count==4 else 2 if digit_count==3 else 0} → {total}
取余数：{total} ÷ 6 余数 = {remainder}
        """)
        st.markdown(f"### 🧿 卦象结果：**{remainder} → {result}**")

    except Exception as e:
        st.error(f"⚠️ 输入处理错误：{e}")
