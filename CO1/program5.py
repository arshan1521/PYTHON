names = input("Enter names separated by spaces: ").split()
count_a = 0
for name in names:
    count_a += name.lower().count('a')
print(count_a)
