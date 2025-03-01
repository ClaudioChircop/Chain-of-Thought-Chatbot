from crewai import Agent
from tools import web_search_tool  # Import the web search tool

# 🔹 Question Rewriter Agent (Same as before)
question_rewriter = Agent(
    role="Question Rewriter",
    goal="Reformat user questions into a structured Chain-of-Thought prompt.",
    backstory=(
        "You are skilled in transforming simple questions into well-structured, "
        "step-by-step Chain-of-Thought (CoT) reasoning formats. "
    ),
    verbose=True,
    memory=True
)

# 🔹 Teacher Agent (With Internet Access)
teacher_agent = Agent(
    role="Friendly Teacher",
    goal="Provide clear and engaging explanations using available knowledge and real-time web search when necessary.",
    backstory=(
        "You are a passionate educator skilled at explaining complex topics in a simple way. "
        "When a question requires external knowledge, you use web search to gather the most relevant and accurate information."
    ),
    verbose=True,
    memory=True,
    tools=[web_search_tool] 
)
