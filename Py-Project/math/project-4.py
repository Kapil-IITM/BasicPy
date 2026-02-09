# Find Factorial of a number

num = int(input("Enter a number :- "))
fact = 1
if num == 0:
    print(f'factorial of {num} is 1')
elif num < 0:
    print(f'factorial of {num} does not exist ')
else:
    for i in range(1,num+1):
        fact = fact * i
    print(f"factorial of {num} is {fact} ")