from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load environment variables
load_dotenv()


# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


# Function to load Hugging Face model and get responses
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def get_huggingface_response(question):
    input_ids = tokenizer.encode(question, return_tensors="pt")
    output = model.generate(input_ids, max_length=50, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response



# Initialize Streamlit app
st.set_page_config(page_title="Chatbot models")
st.header("Chatbot")


with st.sidebar:
    st.header("Settings")
    st.info("Enter your Google API key")
    api_key1 = st.text_input("Google API Key")
    st.sidebar.markdown("[ Get an API Key ](https://aistudio.google.com/app/apikey)")
    st.sidebar.markdown("For better Response use Google Models")

# Configure generative AI with the API key
genai.configure(api_key=api_key1)


# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input field and submit button
input_text = st.text_input("Input URL / Query :", key="input")

col1, col2 = st.columns([5, 3])
with col1:
    submit_button1 = st.button("Submit your query with Google API")
with col2:
    st.markdown(" (work with API Key)")


col3, col4 = st.columns([5,3])
with col3:
    submit_button2 = st.button("Submit your query with Hugging Face model")
with col4:
     st.markdown(" (free version)  ")



# Process user input and generate response1 from google model
if submit_button1 and input_text:
    response1 = get_gemini_response(input_text)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("Human", input_text))  # Human message
    st.subheader("The Response is")
    for chunk in response1:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("AI", chunk.text))  # AI response


# Process user input and generate response2 from hugging face model 
if submit_button2 and input_text:
    response2 = get_huggingface_response(input_text)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("Human", input_text))  # Human message
    st.subheader("The Response is")
    st.write(response2)
    st.session_state['chat_history'].append(("AI", response2))  # AI response



# Display chat history
st.subheader("The Chat History is")
for message_type, content in st.session_state['chat_history']:
    if message_type == "Human":
        with st.chat_message("Human"):
            st.write(content)
    elif message_type == "AI":
        with st.chat_message("AI"):
            st.write(content)
