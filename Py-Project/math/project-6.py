# find the largest among three two-digit numbers 



num1 = int(input("Enter first two-digit number:- "))
num2 = int(input("Enter second two-digit number:- "))
num3 = int(input("Enter third two-digit number:- "))


def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print("The largest is:- ", find_largest(num1, num2, num3))