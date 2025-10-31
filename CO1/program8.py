def exchange_first_last(s: str) -> str:
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]

user_input = input("Enter a string: ")
result = exchange_first_last(user_input)
print("Result:", result)
