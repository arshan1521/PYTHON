numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))


result = []
for n in numbers:
    if n > 100:
        result.append('over')
    else:
        result.append(n)

print("Modified list:", result)
