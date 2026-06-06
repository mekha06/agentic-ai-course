# Tokenization Demo
# Tokenization means splitting text into smaller units called tokens.
text = input("Enter a sentence: ")
# Simple tokenization using split()
tokens = text.split()
print("\nOriginal Text:")
print(text)
print("\nTokens:")
print(tokens)
print("\nNumber of tokens:")
print(len(tokens))

"""
--------------------------------Output-------------------------------
Enter a sentence: learning agentic ai course

Original Text:
learning agentic ai course

Tokens:
['learning', 'agentic', 'ai', 'course']

Number of tokens:
4

"""