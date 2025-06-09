from basicrag import RAGPipeline

# Example with default settings
rag = RAGPipeline(
    llm_provider="groq",
    llm_model="gemma2-9b-it",
    api_key="your_api_key_here",  # Replace with your actual API key
    top_k=3
)

rag.load_data("https://en.wikipedia.org/wiki/Large_language_model")
rag.fit()
response = rag.query("What are large language models?")
print("Response:\n", response)
