from setuptools import setup, find_packages

setup(
    name="raglite",
    version="0.1.0", 
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain-community",
        "faiss-cpu",
        "sentence-transformers",
        "groq",
        "google-generativeai",
        "openai",
        "tiktoken",
        "python-dotenv",
        "bs4",
        "pypdf",
        "requests",
        "docx2txt"
    ],
    description="Lightweight RAG pipeline for document question answering",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Naresh Edagotti",
    author_email="statfusionai@gmail.com",
    url="https://github.com/Nareshedagotti/raglite",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
