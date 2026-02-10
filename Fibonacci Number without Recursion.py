# Fibonacci Number without Recursion
#DEEPAK L GOWDA
#1RUA25BCA0027

num = int(input("Enter term number: "))

a = 0
b = 1

if num == 0:
    print("Fibonacci term =", 0)

elif num == 1:
    print("Fibonacci term =", 1)

else:
    for i in range(2, num + 1):
        c = a + b
        a = b
        b = c

    print("Fibonacci term =", b)
