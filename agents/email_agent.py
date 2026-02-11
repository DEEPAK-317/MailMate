import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
import os
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("GEMINI_API_KEY not found in environment variables or secrets. Please add it.")
except Exception as e:
    st.error(f"Error configuring Gemini: {e}")

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating response with Gemini: {e}")
        return None