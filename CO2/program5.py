n = int(input("Enter N: "))
for i in range(1, n+1):
    line = ""
    for j in range(1, i+1):
        line += str(i*j) + " "
    print(line.strip())
