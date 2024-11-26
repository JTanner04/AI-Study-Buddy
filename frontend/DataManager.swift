import Foundation

class DataManager {
    
    // Singleton pattern for a single shared instance of DataManager
    static let shared = DataManager()
    
    private init() {} // Private initializer to enforce singleton usage
    
    // Function to fetch quiz data from backend or local data
    func fetchQuizData(completion: @escaping ([QuizQuestion]) -> Void) {
        // Replace the URL below with your actual backend endpoint
        guard let url = URL(string: "https://studybuddyapi.com/api/quiz-data/") else {
            print("Invalid URL for quiz data")
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        
        // If using authentication, add your token or credentials here
        // request.setValue("Bearer YOUR_ACCESS_TOKEN", forHTTPHeaderField: "Authorization")
        
        // Fetch data from the backend
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print("Error fetching quiz data: \(error.localizedDescription)")
                return
            }
            
            guard let data = data else {
                print("No data received for quiz")
                return
            }
            
            do {
                // Decode JSON data to array of QuizQuestion
                let quizQuestions = try JSONDecoder().decode([QuizQuestion].self, from: data)
                DispatchQueue.main.async {
                    completion(quizQuestions)
                }
            } catch {
                print("Error decoding quiz data: \(error.localizedDescription)")
            }
        }.resume()
    }
    
    // Function to fetch flashcards from backend or local data
    func fetchFlashcards(completion: @escaping ([Flashcard]) -> Void) {
        // Replace the URL below with your actual backend endpoint
        guard let url = URL(string: "https://studybuddyapi.com/api/flashcards/") else {
            print("Invalid URL for flashcard data")
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        
        // If using authentication, add your token or credentials here
        // request.setValue("Bearer YOUR_ACCESS_TOKEN", forHTTPHeaderField: "Authorization")
        
        // Fetch data from the backend
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print("Error fetching flashcard data: \(error.localizedDescription)")
                return
            }
            
            guard let data = data else {
                print("No data received for flashcards")
                return
            }
            
            do {
                // Decode JSON data to array of Flashcard
                let flashcards = try JSONDecoder().decode([Flashcard].self, from: data)
                DispatchQueue.main.async {
                    completion(flashcards)
                }
            } catch {
                print("Error decoding flashcard data: \(error.localizedDescription)")
            }
        }.resume()
    }
    
    // Function to fetch personalized study suggestions
    func fetchStudySuggestions(completion: @escaping ([String]) -> Void) {
        // Replace the URL below with your actual backend endpoint
        guard let url = URL(string: "https://studybuddyapi.com/api/study-suggestions/") else {
            print("Invalid URL for study suggestions")
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        
        // If using authentication, add your token or credentials here
        // request.setValue("Bearer YOUR_ACCESS_TOKEN", forHTTPHeaderField: "Authorization")
        
        // Fetch data from the backend
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print("Error fetching study suggestions: \(error.localizedDescription)")
                return
            }
            
            guard let data = data else {
                print("No data received for study suggestions")
                return
            }
            
            do {
                // Decode JSON data to array of suggestions
                let suggestions = try JSONDecoder().decode([String].self, from: data)
                DispatchQueue.main.async {
                    completion(suggestions)
                }
            } catch {
                print("Error decoding study suggestions: \(error.localizedDescription)")
            }
        }.resume()
    }
    
    // Function to submit quiz results to backend
    func submitQuizResults(_ results: [String: Any], completion: @escaping (Bool) -> Void) {
        // Replace the URL below with your actual backend endpoint
        guard let url = URL(string: "https://studybuddyapi.com/api/submit-quiz-results/") else {
            print("Invalid URL for submitting quiz results")
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        // If using authentication, add your token or credentials here
        // request.setValue("Bearer YOUR_ACCESS_TOKEN", forHTTPHeaderField: "Authorization")
        
        do {
            // Encode the quiz results to JSON
            let jsonData = try JSONSerialization.data(withJSONObject: results, options: [])
            request.httpBody = jsonData
            
            URLSession.shared.dataTask(with: request) { data, response, error in
                if let error = error {
                    print("Error submitting quiz results: \(error.localizedDescription)")
                    completion(false)
                    return
                }
                
                guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
                    print("Failed to submit quiz results")
                    completion(false)
                    return
                }
                
                // Successfully submitted results
                completion(true)
            }.resume()
        } catch {
            print("Error encoding quiz results to JSON: \(error.localizedDescription)")
            completion(false)
        }
    }
}

