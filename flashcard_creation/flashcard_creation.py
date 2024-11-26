from transformers import pipeline
from summarization_model import summarize_pdf, summarize_text  # Import the summarization function
import spacy
import json

# Load spaCy's English model for keyword extraction
nlp = spacy.load("en_core_web_sm")

# Load models for definition/question generation
definition_generator = pipeline("text2text-generation", model="t5-small")  # For generating definitions

def extract_keywords(summary):
    # Use spaCy to extract potential key terms
    doc = nlp(summary)
    keywords = [chunk.text for chunk in doc.noun_chunks if len(chunk.text.split()) <= 3]  # Limit to short phrases
    return list(set(keywords))  # Remove duplicates

def generate_flashcard(keyword):
    try:
        # Generate a simple definition using a text generation model
        definition = definition_generator(f"Define: {keyword}", max_length=50, num_return_sequences=1)
        return definition[0]['generated_text']
    except Exception as e:
        return f"An error occurred during flashcard generation: {e}"

def create_flashcards(summary):
    keywords = extract_keywords(summary)
    flashcards = []

    for keyword in keywords:
        definition = generate_flashcard(keyword)
        flashcard = {
            "question": f"What is {keyword}?",
            "answer": definition
        }
        flashcards.append(flashcard)
    
    return flashcards

def display_flashcards(flashcards):
    print("\nGenerated Flashcards:\n")
    for idx, flashcard in enumerate(flashcards, start=1):
        print(f"Flashcard {idx}:")
        print(f"Q: {flashcard['question']}")
        print(f"A: {flashcard['answer']}")
        print("-" * 30)

def manual_edit_flashcards(flashcards):
    print("\nManual Editing Mode:\n")
    for idx, flashcard in enumerate(flashcards, start=1):
        print(f"Flashcard {idx}:")
        print(f"Q: {flashcard['question']}")
        print(f"A: {flashcard['answer']}")
        edit = input("Would you like to edit this flashcard? (yes/no): ").strip().lower()
        
        if edit == "yes":
            new_question = input("Enter new question: ")
            new_answer = input("Enter new answer: ")
            flashcard['question'] = new_question
            flashcard['answer'] = new_answer

    return flashcards

def save_flashcards_to_file(flashcards, filename="flashcards.json"):
    try:
        with open(filename, "w") as file:
            json.dump(flashcards, file, indent=4)
        print(f"\nFlashcards successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving flashcards: {e}")

def load_flashcards_from_file(filename="flashcards.json"):
    try:
        with open(filename, "r") as file:
            flashcards = json.load(file)
        return flashcards
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty set of flashcards.")
        return []
    except Exception as e:
        print(f"Error loading flashcards: {e}")
        return []

def main():
    # Load any existing flashcards
    flashcards = load_flashcards_from_file()
    
    user_input = input("Enter the text or PDF you want summarized for flashcard creation: ")
    if user_input.lower().endswith(".pdf"):
        summary = summarize_pdf(user_input)
    else:
        summary = summarize_text(user_input)
    
    if summary:
        print("\nGenerating flashcards based on the summary...\n")
        new_flashcards = create_flashcards(summary)
        
        # Display the generated flashcards
        display_flashcards(new_flashcards)
        
        # Ask the user if they want to manually edit the flashcards
        edit_choice = input("Do you want to manually edit the flashcards? (yes/no): ").strip().lower()
        if edit_choice == "yes":
            new_flashcards = manual_edit_flashcards(new_flashcards)

        # Merge new flashcards with existing ones
        flashcards.extend(new_flashcards)
        
        # Save the flashcards to a file
        save_flashcards_to_file(flashcards)
    else:
        print("Failed to generate summary for the provided content.")

if __name__ == "__main__":
    main()
