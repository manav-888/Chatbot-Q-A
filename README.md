# Chatbot Q/A![ChatBot With Google API](https://github.com/manav-888/Chatbot-Q-A/assets/28830098/b50a55ef-5fa4-4ddf-9abd-1a545bcae761)


# Building a Chatbot by using Google API and Hugging Face model

This project enables you to build a  RAG based chatbot that answers customer queries using website data . The chatbot utilizes Google Gemini pro and Hugging face Model to answer user questions based on the content of a specified website or query.

## Setup Instructions

Follow these steps to set up the project on your local machine:

1. **Clone the Repository:**
   ```
   git clone https://github.com/manav-888/Chatbot-Q-A.git
   ```

2. **Create a Virtual Environment:**

   Note: We used Python 3.10.11 to create the virtual environment. Please ensure that you use the same Python version to avoid potential conflicts and ensure compatibility with the project dependencies.
   ```
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment:**
   ```
   . venv/bin/activate
   ```

5. **Install Requirements:**
   ```
   pip install -r requirements.txt
   ```
    **  or: ** 

   ```
   pip install streamlit transformers google-generativeai python-dotenv torch torchvision torchaudio

   ```

6. ** Create .env  file   in same directory  and Configure GOOGLE API KEY  :**
   ```
    GOOGLE_API_KEY=" Insert Your KEY "
   
   ```


   **  or: ** 

   ** To run without Google API key  then hit submit query button with Hugging face model **




8. **  Run a app.py file in terminal **
   ```
   streamlit run app.py
   
   ```
   
  
