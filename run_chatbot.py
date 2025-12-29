import json

def get_rag_response(user_query):
    # Load your student data from the local folder
    with open('data/students.json', 'r') as f:
        data = json.load(f)
    
    query = user_query.lower()
    
    # RAG Logic: Search the data based on the user's question
    if "highest" in query or "best" in query:
        top = max(data, key=lambda x: x['gpa'])
        return f"🤖 AI Analysis: The student with the highest GPA is {top['name']} ({top['gpa']})."
    
    if "rauf" in query:
        s = next(s for s in data if s['name'] == "Rauf")
        return f"🤖 AI Context Found: Rauf has a GPA of {s['gpa']} and grades: {s['grades']}."
    
    if "yusra" in query:
        s = next(s for s in data if s['name'] == "Yusra")
        return f"🤖 AI Context Found: Yusra has a GPA of {s['gpa']}. Note: {s['notes']}"

    return "🤖 AI: I am ready! Ask me about Rauf, Yusra, or the highest GPA."

if __name__ == "__main__":
    print("--- 🎓 LOCAL RAG CHATBOT IS LIVE ---")
    print("(Type 'exit' to stop)")
    while True:
        prompt = input("\nYou: ")
        if prompt.lower() in ['exit', 'quit']: break
        print(get_rag_response(prompt))