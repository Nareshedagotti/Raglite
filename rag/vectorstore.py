from langchain_community.vectorstores import FAISS

def build_vectorstore(chunks, embedding_model):
    """Create FAISS vector store from document chunks"""
    return FAISS.from_documents(chunks, embedding_model)