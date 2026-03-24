# 🩺 MedDoc Flow - Medical Document Assistant

**Your Intelligent Medical Document Assistant powered by AI and RAG**

MedDoc Flow is a sophisticated Streamlit application that enables healthcare professionals and researchers to interact intelligently with medical documents using advanced AI technology and **Retrieval-Augmented Generation (RAG)**. Upload your medical PDFs and get instant, contextual answers through our conversational interface.

## ✨ Features

- 📄 **Multi-Document Processing**: Upload and process multiple medical PDF documents simultaneously
- 🤖 **AI-Powered Chat Interface**: Ask questions about your documents using natural language
- 🔍 **Semantic Search**: Advanced document retrieval using FAISS vector embeddings
- 💬 **Interactive UI**: Clean, medical-themed interface with real-time chat experience
- 🧠 **RAG-Powered Responses**: Uses Retrieval-Augmented Generation to ground AI answers in your uploaded documents
- ⚡ **Fast Processing**: Efficient text chunking and vector indexing for quick responses
- 📱 **Responsive Design**: Works seamlessly across different screen sizes

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Karanpratap7/MedDoc-Flow.git
   cd MedDoc-Flow
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirments.txt
   ```

3. **Set up your API key**
   - Create or update `app/config.py` with your Euri AI API key:
   ```python
   EURI_API_KEY = "your_api_key_here"
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

5. **Open your browser**
   - Navigate to `http://localhost:8501`
   - Start uploading your medical documents!

## 📖 Usage

### 1. Upload Documents
- Use the sidebar to upload one or more PDF documents
- Supported formats: PDF files containing medical text

### 2. Process Documents
- Click "⚙️ Process Documents" to analyze and index your files
- The system will extract text and create searchable embeddings

### 3. Start Chatting
- Use the chat interface to ask questions about your documents
- Examples:
  - "What are the main symptoms described in patient 1?"
  - "Summarize the treatment recommendations"
  - "What medications were prescribed?"

### 4. Get AI Responses
- Receive contextual answers based on your uploaded documents
- The AI will clearly indicate if information is not available in your documents

## 🏗️ Project Structure

```
MedDoc-Flow/
├── main.py                 # Main Streamlit application
├── app/
│   ├── __init__.py        # Package initialization
│   ├── ui.py              # User interface components
│   ├── pdf_utils.py       # PDF text extraction utilities
│   ├── vectorstore_utils.py # Vector database operations
│   ├── chat_utils.py      # AI chat model interactions
│   └── config.py          # Configuration settings
├── test_patient_records/   # Sample test documents
├── requirments.txt        # Python dependencies
└── README.md              # This file
```

## 🧠 RAG Architecture

Yes — **MedDoc Flow is built on RAG (Retrieval-Augmented Generation)**.

Instead of relying solely on the LLM's training data, the application retrieves relevant passages directly from your uploaded documents and provides them as context to the language model, resulting in accurate, document-grounded answers.

### How the RAG Pipeline Works

```
PDF Upload
    │
    ▼
Text Extraction (PyPDF)
    │
    ▼
Text Chunking (RecursiveCharacterTextSplitter, chunk_size=1000, overlap=200)
    │
    ▼
Embedding Generation (HuggingFace sentence-transformers/all-mpnet-base-v2)
    │
    ▼
Vector Indexing (FAISS)
    │
    ▼ (at query time)
User Question ──► Semantic Similarity Search (top-3 chunks retrieved)
                              │
                              ▼
               Context Injection into LLM Prompt
                              │
                              ▼
               Euri AI LLM (gpt-4.1-nano) Generates Answer
                              │
                              ▼
                   Response Displayed in Chat UI
```

### RAG Components

| Component | Technology | Role |
|-----------|-----------|------|
| **Document Loader** | PyPDF | Extracts raw text from uploaded PDFs |
| **Text Splitter** | LangChain `RecursiveCharacterTextSplitter` | Splits text into overlapping chunks for retrieval |
| **Embedding Model** | `sentence-transformers/all-mpnet-base-v2` | Converts text chunks and queries into dense vectors |
| **Vector Store** | FAISS (faiss-cpu) | Stores embeddings and performs fast similarity search |
| **Retriever** | FAISS `similarity_search` (k=3) | Retrieves the 3 most relevant chunks for each query |
| **LLM** | Euri AI `gpt-4.1-nano` | Generates answers grounded in the retrieved context |

## 🔧 Configuration

### API Configuration
The application requires an Euri AI API key. Configure it in `app/config.py`:

```python
EURI_API_KEY = "your_euri_ai_api_key"
```

### Customization Options
- **Chunk Size**: Modify `chunk_size` in `main.py` for different text processing granularity
- **Model Settings**: Update embedding models in `vectorstore_utils.py`
- **UI Theme**: Customize colors and styling in the CSS section of `main.py`

## 🧪 Testing

The project includes sample medical documents in the `test_patient_records/` directory for testing purposes. These files contain mock patient data for demonstration.

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **AI/ML**:
  - **RAG Pipeline**: LangChain orchestrates retrieval and generation
  - FAISS for vector similarity search (retrieval)
  - HuggingFace embeddings (sentence-transformers) for vectorisation
  - Euri AI for LLM chat completions (generation)
- **Document Processing**: PyPDF for PDF text extraction
- **Backend**: Python 3.8+

## 📊 Dependencies

Key dependencies include:
- `streamlit` - Web application framework
- `pypdf` - PDF text extraction
- `langchain` - AI application framework
- `langchain_community` - Community integrations
- `faiss-cpu` - Vector similarity search
- `sentence_transformers` - Text embeddings
- `euriai` - AI model access

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m "Add your feature description"
   ```
5. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Test your changes with sample documents
- Update documentation as needed

## ⚠️ Disclaimer

**Important**: This application is designed for educational and research purposes. Always consult with qualified healthcare professionals for medical decisions. Do not use this tool as a substitute for professional medical advice, diagnosis, or treatment.

## 🆘 Support

If you encounter any issues:

1. **Check the Issues**: Browse existing [GitHub Issues](https://github.com/Karanpratap7/MedDoc-Flow/issues)
2. **Create an Issue**: Report bugs or request features
3. **Documentation**: Review this README and inline code comments

## 🎯 Roadmap

Future enhancements planned:
- [ ] Support for additional document formats (DOCX, TXT)
- [ ] Multi-language support
- [ ] Advanced document analytics
- [ ] User authentication and document management
- [ ] Export conversation history
- [ ] Integration with more AI models

## 👨‍💻 Author

**Karan Pratap**
- GitHub: [@Karanpratap7](https://github.com/Karanpratap7)

## 🙏 Acknowledgments

- LangChain community for excellent documentation
- Streamlit team for the amazing framework
- HuggingFace for providing pre-trained models
- The open-source community for various libraries used

---

<div align="center">
  <p>Made with ❤️ for the healthcare community</p>
  <p>🩺 <strong>MedDoc Flow</strong> - Bridging AI and Medical Documentation</p>
</div>
