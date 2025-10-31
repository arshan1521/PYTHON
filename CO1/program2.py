# (a) Generate positive list of numbers
numbers = list(map(int, input("Enter integers separated by space: ").split()))
positive_numbers = [num for num in numbers if num > 0]
print("Positive numbers:", positive_numbers)

# (b) Square of N numbers
N = int(input("Enter the value of N: "))
squares = [x**2 for x in range(1, N+1)]
print("Squares:", squares)

# (c) Form a list of vowels
word = input("Enter a word: ")
vowels = [char for char in word if char in 'aeiou']
print("Vowels in word:", vowels)

# (d) List ordinal value
word2 = input("Enter ordinal word: ")
ordinals = [ord(char) for char in word2]
print("Ordinal values of word:", ordinals)
