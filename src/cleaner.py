import re

def clean_text(text):
    """
    Clean the extracted resume text.
    Steps:
    - Convert to lowercase
    - Remove extra spaces
    - Fix newlines
    - Remove special characters
    """
    
    # 1. Lowercase everything (important for skill matching later)
    text = text.lower()

    # 2. Remove bullets or special symbols
    text = re.sub(r'[•●■□▪○–—-]', ' ', text)

    # 3. Remove tabs
    text = text.replace("\t", " ")

    # 4. Replace multiple spaces with one
    text = re.sub(r'\s+', ' ', text)

    # 5. Remove extra line breaks
    text = re.sub(r'\n+', '\n', text)

    # 6. Trim spaces
    text = text.strip()

    return text
