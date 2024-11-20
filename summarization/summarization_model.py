from transformers import pipeline

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
        # Extracting the summary text from the result
        return summary[0]['summary_text']
    except Exception as e:
        return f"An error occurred during summarization: {e}"

def main():
    user_text = get_user_text_info()
    summary = summarize_text(user_text)
    print(f"\nSummary:\n{summary}")

if __name__ == "__main__":
    main()
