from basicrag import RAGPipeline

# Example with custom prompt
custom_prompt = """[SYSTEM] You're a research assistant. Use only the provided context.

Context:
{context}

[USER] Question: {query}
[ASSISTANT] Answer:"""

rag_custom = RAGPipeline(
    chunk_size=500,
    chunk_overlap=50,
    top_k=5,
    llm_provider="gemini",
    llm_model="gemini-1.5-flash",
    api_key="your_api_key_here",  # Replace with your actual API key
    custom_prompt=custom_prompt
)

rag_custom.load_data("C:\\Users\\nares\\Downloads\\How Vectors Are Stored, Indexed, and Retrieved.docx")
rag_custom.fit()
response = rag_custom.query(input("Enter your question: "))
print("📢 Custom Prompt Response:\n", response)