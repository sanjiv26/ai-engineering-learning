# Day 2 - Python Basics

## Variables

Variables store values that can be reused in a program.

```python
name = "Sanjiv"
experience = 4
current_role = "Software Engineer"
learning_ai = True
```

String values can be inserted into text using an f-string:

```python
print(f"My name is {name}. I have {experience} years of experience.")
```

## Lists

A list stores multiple values in an ordered collection.

```python
ai_technologies = ["GenAI", "Agentic AI", "MCP", "LangChain", "LlamaIndex"]
```

List items are accessed by index, starting from 0.

```python
print(ai_technologies[0])  # GenAI
```

## Dictionaries

A dictionary stores data as key-value pairs.

```python
ai_profile = {
    "name": "Sanjiv",
    "skills": ["Python", "Selenium", "Pytest"],
    "learning": ["GenAI", "Agentic AI", "MCP"]
}
```

Values can be accessed using their keys or by combining dictionary and list indexing:

```python
print(ai_profile["name"])
print(ai_profile["skills"][0])
print(ai_profile["learning"][1])
```

## Functions

Functions group reusable code and can return a result.

```python
def add(a, b):
    return a + b

addition = add(5, 3)
print(addition)
```

## If/Else Conditions

Conditional statements execute code based on a condition.

```python
def answer(question):
    if question == "Python":
        return "Python Question"
    elif question == "GenAI":
        return "GenAI Question"
    else:
        return "Other Question"
```

## While Loops and User Input

A while loop repeats as long as its condition is true.

```python
i = 0
while i == 0:
    user_question = input("Enter a question, or 0 to exit: ")
    if user_question == "0":
        break
```

## JSON

JSON is a text format commonly used to exchange data.

```python
import json

test_result = {
    "test_name": "test_login",
    "status": "failed",
    "error": "Element not found"
}

json_text = json.dumps(test_result, indent=4)
python_dict = json.loads(json_text)

print(python_dict["test_name"])
print(python_dict["error"])
```

- `json.dumps()` converts a Python dictionary into formatted JSON text.
- `json.loads()` converts JSON text back into a Python dictionary.