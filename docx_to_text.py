from docx import Document

def docx_to_text(docx_file, txt_file):
    """Converts a .docx file to a .txt file."""
    try:
        # Open the .docx file
        doc = Document(docx_file)
        
        # Extract text from the document
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        
        # Join all the paragraphs and write to the .txt file
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(full_text))
        
        print(f"Successfully converted '{docx_file}' to '{txt_file}'")

    except Exception as e:
        print(f"Error converting docx to txt: {e}")

# Example usage
docx_to_text('sample_resume.docx', 'sample_resume.txt')

