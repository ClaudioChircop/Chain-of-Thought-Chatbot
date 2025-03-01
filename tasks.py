from crewai import Task
from agents import question_rewriter, teacher_agent
from tools import web_search_tool  # Import the web search tool

def create_rewrite_task(user_question):
    """Task for reformatting the user's input into Chain-of-Thought structure."""
    return Task(
        description=(
            "Your task is to take the following user question and rewrite it using Chain-of-Thought reasoning. "
            "Break the question down into structured logical steps to ensure clarity.\n\n"
            f"### **User's Original Question:**\n{user_question}\n\n"
            "### **Expected Reformatted Output:**\n"
            "1️⃣ **Understanding the question:** Explain what the student is really asking.\n"
            "2️⃣ **Breaking it down:** Identify the key concepts involved.\n"
            "3️⃣ **Logical steps:** Outline how the answer should be structured step by step.\n"
            "4️⃣ **Final refined question:** Rewrite the question so that it encourages deep reasoning."
        ),
        expected_output="A structured Chain-of-Thought reformulation of the original question.",
        agent=question_rewriter
    )

def create_teacher_task(reformatted_question):
    """Task for answering the reformulated Chain-of-Thought question using internet search when needed."""
    return Task(
        description=(
            "You have received a well-structured Chain-of-Thought question. "
            "Provide a clear, engaging, and well-explained response.\n\n"
            "### **Rewritten Question:**\n"
            f"{reformatted_question}\n\n"
            "🔹 **If the answer requires external knowledge, use web search to find relevant and up-to-date information.** "
            "Only use search when the question requires factual accuracy beyond general knowledge."
        ),
        expected_output="A clear and informative answer, enriched with web search results if necessary.",
        agent=teacher_agent,
        tools=[web_search_tool]  
    )
