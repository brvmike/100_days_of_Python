print("Welcome to the tip calculator\n")

total_bill = float(input("What was the total bill? $"))
get_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

percentage_tip = float(get_tip)

number_of_customers = int(input("How many people should split the bill? "))

new_total_bill = total_bill + (total_bill * (int(get_tip)/100))
split_division = new_total_bill / number_of_customers

final_split_division = round(split_division, 2)

print(f"Each person should pay: ${final_split_division:.2f}\n")
