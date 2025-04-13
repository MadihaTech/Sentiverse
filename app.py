import streamlit as st
import random
import plotly.graph_objects as go
from groq import Groq

# Set page layout
st.set_page_config(page_title="SentiVerse: Emotional Forecasting AI", layout="wide")

# Emoji theme + title
st.markdown("<h1 style='text-align: center;'>🤖 SentiVerse: Emotional Forecasting AI</h1>", unsafe_allow_html=True)

# Groq API setup
client = Groq(api_key=st.secrets["groq_api_key"])

def generate_emotions_from_groq(headline):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are an expert in emotional forecasting and human-centered AI. Your job is to simulate emotional responses of the general public to various news headlines."},
                {"role": "user", "content": f"Given the headline: '{headline}', generate:\n1. Three predicted emotional responses (e.g., optimism, fear, curiosity), each with 1-line explanation.\n2. An Emotional Volatility Score between 0 and 1.\n3. Cognitive alignment type (Analytical, Reflective, Impulsive, etc.)."}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# Puzzle unlock gate
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    st.subheader("🔐 Solve this to unlock the emotional intelligence of SentiVerse")
    user_input = st.text_input("What comes once in a minute, twice in a moment, but never in a thousand years?")
    if st.button("Submit"):
        if user_input.strip().lower() == "m":
            st.success("That's correct! Welcome to SentiVerse.")
            st.session_state.unlocked = True
            st.rerun()
        else:
            st.error("Oops! Try again.")
    st.stop()

# Input headline
sample = "Fuel prices rise sharply across the country"
st.markdown("#### Try this: `Fuel prices rise sharply across the country`")
headline = st.text_input("Enter a news headline:", key="headline")

# Stakeholder selection
stakeholder = st.radio("Who are you?", ["Student", "Teacher", "Government", "Corporate", "Researcher", "Public"], horizontal=True)

# Emotional forecast
if st.button("Forecast Emotional Futures") and headline:
    gpt_output = generate_emotions_from_groq(headline)

    st.subheader("🧠 Simulated Emotional Futures")
    st.markdown(gpt_output)

    # Just for fun: Fake pie chart for visuals
    emotions = ["Optimism", "Anxiety", "Curiosity"]
    fig = go.Figure(data=[
        go.Pie(labels=emotions, values=[30, 40, 30], hole=0.3,
               marker=dict(colors=["#FFD700", "#FFA07A", "#87CEFA"]))
    ])
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), width=600, height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Strategic suggestions
    st.subheader("📊 Strategic Suggestions")
    st.markdown("- Maintain transparency")
    st.markdown("- Monitor sentiment over time")
    st.markdown("- Facilitate dialogue among stakeholders")

    # Stakeholder insight
    st.subheader("🧩 Stakeholder Insight")
    messages = {
        "Student": "This insight helps align emotional context for student-centric strategy.",
        "Teacher": "Align educational content with emotional awareness.",
        "Government": "Refine policy messaging and anticipate public response.",
        "Corporate": "Adjust marketing or workplace initiatives to fit emotional climate.",
        "Researcher": "Study emotional impact trends to inform future models.",
        "Public": "Understand the emotional climate to better engage with societal shifts."
    }
    st.info(messages.get(stakeholder, "This tool supports emotionally informed decisions."))

# Emotional Intelligence Trainer
st.subheader("🧠 Emotional Intelligence Trainer")
st.markdown("**Scenario:** A controversial policy is causing mixed emotional reactions.")
trainer_option = st.radio("Choose the most emotionally intelligent response:", [
    "Ignore public sentiment",
    "Offer a validation statement acknowledging emotion",
    "Enforce the policy strictly"
], key="trainer")

if trainer_option:
    if trainer_option == "Offer a validation statement acknowledging emotion":
        st.success("Great choice! Acknowledging emotion builds trust and clarity.")
    else:
        st.warning("Consider acknowledging people's emotions to reduce resistance.")

# Footer
st.markdown("---\n©2025 **SentiVerse** | Built with GPT, Streamlit, spaCy & Plotly - #AIforSociety")
