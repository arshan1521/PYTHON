def replace_char(input_str):
    first_char = input_str[0]
    replaced_str = first_char + input_str[1:].replace(first_char, '$')
    return replaced_str

user_input = input("Enter a string: ")
result = replace_char(user_input)
print("Result:", result)
