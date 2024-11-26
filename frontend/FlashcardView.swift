import SwiftUI

struct FlashcardView: View {
    // Sample flashcard data
    @State private var flashcards: [Flashcard] = [
        Flashcard(question: "What is AI?", answer: "AI stands for Artificial Intelligence.")
    ]
    
    @State private var currentIndex: Int = 0
    @State private var showAnswer: Bool = false
    
    var body: some View {
        VStack {
            Text("Flashcards")
                .font(.largeTitle)
                .padding()
            
            // Flashcard display
            ZStack {
                if showAnswer {
                    Text(flashcards[currentIndex].answer)
                        .font(.title2)
                        .padding()
                        .frame(maxWidth: .infinity, maxHeight: 200)
                        .background(Color.blue.opacity(0.3))
                        .cornerRadius(10)
                } else {
                    Text(flashcards[currentIndex].question)
                        .font(.title2)
                        .padding()
                        .frame(maxWidth: .infinity, maxHeight: 200)
                        .background(Color.orange.opacity(0.3))
                        .cornerRadius(10)
                }
            }
            .padding()
            .onTapGesture {
                // Flip the card to show the answer or question
                showAnswer.toggle()
            }
            
            // Navigation buttons
            HStack {
                Button(action: {
                    previousCard()
                }) {
                    Text("Previous")
                        .font(.headline)
                        .padding()
                        .background(Color.gray.opacity(0.3))
                        .cornerRadius(10)
                }
                
                Spacer()
                
                Button(action: {
                    nextCard()
                }) {
                    Text("Next")
                        .font(.headline)
                        .padding()
                        .background(Color.gray.opacity(0.3))
                        .cornerRadius(10)
                }
            }
            .padding()
            
            Spacer()
        }
        .padding()
    }
    
    // Function to move to the previous flashcard
    private func previousCard() {
        if currentIndex > 0 {
            currentIndex -= 1
            showAnswer = false
        }
    }
    
    // Function to move to the next flashcard
    private func nextCard() {
        if currentIndex < flashcards.count - 1 {
            currentIndex += 1
            showAnswer = false
        }
    }
}

// Data Model for Flashcards
struct Flashcard {
    var question: String
    var answer: String
}

struct FlashcardView_Previews: PreviewProvider {
    static var previews: some View {
        FlashcardView()
    }
}
