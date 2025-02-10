import random
import time

# Quiz questions embedded in the script
QUESTIONS = {
    "math": [
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
            "answer": "C"
        },
        {
            "question": "What is 12 x 5?",
            "options": ["A) 50", "B) 60", "C) 70", "D) 80"],
            "answer": "B"
        },
        {
            "question": "What is 100 ÷ 4?",
            "options": ["A) 20", "B) 25", "C) 30", "D) 35"],
            "answer": "B"
        },
        {
            "question": "What is the value of π (pi) to two decimal places?",
            "options": ["A) 3.12", "B) 3.14", "C) 3.16", "D) 3.18"],
            "answer": "B"
        },
        {
            "question": "What is 7 squared?",
            "options": ["A) 49", "B) 56", "C) 63", "D) 70"],
            "answer": "A"
        },
        {
            "question": "What is 15% of 200?",
            "options": ["A) 20", "B) 25", "C) 30", "D) 35"],
            "answer": "C"
        }
    ],
    "science": [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) CO2", "B) H2O", "C) O2", "D) NaCl"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the smallest unit of life?",
            "options": ["A) Atom", "B) Molecule", "C) Cell", "D) Organ"],
            "answer": "C"
        },
        {
            "question": "What is the speed of light?",
            "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 450,000 km/s", "D) 600,000 km/s"],
            "answer": "A"
        },
        {
            "question": "What is the atomic number of carbon?",
            "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
            "answer": "A"
        },
        {
            "question": "What force keeps planets in orbit around the sun?",
            "options": ["A) Electromagnetism", "B) Gravity", "C) Friction", "D) Magnetism"],
            "answer": "B"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A) Gold", "B) Diamond", "C) Iron", "D) Quartz"],
            "answer": "B"
        }
    ],
    "geography": [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "answer": "B"
        },
        {
            "question": "Which country has the largest population?",
            "options": ["A) India", "B) USA", "C) China", "D) Russia"],
            "answer": "C"
        },
        {
            "question": "What is the longest river in the world?",
            "options": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"],
            "answer": "B"
        },
        {
            "question": "Which continent is the Sahara Desert located on?",
            "options": ["A) Asia", "B) Africa", "C) Australia", "D) South America"],
            "answer": "B"
        },
        {
            "question": "What is the smallest country in the world?",
            "options": ["A) Monaco", "B) San Marino", "C) Vatican City", "D) Liechtenstein"],
            "answer": "C"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["A) China", "B) Japan", "C) South Korea", "D) Thailand"],
            "answer": "B"
        },
        {
            "question": "What is the capital of Australia?",
            "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
            "answer": "C"
        }
    ]
}

# Run the quiz

def run_quiz(questions):
    score = 0
    print("Welcome to the Quiz Game!\n")
    time.sleep(1)

    for i, question_data in enumerate(questions):
        print(f"Question {i + 1}: {question_data['question']}")
        for option in question_data["options"]:
            print(option)

        start_time = time.time()
        user_answer = input("Your answer (A/B/C): ").strip().upper()
        end_time = time.time()

        if user_answer == question_data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question_data['answer']}.\n")

        response_time = end_time - start_time
        print(f"Time taken: {response_time: .2f} seconds\n")

    print(f"Your final score is: {score}/{len(QUESTIONS)}")
    return score

# Save the results to a file
def save_result(category, score):
    with open("/app/results/quiz_results.txt", "a") as file:
        file.write(f"Category: {category}, Quiz Score: {score}\n")

# Main function
if __name__ == "__main__":
    print("Choose a category:")
    print("1. Geography")
    print("2. Science")
    print("3. Math")
    choice = input("Enter the number of your choice: ").strip()

    categories = {
        "1": "geography",
        "2": "science",
        "3": "math",
    }

    category = categories.get(choice, "geography") # default geography as a selection for quiz
    questions = QUESTIONS[category]
    random.shuffle(questions) # randomize the questions

    selected_questions = questions[:5] # select five questions

    score = run_quiz(selected_questions)
    save_result(category, score)
