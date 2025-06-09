from .loaders import load_file, load_url
from .preprocessor import clean_text
from .chunker import split_text
from .embedder import get_embeddings
from .vectorstore import build_vectorstore
from .llm import run_llm_response

class RAGPipeline:
    def __init__(
        self,
        llm_provider="groq",
        llm_model="gemma2-9b-it",
        api_key=None,
        chunk_size=1000,
        chunk_overlap=100,
        top_k=3,
        embedding_model="sentence-transformers/all-MiniLM-L6-v2",
        custom_prompt=None
    ):
        self.llm_provider = llm_provider
        self.llm_model = llm_model
        self.api_key = api_key
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.top_k = top_k
        self.embedding_model_name = embedding_model
        self.custom_prompt = custom_prompt
        self.documents = None
        self.chunks = None
        self.vectorstore = None
        self.embedding_model = None

    def load_data(self, source):
        if source.startswith(("http://", "https://")):
            print("🌐 Loading data from URL...")
            self.documents = load_url(source)
        else:
            print(f"📄 Loading data from file: {source}")
            self.documents = load_file(source)
        print(f"✅ Extracted {len(self.documents)} documents")

    def fit(self):
        if not self.documents:
            raise ValueError("No documents loaded. Call load_data() first.")
        
        print("Preprocessing text...")
        for doc in self.documents:
            doc.page_content = clean_text(doc.page_content)
        
        print("Chunking documents...")
        self.chunks = split_text(
            self.documents, 
            self.chunk_size, 
            self.chunk_overlap
        )
        print(f"Created {len(self.chunks)} chunks")
        
        print("Generating embeddings...")
        self.embedding_model = get_embeddings(self.embedding_model_name)
        
        print("Building vector store...")
        self.vectorstore = build_vectorstore(self.chunks, self.embedding_model)
        print("✅ RAG pipeline ready")

    def query(self, query):
        if not self.vectorstore:
            raise ValueError("Vector store not built. Call fit() first.")
        
        print(f"Retrieving top {self.top_k} matches...")
        query_vector = self.embedding_model.embed_query(query)
        top_matches = self.vectorstore.similarity_search_by_vector(
            query_vector, 
            k=self.top_k
        )
        
        print("Generating response...")
        response = run_llm_response(
            query=query,
            top_matches=top_matches,
            provider=self.llm_provider,
            model=self.llm_model,
            api_key=self.api_key,
            custom_prompt=self.custom_prompt
        )
        return response