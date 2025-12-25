# AI Document Analyzer

A Streamlit-based web application that allows you to upload documents (PDF and TXT files) and ask questions about their content using AI models.

## Features

- **Document Upload**: Support for PDF and TXT files
- **Dual AI Backend**: Choose between offline (Ollama) and cloud-based (Gemini) AI models
- **Real-time Analysis**: Ask questions and get answers based on document content
- **Clean Interface**: User-friendly Streamlit web interface

## Supported File Types

- **PDF**: Uses PyPDF2 for text extraction
- **TXT**: Direct text file reading with UTF-8 encoding

## AI Models

### Ollama (Offline)
- Uses `tinyllama` model
- Runs locally on your machine
- Requires Ollama to be installed and running
- No internet connection needed after setup

### Gemini (Free Cloud)
- Uses Google's Gemini Flash model
- Free cloud-based API
- Requires GEMINI_API_KEY environment variable
- Internet connection required

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Install Dependencies
```bash
pip install streamlit PyPDF2 google-genai
```

### For Ollama Support (Optional)
1. Install Ollama: https://ollama.ai/
2. Pull the required model:
```bash
ollama pull tinyllama
```
3. Start Ollama service:
```bash
ollama serve
```

### For Gemini Support (Optional)
1. Get a free API key from Google AI Studio: https://makersuite.google.com/app/apikey
2. Set environment variable:
```bash
# Windows
set GEMINI_API_KEY=your_api_key_here

# Linux/Mac
export GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. Open your browser and go to `http://localhost:8501`

3. Upload a PDF or TXT file using the file uploader

4. Choose your preferred AI model:
   - **Ollama (Offline)**: For local processing without internet
   - **Gemini (Free Cloud)**: For cloud-based processing

5. Ask questions about your document in the text input field

6. Click "Analyze Document" to get AI-powered answers

## Project Structure

```
doc-analysier/
├── app.py              # Main application file
└── README.md           # This documentation
```

## Key Functions

- `extract_text_from_file()`: Extracts text from PDF and TXT files
- `ask_ollama()`: Processes questions using local Ollama model
- `ask_gemini()`: Processes questions using Google's Gemini API
- `main()`: Streamlit UI and application logic

## Limitations

- PDF extraction depends on document formatting and may not work for scanned images
- Ollama uses `tinyllama` model which has limited context window (3000 characters)
- Gemini API has rate limits for free tier
- Large documents may be truncated to fit model context limits

## Troubleshooting

### Common Issues

1. **PyPDF2 not installed**: Run `pip install PyPDF2`
2. **Ollama not found**: Install Ollama and ensure it's running
3. **GEMINI_API_KEY not found**: Set the environment variable correctly
4. **PDF text extraction fails**: Some PDFs may be image-based or have complex formatting

### Error Messages

- `"PyPDF2 not installed"`: Install the required dependency
- `"Ollama not found"`: Install and start Ollama service
- `"GEMINI_API_KEY not found"`: Set up your API key
- `"Unsupported file type"`: Use only PDF or TXT files

## Development

This project uses:
- **Streamlit**: Web framework for the UI
- **PyPDF2**: PDF text extraction
- **Google Generative AI**: Gemini API client
- **Subprocess**: For Ollama command-line interface
- **Pathlib**: File path handling

## License

This project is open source. Feel free to modify and distribute according to your needs.
