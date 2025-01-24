a = int(input("Enter the Number = "))
sum = 0

for i in range(0,a+1):
    if i % 2 != 0:
        sum = sum + i

print(sum,"= Sum of all Odd Number.")