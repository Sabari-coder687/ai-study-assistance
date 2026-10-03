import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Study Assistant")
st.write("Ask any study question and get an AI-generated explanation.")

api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

question = st.text_area(
    "Enter your question:",
    placeholder="Example: Explain Artificial Intelligence in simple words."
)

if st.button("Generate Answer 🚀"):
    if question.strip():
        with st.spinner("Generating answer..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=question
                )

                st.subheader("AI Answer")
                st.write(response.text)

            except Exception as e:
                st.error("An error occurred.")
                st.write(str(e))

    else:
        st.warning("Please enter a question.")
