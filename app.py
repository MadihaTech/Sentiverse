import streamlit as st
import time

# MOCK FUNCTION for emotional forecasting (replace with real API later)
def get_emotional_forecast(headline):
    # Simulate processing delay
    time.sleep(1)

    # Normalize and check for minimal length or vague input
    clean_input = headline.strip().lower()
    if len(clean_input) < 15 or clean_input in ["ai", "hello", "yes", "no", "hi", "ok", "AI is here"]:
        return "Please provide a more descriptive and news-like headline to simulate emotional responses."

    # Simulated emotional forecasts (Replace this with GPT/LLM integration later)
    return (
        f"**Cautious optimism** over potential positive outcomes.\n\n"
        f"**Mild anxiety** about possible unintended consequences.\n\n"
        f"**Curiosity** about how events might unfold."
    )

# Streamlit UI setup
st.set_page_config(page_title="SentiVerse", layout="centered")

st.title("SentiVerse: Emotional Forecasting AI")
st.markdown(
    "This app simulates emotional futures based on real-world headlines. "
    "Enter a headline below to see how society might emotionally respond."
)

# User input
headline = st.text_input("Enter a news headline:")

# Forecast button
if st.button("Forecast Emotional Futures"):
    with st.spinner("Simulating emotional forecast..."):
        try:
            forecast = get_emotional_forecast(headline)
            st.markdown("---")
            st.subheader("Simulated Emotional Futures based on the headline:")
            st.markdown(forecast)
        except Exception as e:
            st.error("Oops! Something went wrong while generating the forecast. Please try again.")