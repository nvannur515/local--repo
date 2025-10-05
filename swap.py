try:
    a = int(input("Enter first number: dddd))
    b = int(input("Enter second number: "))
    print(f"Before swapping: a={a}, b={b}")
    a, b = b, a
    print(f"After swapping: a={a}, b={b}")
except ValueError:
    print("Please enter valid integers.")
   