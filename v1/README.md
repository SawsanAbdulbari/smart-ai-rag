# Smart AI (RAG) – Retrieval-Augmented Generation

This project is an interactive Gradio application that combines document understanding with open-source Large Language Models (LLMs) using the Retrieval-Augmented Generation (RAG) approach.

## Features
- 📄 Process and chunk PDF documents
- 🧠 Generate embeddings for semantic search
- 🔎 Use FAISS for fast vector similarity retrieval
- 🤖 Prompt LLMs with retrieved context for:
  - Question Answering
  - Summarization
  - Translation (to Finnish)

## Tech Stack
- Sentence Transformers (embeddings)
- FAISS (vector search)
- Transformers (LLM)
- Gradio (UI)
- PyPDF (PDF parsing)

## Setup
1. Clone this repo and `cd` into the directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Authenticate with Hugging Face for model downloads:
   ```bash
   huggingface-cli login
   ```
4. Run the app:
   ```bash
   python -m notebook
   # or open Final_Project_Smart_AI_(RAG).ipynb in Jupyter/Colab
   ```

## Usage
- Upload a PDF, select a task (Q&A, Summarize, Translate), and enter a query if needed.
- The app uses semantic search and an LLM to generate responses based on your document.

## Notes
- For best results, use a GPU.
- You may need a Hugging Face account/token for some models.

---
 