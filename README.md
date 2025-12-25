# 📄 AI Document Analyzer

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-orange?logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

**AI-powered Document Analysis Web Application**  
Leverage the power of Large Language Models (LLMs) to instantly extract insights and answer questions from PDF and TXT documents.

---

## 🚀 Overview

The **AI Document Analyzer** is a **Streamlit-based web app** that allows users to upload documents and interact with their content using **cutting-edge AI models**.  
Whether you want to analyze reports, research papers, or any text-based content, this tool provides **real-time, context-aware answers**.

---

## ✨ Features

- **📂 Universal Document Upload** – Supports PDF and TXT formats  
- **🤖 Dual AI Backend** –  
  - **Ollama (Offline)**: Run locally without internet  
  - **Gemini (Free Cloud)**: Google cloud-based AI  
- **⚡ Real-time AI Analysis** – Ask questions and get instant answers  
- **🖥 User-Friendly Interface** – Clean, intuitive Streamlit UI  
- **🔒 Safe and Lightweight** – Minimal setup, optional cloud use  

---

## 📄 Supported File Types

| File Type | Extraction Method |
|-----------|-----------------|
| PDF       | PyPDF2 library for structured text extraction |
| TXT       | Direct UTF-8 file reading |

> ⚠️ Note: Scanned or image-based PDFs may not extract text correctly.

---

## 🤖 AI Models

### 1️⃣ Ollama (Offline)
- Runs locally on your machine  
- Uses the `tinyllama` model  
- Works **without internet** once installed  
- Requires Ollama service running  

### 2️⃣ Gemini (Free Cloud)
- Uses **Google Gemini Flash model** (`gemini-flash-latest`)  
- Requires internet connection  
- Requires **GEMINI_API_KEY** environment variable  
- Free-tier friendly and stable for small/medium documents  

---

## 🛠 Installation

### Prerequisites
- Python **3.7+**
- `pip` package manager

### Install Dependencies
```bash
pip install streamlit PyPDF2 google-genai
```

### Optional: Ollama Setup
Install Ollama: https://ollama.ai/

Pull the required model:
```bash
ollama pull tinyllama
```

Start Ollama service:
```bash
ollama serve
```

### Optional: Gemini Setup
Get a free API key: https://makersuite.google.com/app/apikey

Set environment variable:
```bash
# Windows
set GEMINI_API_KEY=your_api_key_here

# Linux/Mac
export GEMINI_API_KEY=your_api_key_here
```

---

## 💡 Usage

Start the app:
```bash
streamlit run app.py
```

Open browser at http://localhost:8501

1. Upload PDF or TXT document
2. Select AI backend:
   - **Ollama (Offline)** → Local processing
   - **Gemini (Free Cloud)** → Cloud-based processing
3. Enter your question about the document
4. Click **Analyze Document** to get AI-powered answers

---

## 🏗 Project Structure
```bash
doc-analysier/
├── app.py              # Main Streamlit app
├── README.md           # Documentation
└── .git/               # Git repository files
```

---

## 🔑 Core Functions

| Function | Description |
|----------|-------------|
| `extract_text_from_file()` | Extract text from PDF/TXT |
| `ask_ollama()` | Query local Ollama LLM |
| `ask_gemini()` | Query Google Gemini API |
| `main()` | Handles Streamlit UI and workflow |

---

## ⚠️ Limitations

- PDF extraction may fail on scanned or image-based documents
- Ollama tinyllama model has ~3000 character context limit
- Gemini API has free-tier rate limits
- Very large documents may need truncation

---

## 🛠 Troubleshooting

| Issue | Solution |
|-------|----------|
| "PyPDF2 not installed" | Run `pip install PyPDF2` |
| "Ollama not found" | Install Ollama and start the service |
| "GEMINI_API_KEY not found" | Set environment variable correctly |
| "Unsupported file type" | Upload PDF or TXT only |
| "PDF text extraction fails" | Check if PDF is image-based or complex |

---

## 🏗 Development Stack

- **Python & Streamlit** → UI framework
- **PyPDF2** → PDF text extraction
- **google-genai** → Gemini cloud AI integration
- **Subprocess** → Ollama CLI interaction
- **Pathlib & Tempfile** → File management

---

## 📝 Future Enhancements

- Retrieval-Augmented Generation (RAG) with vector embeddings
- Multi-document support
- Summarization and highlighting
- Chat-like interface for document Q&A

---

## 📜 License

MIT License – Open source and free to use, modify, and redistribute.
