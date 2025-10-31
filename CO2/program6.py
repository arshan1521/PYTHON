from collections import Counter

s = input("Enter a string: ")
freq = Counter(s)
for k, v in freq.items():
    print(f'{k}: {v}')
