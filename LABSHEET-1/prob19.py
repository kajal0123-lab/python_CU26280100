p = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan period in years: "))

months = years * 12
r = annual_rate / 1200

if p < 0 or years <= 0 or annual_rate < 0:
    print("Enter valid loan details")
elif r == 0:
    emi = p / months
    print("Monthly EMI:", round(emi, 2))
else:
    emi = p * r * (1 + r) ** months / ((1 + r) ** months - 1)
    print("Monthly EMI:", round(emi, 2))