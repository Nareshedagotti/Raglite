RAGlite - Lightweight RAG Pipeline
RAGlite is a simple yet powerful Python package for building Retrieval-Augmented Generation (RAG) pipelines. With just 4-5 lines of code, you can process documents, generate embeddings, and query information using state-of-the-art LLMs.

Features
✅ Multi-format support: PDF, DOCX, TXT, and URLs
✅ Customizable chunking: Control chunk size and overlap
✅ Multiple LLM providers: Groq, Gemini, OpenAI
✅ Custom prompts: Bring your own prompt templates
✅ Progress logging: Visual console feedback at each step

Installation
bash
pip install raglite
Quick Start
python
from raglite import RAGPipeline

# Initialize pipeline
rag = RAGPipeline(
    llm_provider="groq",
    llm_model="llama3-70b-8192",
    api_key="YOUR_API_KEY"
)

# Load and process data
rag.load_data("https://en.wikipedia.org/wiki/Large_language_model")
rag.fit()

# Query the document
response = rag.query("What are large language models?")
print(response)
Configuration Options
Customize your RAG pipeline with these parameters:

Parameter	Default	Description
llm_provider	"groq"	LLM service ("groq", "gemini", "openai")
llm_model	"llama3-70b-8192"	Model name
api_key	None	Provider API key
chunk_size	1000	Text chunk size in characters
chunk_overlap	100	Chunk overlap in characters
top_k	3	Number of context chunks to retrieve
embedding_model	"sentence-transformers/all-MiniLM-L6-v2"	Embedding model
custom_prompt	None	Custom prompt template
Custom Prompt Templates
Use your own prompt format with {context} and {query} placeholders:

python
custom_prompt = """[INSTRUCTIONS]
Answer the question using ONLY the provided context. 
If unsure, respond "I don't know".

[CONTEXT]
{context}

[QUESTION]
{query}

[ANSWER]
"""

rag = RAGPipeline(
    llm_provider="gemini",
    llm_model="gemini-pro",
    api_key="YOUR_GEMINI_KEY",
    custom_prompt=custom_prompt
)
Supported Models
Groq
llama3-70b-8192

llama3-8b-8192

mixtral-8x7b-32768

gemma2-9b-it

Gemini
gemini-pro

gemini-1.5-pro-latest

gemini-1.0-pro

OpenAI
gpt-4-turbo

gpt-3.5-turbo

gpt-4o

Advanced Usage
Local File Processing
python
# Process different file types
rag.load_data("research_paper.pdf")
rag.load_data("contract.docx")
rag.load_data("notes.txt")
Multiple Documents
python
rag = RAGPipeline(...)

# Load multiple sources
rag.load_data("https://example.com/article")
rag.load_data("data/document1.pdf")
rag.load_data("data/notes.txt")

rag.fit()
Changing Embedding Model
python
rag = RAGPipeline(
    embedding_model="sentence-transformers/all-mpnet-base-v2",
    # other params...
)
Command Line Interface (CLI)
RAGlite includes a simple CLI for quick queries:

bash
raglite query "What is the main topic?" \
  --file document.pdf \
  --provider groq \
  --model llama3-70b-8192 \
  --api-key YOUR_KEY
Install CLI extras:

bash
pip install raglite[cli]
Troubleshooting
Common Issues
Missing dependencies:
pip install -r requirements.txt

API key not set:
Set as parameter or in .env file:

text
GROQ_API_KEY=your_key
GEMINI_API_KEY=your_key
OPENAI_API_KEY=your_key
Unsupported file format:
Currently supports PDF, DOCX, TXT, and URLs

Contributing
We welcome contributions! Here's how to set up your development environment: