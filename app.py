import streamlit as st
import pandas as pd
import time

# ==========================================
# 1. 页面配置与全局美化
# ==========================================
st.set_page_config(page_title="智能分析总控台", page_icon="??", layout="wide")

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%); }
    .stButton>button {
        background: linear-gradient(90deg, #0284c7 0%, #0369a1 100%);
        color: white; border-radius: 8px; border: none; transition: all 0.3s; font-weight: bold;
    }
    .stButton>button:hover { box-shadow: 0 4px 12px rgba(2, 132, 199, 0.4); transform: translateY(-2px); }
    .ball-container { display: flex; gap: 10px; justify-content: center; margin: 15px 0; }
    .ball { width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: bold; color: white; box-shadow: 2px 2px 5px rgba(0,0,0,0.2); }
    .ball-red { background: radial-gradient(circle, #f87171, #dc2626); }
    .ball-blue { background: radial-gradient(circle, #60a5fa, #2563eb); }
    .ball-green { background: radial-gradient(circle, #4ade80, #16a34a); }
    .ball-special { background: radial-gradient(circle, #fbbf24, #d97706); border: 2px solid #fff; }
</style>
""", unsafe_allow_html=True)

# 初始化 session_state 用于存储输入内容
if "ai_input_text" not in st.session_state:
    st.session_state.ai_input_text = "这是2026117期第一球的核算条件，第一球的取值区间为1号至20号之间，"
if "ai_result_text" not in st.session_state:
    st.session_state.ai_result_text = "等待推演..."

# ==========================================
# 2. 侧边栏导航
# ==========================================
with st.sidebar:
    st.title("?? 系统控制台")
    page = st.radio("导航菜单", ["?? 主界面", "?? AI 智能推演"])
    st.divider()

# ==========================================
# 3. 页面一：主界面
# ==========================================
if page == "?? 主界面":
    st.title("?? 智能数据分析总控台")
    st.subheader("?? 最新开奖结果")
    
    st.markdown("""
    <div class="ball-container">
        <div class="ball ball-red">03</div>
        <div class="ball ball-blue">12</div>
        <div class="ball ball-green">25</div>
        <div class="ball ball-red">33</div>
        <div class="ball ball-blue">41</div>
        <div class="ball ball-green">48</div>
        <div class="ball ball-special">★ 09</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.subheader("?? 操作控制台")
    col1, col2, col3 = st.columns(3)
    with col1:
        period = st.selectbox("选择分析期数:", ["2026117", "2026116", "2026115"])
    with col2:
        st.write("")
        st.write("")
        if st.button("?? 一键同步总数据", use_container_width=True):
            with st.spinner("正在拉取数据..."):
                time.sleep(1)
                st.success("? 同步完成！")
    with col3:
        st.write("")
        st.write("")
        if st.button("?? 开始执行计算", use_container_width=True):
            with st.spinner("正在计算..."):
                time.sleep(1)
                st.success(f"? 计算完成！")


# ==========================================
# 4. 页面二：AI 智能推演 (带复选框)
# ==========================================
elif page == "?? AI 智能推演":
    st.title("?? AI 严谨推演系统")
    
    # 左右分栏 (比例为 1:1，保证两边都宽敞)
    col_left, col_right = st.columns(2, gap="large")

    # ---------------- 左侧：输入与展示 ----------------
    with col_left:
        st.subheader("?? 核算条件输入")
        user_input = st.text_area("条件内容：", value=st.session_state.ai_input_text, height=200)
        
        if user_input != st.session_state.ai_input_text:
            st.session_state.ai_input_text = user_input

        st.subheader("?? 分析结果")
        st.text_area("推演结果：", value=st.session_state.ai_result_text, height=250, disabled=True)

    # ---------------- 右侧：复选框矩阵 ----------------
    with col_right:
        st.subheader("?? 快捷条件勾选")
        
        # 复选框区域 (折叠面板)
        with st.expander("?? 生肖与五行", expanded=True):
            c1, c2, c3 = st.columns(3)
            if c1.checkbox("金肖"): st.session_state.ai_input_text += "杀金肖（猴鸡），"
            if c2.checkbox("木肖"): st.session_state.ai_input_text += "杀木肖（虎兔），"
            if c3.checkbox("水肖"): st.session_state.ai_input_text += "杀水肖（鼠猪），"
            if c1.checkbox("火肖"): st.session_state.ai_input_text += "杀火肖（蛇马），"
            if c2.checkbox("土肖"): st.session_state.ai_input_text += "杀土肖（牛龙羊狗），"

        with st.expander("?? 尾数杀号"):
            t_cols = st.columns(5)
            for i in range(10):
                if t_cols[i % 5].checkbox(f"{i}尾"):
                    st.session_state.ai_input_text += f"杀{i}尾，"

        with st.expander("?? 波色单双"):
            b_cols = st.columns(3)
            if b_cols[0].checkbox("红波"): st.session_state.ai_input_text += "杀红波，"
            if b_cols[1].checkbox("蓝波"): st.session_state.ai_input_text += "杀蓝波，"
            if b_cols[2].checkbox("绿波"): st.session_state.ai_input_text += "杀绿波，"
            if b_cols[0].checkbox("红波单"): st.session_state.ai_input_text += "杀红波单，"
            if b_cols[1].checkbox("红波双"): st.session_state.ai_input_text += "杀红波双，"
            if b_cols[2].checkbox("蓝波单"): st.session_state.ai_input_text += "杀蓝波单，"
            
        # 按钮区
        st.divider()
        btn1, btn2 = st.columns(2)
        with btn1:
            if st.button("?? 开始呼叫 AI", use_container_width=True):
                with st.spinner("AI 深度推演中..."):
                    st.session_state.ai_result_text = "【严格筛选结果】：03, 08, 15, 22\\\\n\\\\n【后补筛选结果】：01, 19, 33, 41"
                    st.rerun()
        with btn2:
            if st.button("??? 清空条件", use_container_width=True):
                st.session_state.ai_input_text = f"这是2026117期第一球的核算条件，"
                st.session_state.ai_result_text = "等待推演..."
                st.rerun()