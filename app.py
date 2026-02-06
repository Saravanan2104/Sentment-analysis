import streamlit as st
from sentiment import analyze_sentiment

st.set_page_config(page_title="Sentiment Analyzer")

st.title("🧠 Sentiment Analysis Web App")
st.write("Enter a review below to analyze its sentiment")

review = st.text_area("User Review")

if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        result = analyze_sentiment(review)
        st.success(f"Sentiment: {result}")
