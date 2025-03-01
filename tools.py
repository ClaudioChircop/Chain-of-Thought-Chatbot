import os
from crewai_tools import SerperDevTool


# Set up Serper.dev API Key
os.environ["SERPER_API_KEY"] = ""

# 🔹 Define the Web Search Tool
web_search_tool = SerperDevTool()
