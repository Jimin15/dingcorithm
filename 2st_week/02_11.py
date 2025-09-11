
# factorial(n) = n*factorial(n-1)
# factorial(n-1) = n*factorial(n-2)
# n*factorial(1) = 1
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)



print(factorial(5))