# Chatbot Q/A
![Screenshot 2024-06-01 at 3 29 49 PM](https://github.com/manav-888/manav-wasserstoff-AiTask/assets/28830098/39bb57ea-bbbe-433a-ae81-a9b74596e4dc)

# Building a Chatbot by using Google API and Hugging Face model

This project enables you to build a  RAG based chatbot that answers customer queries using website data . The chatbot utilizes Google Gemini pro and Hugging face Model to answer user questions based on the content of a specified website or query.

## Setup Instructions

Follow these steps to set up the project on your local machine:

1. **Clone the Repository:**
   ```
   git clone https://github.com/manav-888/manav-wasserstoff-AiTask.git
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
![change_API](https://github.com/manav-888/manav-wasserstoff-AiTask/assets/28830098/1163fab6-7e03-4ade-81c7-c72ad8d0e700)

   **  or: ** 

   ** To run without Google API key  then hit submit query button with Hugging face model **

![Screenshot 2024-06-01 at 3 31 42 PM](https://github.com/manav-888/manav-wasserstoff-AiTask/assets/28830098/f8e9ddc0-8023-4bcd-9ada-3b7b34cea4bc)


8. **  Run a app.py file in terminal **
   ```
   streamlit run app.py
   
   ```
   
  
