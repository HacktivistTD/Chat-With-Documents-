import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Google API
genai.configure(api_key=api_key)

def generate_response(prompt):
    """Generate a response from the Google Gemini API."""
    try:
        response = genai.generate_text(
            prompt=prompt,
            model="models/your-correct-model-name",  # Replace with actual model name
            temperature=0.5
        )
        return response['generated_text']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.set_page_config(page_title="Simple Chat Bot", layout="wide")
    st.header("Simple Chat Bot using Google Gemini Pro 💬")

    # Text input for user query
    user_input = st.text_input("You: ", "")
    
    if user_input:
        # Generate response
        response = generate_response(user_input)
        st.write(f"Bot: {response}")

if __name__ == "__main__":
    main()
