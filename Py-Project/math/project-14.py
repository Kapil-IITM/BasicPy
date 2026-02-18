# EMI - Calculator 

def get_emi_inputs():
    principal = float(input("Loan amount (Rs): "))
    rate = float(input("Annual rate (%): ")) / 12 / 100
    months = int(input("Tenure (months): "))
    return principal, rate, months

def calculate_emi(p, r, n):
    emi = p * r * (1+r)**n / ((1+r)**n - 1)
    return emi

p, r, n = get_emi_inputs()
emi = calculate_emi(p, r, n)
print(f"Monthly EMI: Rs. {emi:.2f}")
