# Factorial without recursion
#DEEPAK L GOWDA
#1RUV25BCA0027

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)
