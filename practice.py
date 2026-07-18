def factorial(num):
    fact=1
    for y in range(1, num+1):
        fact = fact * y
    print(fact)

factorial(5)