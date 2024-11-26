import json
import random
from datetime import datetime

# Load flashcards from the JSON file
def load_flashcards(filename="flashcards.json"):
    try:
        with open(filename, "r") as file:
            flashcards = json.load(file)
        return flashcards
    except FileNotFoundError:
        print(f"{filename} not found. Starting without flashcards.")
        return []
    except Exception as e:
        print(f"Error loading flashcards: {e}")
        return []

# Load user performance history from a JSON file
def load_user_history(filename="user_history.json"):
    try:
        with open(filename, "r") as file:
            history = json.load(file)
        return history
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty user history.")
        return {}
    except Exception as e:
        print(f"Error loading user history: {e}")
        return {}

# Save user performance history to a JSON file
def save_user_history(history, filename="user_history.json"):
    try:
        with open(filename, "w") as file:
            json.dump(history, file, indent=4)
        print(f"User history successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving user history: {e}")

# Function to update user performance history
def update_user_performance(user_id, quiz_results):
    user_history = load_user_history()

    if user_id not in user_history:
        user_history[user_id] = {
            "scores": [],
            "topics": {},
            "last_review": None
        }

    user_history[user_id]["scores"].append(quiz_results["score"])
    for topic, correct in quiz_results["topic_performance"].items():
        if topic not in user_history[user_id]["topics"]:
            user_history[user_id]["topics"][topic] = {"correct": 0, "total": 0}
        user_history[user_id]["topics"][topic]["correct"] += correct
        user_history[user_id]["topics"][topic]["total"] += 1

    # Update the last review date
    user_history[user_id]["last_review"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save the updated user history
    save_user_history(user_history)

# Generate personalized study suggestions
def generate_study_suggestions(user_id):
    user_history = load_user_history()
    suggestions = []

    if user_id not in user_history:
        return ["No performance data found. Take a quiz to get personalized suggestions!"]

    user_data = user_history[user_id]
    average_score = sum(user_data["scores"]) / len(user_data["scores"]) if user_data["scores"] else 0
    topics_to_review = []

    # Identify weak areas based on topics
    for topic, performance in user_data["topics"].items():
        accuracy = performance["correct"] / performance["total"] if performance["total"] > 0 else 0
        if accuracy < 0.7:  # Consider a topic "weak" if accuracy is below 70%
            topics_to_review.append((topic, accuracy))

    if average_score < 70:
        suggestions.append("Your average quiz score is below 70%. Focus on general review and flashcards.")
    elif topics_to_review:
        suggestions.append("You have some weak areas to address:")
        for topic, accuracy in topics_to_review:
            suggestions.append(f" - Review topic '{topic}' (Accuracy: {accuracy*100:.1f}%)")
    else:
        suggestions.append("Great work! Keep reviewing flashcards to maintain your knowledge.")

    # Suggest specific flashcards to review based on weak topics
    flashcards = load_flashcards()
    if topics_to_review and flashcards:
        suggestions.append("\nRecommended Flashcards:")
        for topic, _ in topics_to_review:
            relevant_flashcards = [fc for fc in flashcards if topic.lower() in fc['question'].lower()]
            if relevant_flashcards:
                suggestions.append(f" - Topic: {topic}")
                for fc in relevant_flashcards[:3]:  # Suggest up to 3 flashcards per topic
                    suggestions.append(f"   * {fc['question']}: {fc['answer']}")

    return suggestions

# Display personalized study suggestions
def display_study_suggestions(user_id):
    suggestions = generate_study_suggestions(user_id)
    print("\nPersonalized Study Suggestions:\n")
    for suggestion in suggestions:
        print(suggestion)

# Function to get user preferences and suggest study strategies
def suggest_study_strategy():
    print("\nAnswer a few questions to get a personalized study strategy:")
    preferred_style = input("Do you prefer (1) Visual, (2) Auditory, or (3) Kinesthetic learning? ")

    strategies = {
        "1": "Visual: Use diagrams, charts, and mind maps. Consider using flashcards for spaced repetition.",
        "2": "Auditory: Record your notes and listen to them. Engage in discussions or use voice-based study tools.",
        "3": "Kinesthetic: Use hands-on activities, role-play scenarios, or write notes by hand to reinforce learning."
    }

    print(f"\nStudy Strategy: {strategies.get(preferred_style, 'General: Experiment with different methods to see what works best for you!')}")

# Main function
def main():
    user_id = input("Enter your user ID: ")

    # Display personalized study suggestions
    display_study_suggestions(user_id)

    # Suggest study strategies based on learning style
    suggest_study_strategy()

if __name__ == "__main__":
    main()
