questions = {"What is 2+2?": "4", "Capital of India?": "Delhi"}
score = 0
for q, a in questions.items():
    ans = input(q + " ")
    if ans.lower() == a.lower():
        score += 1
print(f"Your score: {score}/{len(questions)}")
