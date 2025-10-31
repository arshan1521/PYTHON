import math

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end+1):
    if 1000 <= num <= 9999 and all(int(d)%2==0 for d in str(num)):
        if math.isqrt(num)**2 == num:
            print(num)
