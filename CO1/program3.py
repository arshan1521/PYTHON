def word_count(line):
    counts = {}
    words = line.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# Example usage:
user_input = input("Enter a line of text: ")
result = word_count(user_input)
print(result)
