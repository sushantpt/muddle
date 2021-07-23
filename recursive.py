# recursive way to find factorial no.def factorial(n):
    if n == 0:
        return 1
    else:
        factor = n * factorial(n-1)
        return factor
user_input = (int(input("Enter number:")))
    
factorial(user_input)
