def run_llm_response(query, top_matches, provider, model, api_key, custom_prompt=None):
    """Generate LLM response with context from top matches"""
    context = "\n\n".join([f"Source {i+1}: {doc.page_content}" for i, doc in enumerate(top_matches)])
    
    # Use custom prompt if provided, otherwise use default
    if custom_prompt:
        prompt = custom_prompt.format(context=context, query=query)
    else:
        prompt = f"""Use the following context to answer the question at the end.
        
        Context:
        {context}
        
        Question: {query}
        Answer:"""
    
    # Groq implementation
    if provider == "groq":
        from groq import Groq
        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model,
            temperature=0.3,
        )
        return completion.choices[0].message.content
    
    # Gemini implementation
    elif provider == "gemini":
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model)
        response = model.generate_content(prompt)
        return response.text
    
    # OpenAI implementation
    elif provider == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        return response.choices[0].message.content
    
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")