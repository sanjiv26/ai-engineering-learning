print("Welcome to my First Chatbot!")
user_name = input("Enter Your Name: ")
print("Hello ",user_name)
question = input("What do you want to learn ?")
if question == "Machine Learning":
    print("Machine Learning is a subset of AI")
elif question == "AI":
    print("AI is Aritificial Intelligence")
elif question == "Deep Learning":
    print("Deep Learning is a subset of Machine Learning")
elif question == "General AI":
    print("General AI is a type of AI that can perform any intellectual task that a human can do")
elif question == "LLM":
    print("LLM is a type of AI that can understand and generate human language")
else:
    print("I am still learning , Ask me somethig else :)")