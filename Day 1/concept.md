# Concepts in `day1_chatbot.py`

## Input and output

`input()` prompts the user and reads their response. `print()` displays messages in the console. The chatbot uses both to have a short text conversation.

## Variables

- `user_name` stores the name entered by the user.
- `question` stores the topic the user wants to learn about.

## Conditional branching

The `if`, `elif`, and `else` statements select a response based on the user's answer. The first matching condition runs; if no topic matches, the `else` branch provides a fallback response.

## String comparison

The chatbot compares `question` to exact text such as `"AI"` and `"LLM"`. These comparisons are case-sensitive, so `"AI"` matches but `"ai"` does not.

## Rule-based chatbot

Each answer is predefined in the code. The program does not learn or generate new answers; it selects a response according to the matching rule.

## Conversation flow

1. Display a welcome message.
2. Ask for the user's name and greet them.
3. Ask what they want to learn.
4. Display the matching topic response or the fallback message.