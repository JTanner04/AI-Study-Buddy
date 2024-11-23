from transformers import pipeline
import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text
    except FileNotFoundError:
        print(f"Error: The file at {pdf_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        return None

def get_user_text_info():
    text_input = input("Please enter the text you want summarized: ")
    while len(text_input) < 30 or len(text_input) > 1000:
        print("Text should be at least 30 characters long and with a maximum of 1000 characters.")
        text_input = input("Please enter the text you want summarized: ")
    return text_input

def summarize_text(text):
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"An error occurred during summarization: {e}"

def summarize_pdf(pdf_path):
    extracted_text = extract_text_from_pdf(pdf_path)
    if not extracted_text:
        return "No text could be extracted from the PDF."

    if len(extracted_text) > 1000:
        extracted_text = extracted_text[:1000]

    summary = summarize_text(extracted_text)
    return summary

def main():
    input_type = input("Enter 'text' to summarize a text or 'pdf' to summarize a PDF: ")
    if input_type.lower() == "text":
        user_text = get_user_text_info()
        summary = summarize_text(user_text)
        print(f"\nSummary:\n{summary}")
    elif input_type.lower() == "pdf":
        pdf_path = input("Enter the path to the PDF file: ")
        while not (pdf_path.endswith(".pdf") and os.path.isfile(pdf_path)):
            print("Please enter a valid path to an existing PDF file.")
            pdf_path = input("Enter the path to the PDF file: ")
        summary = summarize_pdf(pdf_path)
        print(f"\nSummary:\n{summary}")
    else:
        print("Invalid input. Please enter 'text' or 'pdf'.")

if __name__ == "__main__":
    main()
