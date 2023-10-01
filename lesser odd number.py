n = int(input("Enter a number:  "))
x = int(input("Even: 0\n Odd: 1\n "))
y = 0
for i in range(x,n, 2):
    print(i)
    y = y + i

print("Total of numbers: ",y)   
