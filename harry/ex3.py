#Create a program capable of displaying questions to the user like KBC.
#Use list data types to store the qn and their correct answers.
#display the final amount the person is taking home after playing the game

questions = [
    {
        "question": "Which is the capital of nepal?",
        "options": ["A. Kathmandu", "B. Pokhara", "C.Biratnagar", "D. Dhangadi"],
        "answer":"A"
    },
    {
        "question": "Which language is used to write programs?",
        "options": ["A. English", "B. Python", "C. Nepali", "D. Hindi"],
        "answer": "B"
    }

]
prize_money = [1000, 5000, 10000]
total = 0
print("Welcome to KBC!")

for i in range(len(questions)):
    q = questions[i]
    print(f"Q{i+1}: {q['question']}")
    for opt in q["options"]:
        print(opt)
    
    ans = input("Enter your answer :").upper()

    if ans == q["answer"]:
        total += prize_money[i]
        print(f"Correct! You won Rs.{total}\n")
    else:
        print("Wrong answer!")
        break

print(f"Final amount: Rs.{total}")
