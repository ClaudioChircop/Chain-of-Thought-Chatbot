import os
from crewai_tools import SerperDevTool


# Set up Serper.dev API Key
os.environ["SERPER_API_KEY"] = "f1ae638bfb2f9a1972c55518c5a8ae99f1a01610"

# 🔹 Define the Web Search Tool
web_search_tool = SerperDevTool()
