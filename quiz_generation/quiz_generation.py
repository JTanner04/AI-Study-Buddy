from transformers import pipeline
from summarization_model import summarize_pdf, summarize_text  # Import the summarization function

# Load models for question generation and distractor creation
question_generator = pipeline("text2text-generation", model="valhalla/t5-small-qa-qg-hl")
distractor_generator = pipeline("text2text-generation", model="valhalla/t5-small-qa-qg-hl")  # Same model for simplicity

def generate_questions_from_summary(summary):
    try:
        questions = question_generator(f"generate questions: {summary}", max_length=100, num_return_sequences=5)
        return [q['generated_text'] for q in questions]
    except Exception as e:
        return f"An error occurred during question generation: {e}"

def generate_distractors(question, context):
    try:
        # Use the context to generate distractors (incorrect answers)
        distractors = distractor_generator(f"generate distractors: question: {question} context: {context}", 
                                           max_length=50, num_return_sequences=3)
        return [d['generated_text'] for d in distractors]
    except Exception as e:
        return [f"An error occurred during distractor generation: {e}"]

def format_quiz_question(question, correct_answer, distractors):
    # Randomly shuffle the correct answer and distractors
    import random
    all_answers = [correct_answer] + distractors
    random.shuffle(all_answers)

    # Return the formatted question and answer choices
    return {
        "question": question,
        "choices": all_answers,
        "correct": correct_answer
    }

def administer_quiz(quiz_questions):
    score = 0
    total_questions = len(quiz_questions)
    
    for idx, item in enumerate(quiz_questions, start=1):
        print(f"\nQuestion {idx}: {item['question']}")
        for i, choice in enumerate(item['choices'], start=1):
            print(f"{i}. {choice}")
        
        user_answer = input("Your answer (choose the number): ")
        try:
            user_choice = int(user_answer)
            if item['choices'][user_choice - 1] == item['correct']:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was: {item['correct']}")
        except (ValueError, IndexError):
            print(f"Invalid choice. The correct answer was: {item['correct']}")

    print(f"\nQuiz completed! Your score: {score}/{total_questions}")

def main():
    user_input = input("Enter the text or PDF you want summarized for quiz generation: ")
    if user_input.lower().endswith(".pdf"):
        summary = summarize_pdf(user_input)
    else:
        summary = summarize_text(user_input)
    
    if summary:
        print("\nGenerating questions based on the summary...\n")
        questions = generate_questions_from_summary(summary)
        
        # Create the quiz questions with multiple-choice answers
        quiz_questions = []
        for question in questions:
            distractors = generate_distractors(question, summary)
            quiz_item = format_quiz_question(question, correct_answer="TBD", distractors=distractors)  # Set correct answer manually or automate it if possible
            quiz_questions.append(quiz_item)
        
        # Administer the quiz
        administer_quiz(quiz_questions)
    else:
        print("Failed to generate summary for the provided content.")

if __name__ == "__main__":
    main()
