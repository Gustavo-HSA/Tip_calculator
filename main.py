print("Welcome to the tip calculator!!")
bill = float(input("Whats was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? ")) 
tip = bill * (percentage / 100)
bill_with_tip = bill + tip
bill_splited = round(bill_with_tip / people, 2)

print(f"Each person should pay: ${bill_splited}")

