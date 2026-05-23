import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


PINK = "#E84393"
LIGHT_PINK = "#FCE4EC"
DEEP_PINK = "#C2185B"


# ─────────────────────────────────────────────
# OVERVIEW
# ─────────────────────────────────────────────
def show_overview(pain_data):
    st.markdown("### 🎯 Step 1 — Select a User Pain Point")
    st.caption("Pick one pain point from Nykaa Fashion's real user problems to anchor your entire PM project.")

    selected = st.session_state.get("selected_pain")

    cols = st.columns(2)
    for idx, (key, val) in enumerate(pain_data.items()):
        col = cols[idx % 2]
        with col:
            is_sel = selected == key
            border = f"2px solid {PINK}" if is_sel else "1px solid #f5c6d8"
            bg = LIGHT_PINK if is_sel else "#fff8fa"
            sev_color = "#C62828" if val["severity"] == "High" else "#F57F17"
            sev_bg = "#FFEBEE" if val["severity"] == "High" else "#FFF8E1"
            st.markdown(f"""
<div style="border:{border};border-radius:10px;padding:16px;background:{bg};margin-bottom:10px">
  <div style="font-size:22px;margin-bottom:6px">{val['icon']}</div>
  <div style="font-size:14px;font-weight:700;color:#1A0A10;margin-bottom:4px">{val['short']}</div>
  <div style="font-size:12px;color:#7A5060;line-height:1.5;margin-bottom:8px">{val['desc']}</div>
  <span style="background:{sev_bg};color:{sev_color};font-size:11px;font-weight:700;padding:3px 9px;border-radius:20px">● {val['severity']} Impact</span>
  &nbsp;
  <span style="background:#fff;color:{PINK};font-size:12px;font-weight:700;padding:3px 9px;border-radius:20px;border:1px solid #f5c6d8">{val['stat']} — {val['stat_label']}</span>
</div>
""", unsafe_allow_html=True)
            if st.button(f"{'✅ Selected' if is_sel else '▷ Select'} — {val['short']}", key=f"sel_{idx}"):
                st.session_state.selected_pain = key
                st.session_state.step = 2
                st.rerun()

    st.markdown("---")
    st.markdown("### 📅 3–4 Week Project Plan")
    weeks = [
        ("Week 1", "Discover & Define", "Select pain point → write problem statement · Secondary research (app reviews, Reddit) · Create 2–3 user personas · Map user journey"),
        ("Week 2", "Ideate & Prioritise", "Competitive analysis (Myntra, AJIO, Meesho) · Brainstorm 10+ feature ideas · Apply RICE framework · Define North Star Metric"),
        ("Week 3", "Design & Validate", "Write PRD (Product Requirements Doc) · Create low-fi wireframes (Figma) · Define A/B test hypothesis · Write user stories"),
        ("Week 4", "Ship & Measure", "Define launch checklist · Set up success metrics dashboard · Write case study doc · Publish to GitHub + LinkedIn"),
    ]
    for w, title, tasks in weeks:
        color = "#00897B" if w == "Week 4" else PINK
        st.markdown(f"""
<div style="border-left:3px solid {color};background:white;border:1px solid #f5c6d8;border-left:3px solid {color};border-radius:0 8px 8px 0;padding:14px 16px;margin-bottom:10px">
  <div style="font-size:13px;font-weight:700;color:{color};margin-bottom:6px">{w} — {title}</div>
  <div style="font-size:13px;color:#7A5060;line-height:1.8">{tasks}</div>
</div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# RESEARCH
# ─────────────────────────────────────────────
def show_research(pain_data):
    selected = st.session_state.get("selected_pain")
    if not selected:
        st.info("👈 Please select a pain point on the **Overview** tab first.")
        return

    d = pain_data[selected]
    st.session_state.step = max(st.session_state.step, 3)

    st.markdown(f"### 🔬 Step 2 — User Research: *{d['short']}*")
    st.markdown(f"<span style='background:#E8F5E9;color:#2E7D32;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;letter-spacing:.6px;text-transform:uppercase'>Research Phase</span>", unsafe_allow_html=True)
    st.markdown("")

    # Key stat
    c1, c2, c3 = st.columns(3)
    c1.metric("Key Metric", d["stat"], d["stat_label"])
    c2.metric("Personas Built", "2", "Based on research")
    c3.metric("Competitors Analysed", "3", "Myntra · AJIO · Meesho")

    st.markdown("#### 📝 Problem Statement")
    st.info(d["problem_statement"])

    st.markdown("#### 🔍 Research Findings")
    for r in d["research"]:
        with st.expander(f"📌 {r['title']}", expanded=True):
            st.write(r["body"])

    st.markdown("---")
    st.markdown("### 👤 Step 3 — User Personas")
    st.markdown(f"<span style='background:#E8F5E9;color:#2E7D32;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px'>Personas</span>", unsafe_allow_html=True)
    st.markdown("")
    for p in d["personas"]:
        with st.container():
            pc1, pc2 = st.columns([1, 3])
            with pc1:
                st.markdown(f"<div style='font-size:48px;text-align:center;background:{LIGHT_PINK};border-radius:50%;width:72px;height:72px;display:flex;align-items:center;justify-content:center;margin:auto'>{p['icon']}</div>", unsafe_allow_html=True)
            with pc2:
                st.markdown(f"**{p['name']}**")
                st.caption(p["role"])
                st.markdown(f"> *{p['quote']}*")
                g_col, f_col = st.columns(2)
                with g_col:
                    st.markdown("**Goals**")
                    for g in p["goals"]:
                        st.markdown(f"✅ {g}")
                with f_col:
                    st.markdown("**Frustrations**")
                    for f in p["frustrations"]:
                        st.markdown(f"⚠️ {f}")
            st.markdown("---")
    st.session_state.step = max(st.session_state.step, 4)


# ─────────────────────────────────────────────
# SOLUTION
# ─────────────────────────────────────────────
def show_solution(pain_data):
    selected = st.session_state.get("selected_pain")
    if not selected:
        st.info("👈 Please select a pain point on the **Overview** tab first.")
        return

    d = pain_data[selected]
    st.session_state.step = max(st.session_state.step, 5)

    # RICE
    st.markdown("### 📊 Step 4 — RICE Prioritisation")
    st.markdown(f"<span style='background:#FFF3E0;color:#E65100;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px'>Prioritisation</span>", unsafe_allow_html=True)
    st.markdown("")

    df = pd.DataFrame(d["rice"])
    df_display = df.copy()
    df_display.columns = ["Feature Idea", "Reach", "Impact (1–10)", "Confidence", "Effort", "RICE Score"]
    max_score = df["score"].max()
    st.dataframe(
        df_display.style.apply(
            lambda row: ["background-color: #FCE4EC; font-weight: bold" if float(row["RICE Score"]) == max_score else "" for _ in row],
            axis=1,
        ),
        use_container_width=True,
        hide_index=True,
    )

    # Bar chart
    fig = px.bar(
        df.sort_values("score", ascending=True),
        x="score",
        y="feature",
        orientation="h",
        color="score",
        color_continuous_scale=[[0, "#FCE4EC"], [1, PINK]],
        labels={"score": "RICE Score", "feature": "Feature"},
        title="RICE Score Comparison",
    )
    fig.update_layout(showlegend=False, coloraxis_showscale=False, plot_bgcolor="white", height=280, margin=dict(l=0, r=0, t=40, b=0))
    fig.update_xaxes(showgrid=True, gridcolor="#f5c6d8")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.markdown(f"### 💡 Step 5 — Proposed Feature: *{d['solution_name']}*")
    st.markdown(f"<span style='background:#FFF3E0;color:#E65100;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px'>Feature Design</span>", unsafe_allow_html=True)
    st.markdown("")

    st.markdown("#### 🔄 User Flow")
    flow_cols = st.columns(len(d["solution_flow"]))
    for i, (col, step) in enumerate(zip(flow_cols, d["solution_flow"])):
        with col:
            arrow = "→" if i < len(d["solution_flow"]) - 1 else ""
            st.markdown(f"""
<div style="background:{LIGHT_PINK};border:1px solid #f5c6d8;border-radius:8px;padding:10px 8px;font-size:11px;font-weight:600;color:{DEEP_PINK};text-align:center;min-height:60px;display:flex;align-items:center;justify-content:center">
{step}
</div>""", unsafe_allow_html=True)

    st.markdown("#### ✅ Acceptance Criteria")
    for c in d["acceptance_criteria"]:
        st.markdown(f"✅ {c}")


# ─────────────────────────────────────────────
# METRICS
# ─────────────────────────────────────────────
def show_metrics(pain_data):
    selected = st.session_state.get("selected_pain")
    if not selected:
        st.info("👈 Please select a pain point on the **Overview** tab first.")
        return

    d = pain_data[selected]
    st.session_state.step = max(st.session_state.step, 6)

    st.markdown("### 📊 Step 6 — Success Metrics")
    st.markdown(f"<span style='background:#F3E5F5;color:#6A1B9A;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px'>Metrics</span>", unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"""
<div class="northstar" style="background:linear-gradient(135deg,#fce4ec,#fff);border:1px solid #f5c6d8;border-left:4px solid {PINK};border-radius:8px;padding:16px 20px;margin-bottom:16px">
  <div style="font-size:11px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;color:#7A5060">⭐ North Star Metric</div>
  <div style="font-size:18px;font-weight:700;color:{PINK};margin-top:6px">{d['north_star']}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("#### 🎯 OKRs — Objectives & Key Results")
    for o in d["okrs"]:
        with st.expander(f"🎯 {o['objective']}", expanded=True):
            st.markdown(f"**Key Result:** {o['key_result']}")

    st.markdown("#### ⚠️ Guardrail Metrics")
    for g in d["guardrails"]:
        st.warning(f"⚠️ {g}")

    # Simulated metric chart
    st.markdown("#### 📈 Simulated Impact Preview")
    fig = go.Figure()
    weeks = list(range(1, 13))
    baseline = [28] * 12
    projected = [28, 27.5, 26.8, 25.5, 23.9, 22.0, 20.8, 20.0, 19.3, 18.7, 18.2, 18.0]
    fig.add_trace(go.Scatter(x=weeks, y=baseline, name="Baseline (no change)", line=dict(color="#ccc", dash="dash")))
    fig.add_trace(go.Scatter(x=weeks, y=projected, name="With Feature", line=dict(color=PINK, width=3), fill="tozeroy", fillcolor="rgba(232,67,147,0.07)"))
    fig.update_layout(
        title="Projected improvement over 12 weeks (illustrative)",
        xaxis_title="Week",
        yaxis_title="Metric",
        plot_bgcolor="white",
        height=300,
        legend=dict(orientation="h", y=-0.2),
        margin=dict(l=0, r=0, t=40, b=0),
    )
    fig.update_xaxes(showgrid=True, gridcolor="#f5f5f5")
    fig.update_yaxes(showgrid=True, gridcolor="#f5f5f5")
    st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────
# ROADMAP
# ─────────────────────────────────────────────
def show_roadmap(pain_data):
    selected = st.session_state.get("selected_pain")
    if not selected:
        st.info("👈 Please select a pain point on the **Overview** tab first.")
        return

    d = pain_data[selected]
    st.session_state.step = max(st.session_state.step, 7)

    st.markdown("### 🗺️ Step 7 — Launch Roadmap & GTM")
    st.markdown(f"<span style='background:#E0F2F1;color:#00695C;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px'>Launch Plan</span>", unsafe_allow_html=True)
    st.markdown("")

    for i, r in enumerate(d["roadmap"]):
        color = PINK if i < len(d["roadmap"]) - 1 else "#00897B"
        st.markdown(f"""
<div style="border-left:3px solid {color};background:white;border:1px solid #f5c6d8;border-left:3px solid {color};border-radius:0 8px 8px 0;padding:14px 16px;margin-bottom:10px">
  <div style="font-size:13px;font-weight:700;color:{color};margin-bottom:4px">{r['phase']} — {r['title']}</div>
  <div style="font-size:13px;color:#7A5060;line-height:1.8">{r['tasks']}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📂 GitHub Repo Structure")
    st.code("""nykaa-pm-project/
├── README.md                  # Project overview
├── 01-problem-statement.md
├── 02-user-research.md
├── 03-personas.md
├── 04-rice-framework.md
├── 05-prd.md                  # Product Requirements Doc
├── 06-metrics.md
├── 07-roadmap.md
├── wireframes/                # Figma screenshots
└── assets/                    # Charts, diagrams""", language="text")

    st.markdown("### 🏷️ LinkedIn Post Template")
    st.markdown(f"""
> Completed a product management case study on **{d['short']}** for Nykaa Fashion.
> Identified the problem through user research, built 2 personas, prioritised solutions using
> the RICE framework, and defined success metrics with a phased GTM plan.
> Full project published on GitHub → [link]
> #ProductManagement #PM #NykaaFashion #ProductThinking
""")


# ─────────────────────────────────────────────
# INTERVIEW PREP
# ─────────────────────────────────────────────
def show_interview_prep(pain_data):
    selected = st.session_state.get("selected_pain")

    st.markdown("### 🎤 Interview Prep — Q&A Bank")
    st.markdown(f"<span style='background:#E3F2FD;color:#1565C0;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px'>Interview Ready</span>", unsafe_allow_html=True)
    st.markdown("")

    if not selected:
        st.info("👈 Select a pain point on the **Overview** tab to see your personalised Q&A.")

        # Generic PM questions when no pain point selected
        st.markdown("#### 📚 Universal PM Interview Questions")
        generic = [
            ("What is a product manager?", "A PM is the person responsible for defining the 'why' and 'what' of a product. They sit at the intersection of business, technology, and user experience — prioritising problems, guiding solutions, and measuring outcomes."),
            ("How do you prioritise features?", "I use frameworks like RICE (Reach × Impact × Confidence ÷ Effort) or ICE (Impact × Confidence × Ease) to score and rank features objectively. I always align prioritisation to the team's North Star metric."),
            ("How do you define success for a feature?", "I define success through a North Star metric that reflects core user value, supported by leading indicators (engagement, adoption), and guardrail metrics to prevent unintended harm (e.g. higher churn, lower NPS)."),
            ("Tell me about a product you use and how you'd improve it.", "I'd pick Nykaa Fashion and improve the size & fit experience. 67% of returns are size-related. I'd build a community size-tagging system and measurement-based recommender — this is the SizeMatch project I designed as a case study."),
        ]
        for q, a in generic:
            with st.expander(f"❓ {q}"):
                st.markdown(f"**Answer:** {a}")
        return

    d = pain_data[selected]
    st.markdown(f"**Showing Q&A for:** {selected}")
    st.markdown("")

    for qa in d["interview_qa"]:
        with st.expander(f"❓ {qa['q']}"):
            st.markdown(f"**Model Answer:**\n\n{qa['a']}")

    st.markdown("---")
    st.markdown("#### 🧩 PM Interview Frameworks Cheatsheet")

    cheat = {
        "RICE Prioritisation": "Reach × Impact × Confidence ÷ Effort = RICE Score. Higher = build first.",
        "North Star Metric": "Single metric that best captures core product value. All team efforts align to moving it.",
        "OKRs": "Objectives (qualitative goals) + Key Results (measurable outcomes). Set quarterly.",
        "User Story": "'As a [user], I want to [goal] so that [reason].' Used to define feature scope.",
        "A/B Testing": "Split users into control (old) and variant (new). Measure difference in target metric.",
        "Guardrail Metrics": "Metrics you must NOT harm while improving North Star. Catch unintended side-effects.",
        "PRD": "Product Requirements Document. Covers problem, users, solution, metrics, and launch plan.",
    }
    c1, c2 = st.columns(2)
    items = list(cheat.items())
    for i, (k, v) in enumerate(items):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""
<div style="background:#fff0f5;border:1px solid #f5c6d8;border-radius:8px;padding:12px 14px;margin-bottom:10px">
  <div style="font-size:12px;font-weight:700;color:{PINK};margin-bottom:4px">{k}</div>
  <div style="font-size:12px;color:#7A5060;line-height:1.6">{v}</div>
</div>""", unsafe_allow_html=True)
