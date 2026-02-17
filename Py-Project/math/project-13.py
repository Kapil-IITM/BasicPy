#Savings Goal Calculator
def get_savings_inputs():
    goal = float(input("Savings goal (Rs): "))
    monthly_save = float(input("Monthly savings (Rs): "))
    return goal, monthly_save

def calculate_months(goal, monthly):
    months = goal / monthly
    return months

goal, monthly = get_savings_inputs()
months_needed = calculate_months(goal, monthly)
print(f"Months needed: {months_needed:.1f}")
