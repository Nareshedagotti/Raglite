from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(documents, chunk_size=1000, chunk_overlap=100):
    """Split documents into chunks with specified size and overlap"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    return splitter.split_documents(documents)