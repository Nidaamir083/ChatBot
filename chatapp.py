import os
import streamlit as st
import google.generativeai as genai

# --- Set up ---
st.set_page_config(page_title="Gemini-Powered Oncologist Chatbot", layout="centered")
st.title("🧬 Gemini-Powered AI Chatbot for Drug Repurposing (ATC)")

# --- Load API key from environment ---
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("🚫 API key not found. Please set GOOGLE_API_KEY as an environment variable.")
    st.stop()
else:
    genai.configure(api_key=api_key)

# --- Initialize model ---
model = genai.GenerativeModel("gemini-pro")

# --- Maintain chat history ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Input box ---
user_input = st.text_input("Ask a question about Anaplastic Thyroid Cancer (ATC), drug trials, or repurposing:")

# --- Generate response ---
if user_input:
    st.session_state.history.append(f"You: {user_input}")
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content("\n".join(st.session_state.history)).text
        except Exception as e:
            response = f"⚠️ Error: {str(e)}"
    st.session_state.history.append(f"Bot: {response}")
    st.write(response)

# --- Show history ---
if st.checkbox("Show full chat history"):
    st.markdown("### Chat History")
    for msg in st.session_state.history:
        st.text(msg)






   




   




