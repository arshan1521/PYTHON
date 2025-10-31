words = input("Enter words separated by space: ").split()
longest = max(words, key=len)
print("Length of longest word:", len(longest))
