# 📧 MailMate – Think Less, Send Smart

MailMate is an intelligent email assistant powered by Google's Gemini AI. It helps you generate professional, friendly, apologetic, or persuasive email responses instantly and sends them directly to the recipient.

## 🚀 Features

- **AI-Powered Responses**: Uses Google's Gemini model (`gemini-2.5-flash`) to craft high-quality email replies.
- **Tone Selection**: Choose from multiple tones to match the context:
  - 👔 Professional
  - 😊 Friendly
  - 🙏 Apologetic
  - 🗣️ Persuasive
- **Instant Sending**: Seamlessly integrates with SMTP (e.g., Gmail) to send the generated email directly from the app.
- **User-Friendly Interface**: Built with [Streamlit](https://streamlit.io/) for a clean and simple experience.

## 🛠️ Tech Stack

- **Python** (Core Logic)
- **Streamlit** (Frontend)
- **Google Generative AI** (LLM for generating content)
- **SMTP** (Email Dispatch)

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/DEEPAK-317/MailMate.git
    cd MailMate
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add the following credentials:
    ```env
    GEMINI_API_KEY=your_google_gemini_api_key
    SENDER_EMAIL=your_email@gmail.com
    EMAIL_PASSWORD=your_email_app_password
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587
    ```
    *(Note: For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.)*

## ▶️ Usage

1.  **Run the application:**
    ```bash
    streamlit run main.py
    ```

2.  **Open your browser:**
    The app should automatically open at `http://localhost:8501`.

3.  **Generate & Send:**
    - Paste the email you received.
    - Enter the recipient's email address.
    - Select your desired tone.
    - Click **Generate & Send Email**.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License.
