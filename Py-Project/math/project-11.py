# Take a user input and make a program for multiplication table 

num = int(input("Enter a number :- "))

print(f"Multiplication Table for {num} :")
print("-" * 30)

for i in range(1,11):
    print(f"{num} * {i} = {num * i }")