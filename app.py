import streamlit as st
from pages_content import (
    show_overview,
    show_research,
    show_solution,
    show_metrics,
    show_interview_prep,
    show_roadmap,
)
from data.pain_points import PAIN_POINTS

st.set_page_config(
    page_title="Nykaa Fashion — PM Project Dashboard",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
[data-testid="stSidebar"] { background: #fff0f5; border-right: 1.5px solid #f5c6d8; }
.brand-strip { background: linear-gradient(135deg, #FCE4EC, #F8BBD0); border-radius: 12px; padding: 24px 28px; margin-bottom: 24px; border: 1px solid #f5c6d8; }
.brand-strip h1 { font-family: 'Playfair Display', serif; font-size: 32px; color: #1A0A10; margin: 0; }
.brand-strip p { color: #7A5060; font-size: 15px; margin: 6px 0 0; }
.northstar { background: linear-gradient(135deg,#fce4ec,#fff); border: 1px solid #f5c6d8; border-left: 4px solid #E84393; border-radius: 8px; padding: 16px 20px; margin-bottom: 16px; }
.northstar .ns-label { font-size:11px; font-weight:700; letter-spacing:1.2px; text-transform:uppercase; color:#7A5060; }
.northstar .ns-val { font-size:17px; font-weight:700; color:#E84393; margin-top:4px; }
div.stButton > button { background: #E84393 !important; color: white !important; border: none !important; border-radius: 8px !important; font-weight: 600 !important; }
div.stButton > button:hover { background: #C2185B !important; }
</style>
""", unsafe_allow_html=True)

if "selected_pain" not in st.session_state:
    st.session_state.selected_pain = None
if "step" not in st.session_state:
    st.session_state.step = 1

with st.sidebar:
    st.markdown("## 💄 Nykaa Fashion\n**PM Project Dashboard**")
    st.markdown("---")
    st.markdown("### 📋 PM Process Steps")
    steps = [
        "Problem Definition",
        "User Research",
        "User Personas",
        "RICE Prioritization",
        "Feature Solution",
        "Success Metrics",
        "Roadmap & GTM",
    ]
    for i, s in enumerate(steps, 1):
        icon = "✅" if i < st.session_state.step else ("▶️" if i == st.session_state.step else "⬜")
        st.markdown(f"{icon} **Step {i}** — {s}")
    st.markdown("---")
    if st.session_state.selected_pain:
        st.markdown(f"**Selected Pain Point:**\n\n🎯 {st.session_state.selected_pain}")
    else:
        st.markdown("_No pain point selected yet_")
    st.markdown("---")
    progress = (st.session_state.step - 1) / 7
    st.markdown(f"**Project Progress:** {st.session_state.step - 1}/7")
    st.progress(progress)
    st.caption("3–4 week plan · Resume-ready · GitHub-publishable")

st.markdown("""
<div class="brand-strip">
  <h1>Nykaa Fashion — PM Live Project</h1>
  <p>A complete end-to-end Product Manager case study · Solving real user pain points · Interview & GitHub ready</p>
</div>
""", unsafe_allow_html=True)

pain_data = PAIN_POINTS

tabs = st.tabs([
    "🏠 Overview",
    "🔬 Research",
    "💡 Solution",
    "📊 Metrics",
    "🗺️ Roadmap",
    "🎤 Interview Prep",
])

with tabs[0]:
    show_overview(pain_data)
with tabs[1]:
    show_research(pain_data)
with tabs[2]:
    show_solution(pain_data)
with tabs[3]:
    show_metrics(pain_data)
with tabs[4]:
    show_roadmap(pain_data)
with tabs[5]:
    show_interview_prep(pain_data)
