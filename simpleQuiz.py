def quiz_game():
    score = 0
    questions = [
        {"question": "What is the capital of France?", "options": ["a) Paris", "b) Berlin", "c) Madrid"], "answer": "a"},
        {"question": "What is 2 + 2?", "options": ["a) 3", "b) 4", "c) 5"], "answer": "b"},
        {"question": "Which language is known as the language of the web?", "options": ["a) Python", "b) C++", "c) JavaScript"], "answer": "c"},
    ]
    
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        guess = input("Enter your answer (a/b/c): ").lower()
        if guess == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!\n")
    
    print(f"Your final score is {score} out of {len(questions)}.")

quiz_game()
