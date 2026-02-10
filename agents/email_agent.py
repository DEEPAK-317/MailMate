import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("GEMINI_API_KEY not found in secrets. Please add it.")
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
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating response with Gemini: {e}")
        return None