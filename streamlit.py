import streamlit as st
from app import get_teacher_response

# Initialize chat history in session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""  # Temporary storage for user input

def process_input():
    """Handles user input, reformats it using CoT, and updates chat history."""
    user_question = st.session_state.user_input.strip()

    if user_question:
        # 🔹 Get the chatbot's response
        response = get_teacher_response(user_question, st.session_state.conversation_history)

        # Clear the input field after processing
        st.session_state.user_input = ""

# Streamlit UI
st.title("Chain-of-Thought Teacher Chatbot")
st.write("Ask me anything, and I'll structure your question before answering!")

# Display chat history without refreshing the UI
chat_container = st.container()
with chat_container:
    for message in st.session_state.conversation_history:
        if message.startswith("You:"):
            st.markdown(f"**{message[4:]}**")
        elif message.startswith("🔄"):
            st.markdown(f"🔄 **{message[2:]}**")  # Show reformatted question
        else:
            st.markdown(f"**{message}**")

# User input field with callback
st.text_input("Type your message here:", key="user_input", on_change=process_input)
