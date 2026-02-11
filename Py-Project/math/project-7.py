# Python program to check leap year 
num = int(input("Enter a year :- "))
def leap_year(num):
    if num % 4 == 0 and (num % 100 != 0 or num % 400 == 0):
        print(f"{num} is a Leap year ")
    else:
        print(f"{num} is not a Leap year")

leap_year(num)
