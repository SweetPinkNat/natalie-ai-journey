def run_quiz(questions):
    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q["correct"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {q['correct']}.\n")

    return score


questions = [
    {
        "question": "1. What data type is True/False in Python?",
        "options": ["A. str", "B. int", "C. bool", "D. float"],
        "correct": "C"
    },
    {
        "question": "2. Which symbol starts a comment in Python?",
        "options": ["A. //", "B. #", "C. --", "D. **"],
        "correct": "B"
    },
    {
        "question": "3. What does len(['a','b','c']) return?",
        "options": ["A. 2", "B. 3", "C. 4", "D. Error"],
        "correct": "B"
    },
    {
        "question": "4. What keyword defines a function?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "correct": "C"
    }
]

total_questions = len(questions)
final_score = run_quiz(questions)

print("--- Quiz Complete ---")
print(f"You scored {final_score} out of {total_questions}.")

if final_score == total_questions:
    print("Perfect score! 🎉")
elif final_score >= total_questions / 2:
    print("Good job!")
else:
    print("Keep practicing — you'll get there.")