# 🎓 Student AI RAG Assistant - Phase 1

## 👤 Developer: Furqun Ali
**Project Goal:** To build a functional AI assistant that retrieves student performance data from a local knowledge base using RAG architecture.

---

## 🚀 How it Works (RAG Logic)
This project implements a **Retrieval-Augmented Generation** flow:
1.  **Knowledge Base**: Student records are stored in `data/students.json`.
2.  **Retrieval**: The Python engine (`run_chatbot.py`) searches the JSON for specific names or IDs.
3.  **Augmentation**: The script pulls the GPA and teacher notes to provide context.
4.  **Generation**: The AI (simulated locally or via Claude) generates a response based on that retrieved data.

---

## 🛠️ Features
- **Instant GPA Retrieval**: Quickly find top-performing students.
- **Performance Notes**: Get AI-generated summaries of student strengths and weaknesses.
- **Local Execution**: Runs entirely in the terminal for fast testing.

## 📦 Tech Stack
- **Language**: Python 3.11
- **Data Format**: JSON
- **Version Control**: Git & GitHub

## 🚦 How to Run
1. Clone the repository.
2. Ensure you have Python installed.
3. Run the command: `python run_chatbot.py`
