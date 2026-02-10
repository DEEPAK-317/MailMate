import smtplib
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(recipient, body):
    try:
        sender_email = os.getenv("SENDER_EMAIL") or st.secrets.get("SENDER_EMAIL")
        if not sender_email:
            st.error("SENDER_EMAIL is missing.")
            return False

        sender_password = os.getenv("EMAIL_PASSWORD") or st.secrets.get("EMAIL_PASSWORD")
        if not sender_password:
            st.error("EMAIL_PASSWORD is missing.")
            return False

        smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com") 
        if not os.getenv("SMTP_SERVER") and "SMTP_SERVER" in st.secrets:
             smtp_server = st.secrets.get("SMTP_SERVER")
        
        smtp_port = int(os.getenv("SMTP_PORT", 587))
        if not os.getenv("SMTP_PORT") and "SMTP_PORT" in st.secrets:
             smtp_port = int(st.secrets.get("SMTP_PORT"))

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = "Response To Your Email"

        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False