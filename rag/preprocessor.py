import re

def clean_text(text):
    """Basic text cleaning function"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove non-printable characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text.strip()