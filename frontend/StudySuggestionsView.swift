import SwiftUI

struct StudySuggestionsView: View {
    // Sample personalized suggestions
    @State private var suggestions: [String] = [
        "Review the concept of Neural Networks.",
        "Focus more on reinforcement learning basics.",
        "Consider using flashcards to memorize key terms."
    ]
    
    var body: some View {
        VStack {
            Text("Personalized Study Suggestions")
                .font(.largeTitle)
                .padding()
            
            List(suggestions, id: \.self) { suggestion in
                Text(suggestion)
                    .padding()
            }
            
            Spacer()
        }
        .padding()
    }
}

struct StudySuggestionsView_Previews: PreviewProvider {
    static var previews: some View {
        StudySuggestionsView()
    }
}
