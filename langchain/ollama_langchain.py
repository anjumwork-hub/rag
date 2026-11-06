from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import os

# Load environment variables
load_dotenv()

# Initialize Ollama
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

# Ask a question
question = "Explain Python in one sentence."

# Get response
response = llm.invoke(question)

# Print results
print("Answer:", response.content)
print("Type:", type(response).__name__)
print("Tokens:", response.usage_metadata)