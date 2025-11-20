import docx

def extract_text_from_docx(path):
    document = docx.Document(path)
    return "\n".join([para.text for para in document.paragraphs])
