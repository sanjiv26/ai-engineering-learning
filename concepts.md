# Concepts in `day1_chatbot.py`

## 1. Input and output

- `input()` displays a prompt and waits for the user to type a response.
- `print()` displays text in the console.
- This chatbot uses both to have a short text conversation.

## 2. Variables

Variables store values so the program can use them later:

- `user_name` stores the name entered by the user.
- `question` stores the topic the user wants to learn about.

## 3. Conditional branching

The `if`, `elif`, and `else` statements let the program choose what to do based on the user's answer. The first matching condition runs; if none match, the `else` branch provides a fallback response.

## 4. String comparison

Each condition compares `question` to a specific piece of text, such as `"AI"` or `"LLM"`. These are exact, case-sensitive matches. For example, `"AI"` matches, but `"ai"` does not.

## 5. Rule-based chatbot

The responses are written directly into the program. The chatbot does not learn from the conversation or generate new answers; it selects a predefined response based on the matched rule.

## Conversation flow

1. Display a welcome message.
2. Ask for the user's name and greet them.
3. Ask what they want to learn.
4. Match the answer to a predefined topic and show its response, or show the fallback message.