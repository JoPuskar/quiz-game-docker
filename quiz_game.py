import json

# Quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    print("Welcome to the Quiz Game!\n")

    for i, question_data in enumerate(quiz_data):
        print(f"Question {i + 1}: {question_data['question']}")
        for option in question_data["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C): ").strip().upper()

        if user_answer == question_data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question_data['answer']}.\n")

    print(f"Your final score is: {score}/{len(quiz_data)}")
    return score

def save_result(score):
    with open("quiz_results.txt", "a") as file:
        file.write(f"Quiz Score: {score}/{len(quiz_data)}\n")

if __name__ == "__main__":
    score = run_quiz()
    save_result(score)
