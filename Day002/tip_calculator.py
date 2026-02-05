# Project_002
print("--- Welcome to the Tip Calculator! ---")
total_bill = float(input("Enter the Total Bill: $"))
tip_pay = int(input("How much tip would you like to give? 10%, 12% or 15%: "))
split_tip = int(input("How many people to split the bill: "))

calc_tip = (total_bill * (tip_pay / 100) + total_bill) / split_tip
calc_tip = round(calc_tip,2)
print(f"Each person should pay ${calc_tip}")
