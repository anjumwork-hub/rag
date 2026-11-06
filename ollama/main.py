# Install Python once:  winget install Python.Python.3.12
# Then:                 py -m pip install ollama
import ollama

reply = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "Give me 3 fun facts about space"}],
)
print(reply["message"]["content"])
