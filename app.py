# app.py - SentiVerse: Final Version with All Features

import streamlit as st
import random
import spacy
import plotly.express as px
import pandas as pd

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Page configuration
st.set_page_config(page_title="SentiVerse: Emotional Forecasting AI", layout="wide")

# --- Styling ---
st.markdown("""
    <style>
    .stButton>button {
        background-color: #6C63FF;
        color: white;
        font-weight: 600;
        padding: 0.6em 1.2em;
        border-radius: 8px;
    }
    .stRadio > div {
        flex-direction: row;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title & Description ---
st.title("🧠 SentiVerse: Emotional Forecasting AI")
st.markdown("An AI app that simulates society's emotional response to news and headlines. Unlock emotion-aware intelligence for policy, research, and communication.")

# --- Sample Headlines ---
sample_headlines = [
    "Government launches AI-based healthcare reforms",
    "Fuel price hike triggers protests in rural districts",
    "Education sector welcomes national mental health initiative",
    "AI-powered surveillance raises global privacy concerns"
]

selected = st.selectbox("Need inspiration? Choose a sample headline:", [""] + sample_headlines)

headline = st.text_input("Enter a news headline:", value=selected if selected else "")

# --- Functions ---
def simulate_emotional_forecast(headline):
    if len(headline.strip()) < 10:
        return "⚠️ Please enter a more descriptive headline."
    return (
        "🟢 **Cautious optimism** — society sees potential and progress.\n\n"
        "🟠 **Mild anxiety** — there's uncertainty about side effects.\n\n"
        "🔵 **Curiosity** — people are eager to see what unfolds."
    )

def generate_emotional_volatility_score():
    score = round(random.uniform(0.2, 0.9), 2)
    interpretation = (
        "🔹 Low volatility — public sentiment is stable." if score < 0.4 else
        "🟠 Moderate volatility — expect mixed reactions." if score < 0.7 else
        "🔺 High volatility — polarized or intense emotions likely."
    )
    return f"**Emotional Volatility Score (EVS): {score}**\n{interpretation}"

def generate_cognitive_alignment():
    return f"**Cognitive Alignment Prediction:** {random.choice(['🧠 Rational', '❤️ Emotional', '⚡ Impulsive'])}"

def extract_geography(text):
    text = text.lower()
    geo_map = {
        # India
        "modi": "India", "narendra modi": "India", "delhi": "India", "rupee": "India",

        # UAE & GCC
        "dirhams": "UAE", "emirati": "UAE", "dubai": "UAE", "abu dhabi": "UAE", "sheikh": "UAE",

        # USA
        "biden": "USA", "white house": "USA", "dollar": "USA", "washington": "USA",

        # UK & EU
        "pound": "UK", "london": "UK", "sunak": "UK", "brexit": "UK", "euro": "EU", "european union": "EU",

        # China
        "xi jinping": "China", "yuan": "China", "beijing": "China", "shanghai": "China",

        # Middle East
        "riyadh": "Saudi Arabia", "iran": "Iran", "qatar": "Qatar", "oman": "Oman",

        # Other major players
        "putin": "Russia", "moscow": "Russia", "zelenskyy": "Ukraine", "kyiv": "Ukraine",
        "tokyo": "Japan", "yen": "Japan", "seoul": "South Korea", "won": "South Korea",
        "canberra": "Australia", "australian dollar": "Australia", "canadian dollar": "Canada", "ottawa": "Canada",

        # Africa
        "nairobi": "Kenya", "lagos": "Nigeria", "cape town": "South Africa", "egypt": "Egypt"
    }
    for k in geo_map:
        if k in text:
            return geo_map[k]
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]:
            return ent.text
    return "Unknown Location"

def generate_suggestion_from_headline(headline_text):
    headline_text = headline_text.lower()
    if any(word in headline_text for word in ["crisis", "hike", "protest", "unrest"]):
        return (
            "🔧 **Suggested Actions:**\n"
            "- Launch transparent communication campaigns\n"
            "- Address root causes with empathy\n"
            "- Offer immediate support to affected groups"
        )
    elif any(word in headline_text for word in ["reform", "success", "growth", "initiative"]):
        return (
            "🚀 **Enhancement Ideas:**\n"
            "- Scale the initiative with feedback loops\n"
            "- Replicate in other sectors\n"
            "- Showcase success stories to increase trust"
        )
    else:
        return (
            "🧭 **General Strategic Suggestion:**\n"
            "- Track public sentiment continuously\n"
            "- Ensure transparent messaging\n"
            "- Promote open dialogue with stakeholders"
        )

def generate_emotion_data():
    return pd.DataFrame({
        "Emotion": ["Optimism", "Anxiety", "Curiosity"],
        "Intensity": [0.6, 0.4, 0.5]
    })

# --- Forecasting ---
if st.button("📡 Forecast Emotional Futures"):
    with st.spinner("Analyzing headline..."):
        forecast = simulate_emotional_forecast(headline)
        st.markdown("### 🔍 Emotional Forecast")
        st.markdown(forecast)

        # EVS + Alignment + Geo
        st.markdown(generate_emotional_volatility_score())
        st.markdown(generate_cognitive_alignment())
        st.markdown("**Geographic Focus:** " + extract_geography(headline))

        # Stakeholder Insight
        user_type = st.selectbox("### 👥 Who are you?", ["Student", "Teacher", "Government/Policymaker", "Corporate Professional", "Researcher", "General Public"])
        insights = {
            "Student": "This helps build emotional awareness for social and academic issues.",
            "Teacher": "Useful for discussing real-world events and student engagement.",
            "Government/Policymaker": "Track sentiment to guide policy communication.",
            "Corporate Professional": "Forecast consumer/employer sentiment to reduce risk.",
            "Researcher": "Study public emotion dynamics tied to real-world events.",
            "General Public": "Get emotionally informed and context-aware."
        }
        st.info(f"**Stakeholder Insight:** {insights[user_type]}")

        # Strategic Suggestion
        st.markdown("### 🧩 Strategic Suggestions")
        st.success(generate_suggestion_from_headline(headline))

        # Emotional Heatmap
        st.markdown("### 🌡️ Emotional Heatmap")
        fig = px.bar(generate_emotion_data(), x="Emotion", y="Intensity", color="Emotion")
        st.plotly_chart(fig)

# --- EI Trainer ---
with st.expander("📚 Emotional Intelligence Trainer"):
    st.markdown("Learn how to interpret and respond to emotional dynamics in society.")
    st.markdown("**Scenario:** A controversial law triggers mixed emotional reactions.")
    response = st.radio("What is the most emotionally intelligent action?", [
        "Ignore the emotional response",
        "Offer an official emotional validation statement",
        "Escalate the law enforcement",
    ])
    if response:
        st.success("Great choice! Acknowledging emotion builds trust and clarity.")