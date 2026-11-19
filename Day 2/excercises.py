questions = {
    "Python": "What is Python?",
    "Variables": "What are variables in Python?",
    "Data Types": "What are the different data types in Python?",
    "Lists": "What are lists in Python?",
    "Dictionaries": "What are dictionaries in Python?",
    "Other": "I don't know the answer to this question."
}

def get_answer(question):
        if question == "Python":
            print(questions["Python"])
        elif question == "Variables":
            print(questions["Variables"])
        elif question == "Data Types":
            print(questions["Data Types"])
        elif question == "Lists":
            print(questions["Lists"])
        elif question == "Dictionaries":
            print(questions["Dictionaries"])
        else:
            print(questions["Other"])

i = 0
while i == 0:
    user_question = input("To Exit press 0 , else Please enter a question: ")
    if user_question == "0":
        break
    get_answer(user_question)
