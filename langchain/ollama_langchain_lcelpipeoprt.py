"""08 · LCEL & the Pipe Operator

Run (with the venv active):  python main.py
Needs OPENAI_API_KEY in a .env file (see ../.env.example).
"""

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()
prompt = ChatPromptTemplate.from_template("Explain {topic} to a 10-year-old in 2 lines.")
llm = ChatOllama(model="llama3.2", temperature=0)

chain = prompt | llm | StrOutputParser()

print(chain.invoke({"topic": "gravity"}))
print(chain.batch([{"topic": "rain"}, {"topic": "magnets"}]))
chain.get_graph().print_ascii()
