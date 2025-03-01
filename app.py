import os
from crewai import Crew, Process
from agents import question_rewriter, teacher_agent
from tasks import create_rewrite_task, create_teacher_task

# Set up API Key
os.environ["OPENAI_API_KEY"] = ""

# Initialize Crew
chatbot_crew = Crew(
    agents=[question_rewriter, teacher_agent],
    process=Process.sequential  # Ensures question rewriter runs before teacher agent
)

def get_teacher_response(user_question, conversation_history):
    """Processes user input by rewriting the question and getting a structured answer."""
    
    # 🔹 Step 1: Rewrite the user's question into a Chain-of-Thought format
    rewrite_task = create_rewrite_task(user_question)
    chatbot_crew.tasks = [rewrite_task]
    reformatted_question = chatbot_crew.kickoff(inputs={})

    # 🔹 Step 2: Use the improved question to get an answer (using web search if needed)
    teacher_task = create_teacher_task(reformatted_question)
    chatbot_crew.tasks = [teacher_task]
    response = chatbot_crew.kickoff(inputs={})

    # Append conversation history
    conversation_history.append(f"You: {user_question}")
    conversation_history.append(f"🔄 Reformatted Question: {reformatted_question}")
    conversation_history.append(f"Teacher Bot: {response}")

    return response

if __name__ == "__main__":
    print("\nFriendly Teacher Bot: Hello! What would you like to learn today? (Type 'exit' to quit)")

    conversation_history = []  # Store conversation history for multi-turn chat

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Friendly Teacher Bot: It was great chatting! Keep learning! ")
            break
        
        response = get_teacher_response(user_input, conversation_history)

        # Display full conversation history
        print("\n🔄 Reformatted Question:", conversation_history[-2])  # Last reformatted question
        print("\n👩‍🏫 Friendly Teacher Bot:", response)

