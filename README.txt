=============================================
CrewAI Teacher Chatbot with Web Search
=============================================

An advanced AI-powered educational chatbot utilizing **CrewAI** to provide structured, insightful, and real-time responses.  
This chatbot employs a **multi-agent system** to enhance learning experiences by **rewriting user questions into structured prompts**  
before passing them to an AI teacher. The chatbot also leverages **web search** for up-to-date information when required.

-----------------------------------
Application Overview
-----------------------------------
The chatbot consists of two intelligent **CrewAI agents**, each performing a specialized role:  

1️ **Question Rewriter Agent**  
   - Reformats user input into a structured **Chain-of-Thought (CoT)** prompt.  
   - Breaks down questions into **logical steps** for deeper understanding.  
   - Ensures the teacher agent receives **optimized queries** for better responses.  

2️ **Teacher Agent**  
   - Answers questions using **general knowledge and structured reasoning**.  
   - Utilizes **real-time web search** when needed to fetch the most accurate and updated information.  
   - Provides **clear, engaging, and well-explained responses** to enhance learning.  

-----------------------------------
Tasks & Execution Flow
-----------------------------------
The chatbot follows a **sequential process** using CrewAI:  

1. **User inputs a question.**  
2. The **Question Rewriter Agent** reformats it using Chain-of-Thought reasoning.  
3. The **Teacher Agent** receives the improved question and provides an answer.  
4. If the question requires **external knowledge**, the teacher agent performs a **web search** before responding.  
5. The final answer is returned to the user, maintaining conversation history.  

-----------------------------------
Integrated Tools
-----------------------------------
 **Serper.dev Web Search Tool**  
   - Allows the teacher agent to **search the internet** for real-time information.  
   - Used only when a query **requires external verification or recent updates**.  

