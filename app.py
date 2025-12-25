# -*- coding: utf-8 -*-

import streamlit as st
import subprocess
from pathlib import Path
import tempfile
from google import genai
import os


st.set_page_config(
    page_title="Document Analyzer",
    layout="wide"
)

# -----------------------------
# Document Text Extraction
# -----------------------------
def extract_text_from_file(file_path: Path) -> str:
    try:
        if file_path.suffix.lower() == ".txt":
            return file_path.read_text(encoding="utf-8", errors="ignore")

        elif file_path.suffix.lower() == ".pdf":
            try:
                import PyPDF2
            except ImportError:
                return "PyPDF2 not installed. Run: pip install PyPDF2"

            text = []
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text.append(page_text)

            return " ".join(text).strip()

        else:
            return "Unsupported file type."

    except Exception as e:
        return f"Error reading file: {e}"


# -----------------------------
# Ollama LLM Call (Offline)
# -----------------------------
def ask_ollama(question: str, context: str) -> str:
    context = context[:3000]

    prompt = (
        "You are a helpful AI assistant.\n\n"
        f"Document Content:\n{context}\n\n"
        f"Question:\n{question}\n\n"
        "Answer clearly based only on the document."
    )

    try:
        result = subprocess.run(
            ["ollama", "run", "tinyllama"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            return result.stderr.strip() or "Ollama execution failed."

        return result.stdout.strip()

    except FileNotFoundError:
        return "Ollama not found. Install and run Ollama."
    except subprocess.TimeoutExpired:
        return "Ollama request timed out."
    except Exception as e:
        return f"Ollama error: {e}"


# -----------------------------
# Gemini LLM Call (Free Cloud)
# -----------------------------
def ask_gemini(question: str, context: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "GEMINI_API_KEY not found in environment variables."

    try:
        client = genai.Client(api_key=api_key)

        prompt = (
            "Answer the question strictly using the document content.\n\n"
            f"Document:\n{context[:3000]}\n\n"
            f"Question:\n{question}"
        )

        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Gemini error: {e}"

# -----------------------------
# Streamlit UI
# -----------------------------
def main():
    st.title("📄 AI Document Analyzer")
    st.write("Upload a document and ask questions using AI.")

    model_choice = st.radio(
        "Choose AI Model",
        ["Ollama (Offline)", "Gemini (Free Cloud)"],
        horizontal=True
    )

    uploaded_file = st.file_uploader(
        "Upload PDF or TXT file",
        type=["pdf", "txt"]
    )

    if uploaded_file:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=Path(uploaded_file.name).suffix
        ) as tmp:
            tmp.write(uploaded_file.getbuffer())
            temp_path = Path(tmp.name)

        with st.spinner("Reading document..."):
            document_text = extract_text_from_file(temp_path)

        temp_path.unlink(missing_ok=True)

        if document_text and not document_text.lower().startswith("error"):
            st.success(f"Document loaded ({len(document_text)} characters)")

            question = st.text_input("Ask a question about the document")

            if st.button("Analyze Document") and question.strip():
                with st.spinner("Analyzing with AI..."):
                    if model_choice == "Ollama (Offline)":
                        answer = ask_ollama(question, document_text)
                    else:
                        answer = ask_gemini(question, document_text)

                st.markdown("### 🧠 Question")
                st.write(question)

                st.markdown("### ✅ Answer")
                st.write(answer)
        else:
            st.error(document_text)


if __name__ == "__main__":
    main()
