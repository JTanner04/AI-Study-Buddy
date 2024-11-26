import SwiftUI

struct QuizView: View {
    // Sample Data for Quiz
    @State private var quizQuestions: [QuizQuestion] = [
        QuizQuestion(question: "What is AI?", options: ["Artificial Intelligence", "Animal Interaction", "Automated Input", "Artificial Insight"], correctOption: 0)
    ]
    
    @State private var currentQuestionIndex: Int = 0
    @State private var userAnswer: Int? = nil
    @State private var isAnswerCorrect: Bool? = nil
    @State private var showResult: Bool = false
    
    var body: some View {
        VStack {
            Text("Quiz")
                .font(.largeTitle)
                .padding()
            
            // Display the current question
            Text(quizQuestions[currentQuestionIndex].question)
                .font(.title2)
                .padding()
            
            // Display answer options
            ForEach(0..<quizQuestions[currentQuestionIndex].options.count, id: \.self) { index in
                Button(action: {
                    userAnswer = index
                    checkAnswer()
                }) {
                    Text(quizQuestions[currentQuestionIndex].options[index])
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(userAnswer == index ? Color.blue : Color.gray.opacity(0.3))
                        .foregroundColor(.black)
                        .cornerRadius(8)
                        .padding(.vertical, 5)
                }
            }
            
            // Feedback for the user
            if let isCorrect = isAnswerCorrect {
                Text(isCorrect ? "Correct!" : "Wrong!")
                    .font(.headline)
                    .foregroundColor(isCorrect ? .green : .red)
                    .padding()
            }
            
            // Button to move to the next question
            Button(action: {
                nextQuestion()
            }) {
                Text("Next Question")
                    .font(.headline)
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
            .padding(.top)
            
            Spacer()
        }
        .padding()
    }
    
    // Function to check if the selected answer is correct
    private func checkAnswer() {
        guard let userAnswer = userAnswer else { return }
        isAnswerCorrect = userAnswer == quizQuestions[currentQuestionIndex].correctOption
        showResult = true
    }
    
    // Function to go to the next question
    private func nextQuestion() {
        if currentQuestionIndex < quizQuestions.count - 1 {
            currentQuestionIndex += 1
            userAnswer = nil
            isAnswerCorrect = nil
        } else {
            // Show completion message if no more questions
            print("Quiz completed")
        }
    }
}

// Data Model for Quiz Questions
struct QuizQuestion {
    var question: String
    var options: [String]
    var correctOption: Int
}

struct QuizView_Previews: PreviewProvider {
    static var previews: some View {
        QuizView()
    }
}
