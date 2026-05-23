# 💄 Nykaa Fashion — PM Live Project Dashboard

A complete **end-to-end Product Manager case study** built as an interactive Streamlit dashboard. Designed to be published on GitHub and used as a portfolio project for PM interviews.

---

## 🎯 Project Overview

| Field | Detail |
|---|---|
| **Company** | Nykaa Fashion |
| **Focus** | Solving a real user pain point |
| **Timeline** | 3–4 weeks |
| **Outcome** | Interview-ready PM case study |

---

## 🗂️ What's Inside

The dashboard covers **all 7 PM process steps**:

1. **Problem Definition** — Identify and articulate the user pain point
2. **User Research** — Qualitative + quantitative evidence
3. **User Personas** — 2 archetypes per pain point
4. **RICE Prioritisation** — Score features by Reach, Impact, Confidence, Effort
5. **Feature Solution** — Proposed feature with user flow + acceptance criteria
6. **Success Metrics** — North Star, OKRs, and guardrail metrics
7. **Roadmap & GTM** — Phased launch plan + GitHub/LinkedIn templates

### 4 Pain Points Available

| Pain Point | Key Stat | Proposed Feature |
|---|---|---|
| 📏 Size & Fit Confusion | 67% returns cite wrong size | SizeMatch — Community + AI Size Intelligence |
| 🔍 Discovery & Personalisation Gap | 3.2 avg items browsed before exit | StyleDNA — Taste-Matched Personalisation |
| 📸 Product Image Quality Gap | 45% users abandon due to unclear visuals | TrueView — Seller Image Standards + Buyer Photos |
| 📦 Post-Purchase Experience | 38% users don't repurchase after bad return | NykaaReturn Pro — Frictionless Post-Purchase |

---

## 🚀 Running Locally

### Prerequisites
- Python 3.9+
- pip

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/nykaa-pm-dashboard.git
cd nykaa-pm-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## ☁️ Deploy on Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select your repo → set **Main file path** to `app.py`
4. Click **Deploy** — your live URL will be ready in ~2 minutes

---

## 📁 Project Structure

```
nykaa-pm-dashboard/
├── app.py                  # Main Streamlit app entry point
├── pages_content.py        # All tab/page rendering functions
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── data/
│   ├── __init__.py
│   └── pain_points.py      # All pain point data, personas, RICE, metrics
└── .streamlit/
    └── config.toml         # Theme configuration (Nykaa pink)
```

---

## 🎤 Interview Usage

Each pain point section includes:
- A **model problem statement** you can recite in PM interviews
- **RICE analysis** with scores and rationale
- **North Star + OKR definitions** to demonstrate metrics thinking
- **Q&A bank** with real PM interview questions and structured answers specific to your chosen pain point

### How to answer "Tell me about a product problem you worked on":
> "I conducted a PM case study on Nykaa Fashion. I identified that [pain point] was causing [key stat]. I researched this through [methods], built user personas, prioritised solutions using RICE, and proposed [feature name] with a North Star metric of [metric]. My expected outcome was [OKR]."

---

## 🛠️ Tech Stack

| Tool | Use |
|---|---|
| Streamlit | Dashboard framework |
| Plotly | RICE bar chart + metrics visualisation |
| Pandas | Data tables |
| Python | Everything |

---

## 📌 Author Notes

This project was built as a **real PM portfolio project** — not a tutorial clone. Every data point, persona, and RICE score is researched and grounded in real Indian fashion e-commerce context (Redseer 2023, app store reviews, competitive benchmarks).

> **Tip for interviews:** Select one pain point, go through all 7 steps, and write each section in your own words in the `/docs` folder. That becomes your actual case study document.

---

## 📜 License

MIT — free to use, fork, and build on.
