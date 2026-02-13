# Prime Number Check

num = int(input("Enter a number :- "))

if num <= 1:
    print(f"{num} is not prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
