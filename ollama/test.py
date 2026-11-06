import ollama

print("Connecting to Ollama...")

reply = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Give me 3 fun facts about space"
        }
    ]
)

print(reply["message"]["content"])