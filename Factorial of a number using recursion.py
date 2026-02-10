# Factorial using Recursion
#deepak l gowda
#1rua25bca0027

def factorial(n):2
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))
print("Factorial =", factorial(num))
