# Rent calculator for flatmates

def get_inputs():
    rent = float(input("Enter rent of one month: "))
    elect_unit = int(input("Enter total electricity units this month: "))
    charge_per_unit = float(input("Enter charge per unit: "))
    food_expenses = float(input("Enter total food expenses this month: "))
    other_expenses = float(input("Enter other expenses (if any): "))
    total_person = int(input("Enter total number of persons: "))
    return rent, elect_unit, charge_per_unit, food_expenses, other_expenses, total_person

def calculate_expenses(rent, elect_unit, charge_per_unit, food_expenses, other_expenses, total_person):
    elect_bill = elect_unit * charge_per_unit
    total_expenses = elect_bill + rent + food_expenses + other_expenses
    bill_per_person = total_expenses / total_person
    return elect_bill, total_expenses, bill_per_person

def display_result(rent, food_expenses, elect_bill, total_expenses, bill_per_person):
    print("\n=== Calculation Breakdown ===")
    print(f"Rent: Rs. {rent:,.2f}")
    print(f"Food: Rs. {food_expenses:,.2f}")
    print(f"Electricity Bill: Rs. {elect_bill:,.2f}")
    print(f"Total Expense: Rs. {total_expenses:,.2f}")
    print(f"Per Person Share: Rs. {bill_per_person:,.2f}")

# Main code
print("=== Rent Calculator ===")
rent, elect_unit, charge_per_unit, food_expenses, other_expenses, total_person = get_inputs()
elect_bill, total_expenses, bill_per_person = calculate_expenses(rent, elect_unit, charge_per_unit, food_expenses, other_expenses, total_person)
display_result(rent, food_expenses, elect_bill, total_expenses, bill_per_person)

