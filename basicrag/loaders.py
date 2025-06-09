import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader, WebBaseLoader

def load_file(path):
    """Load document from file path based on extension"""
    ext = os.path.splitext(path)[-1].lower()
    if ext == ".pdf":
        loader = PyPDFLoader(path)
    elif ext == ".txt":
        loader = TextLoader(path)
    elif ext == ".docx":
        loader = Docx2txtLoader(path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
    return loader.load()

def load_url(url):
    """Load content from webpage URL"""
    return WebBaseLoader([url]).load()