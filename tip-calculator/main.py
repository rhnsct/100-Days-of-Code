print("Welcome to the tip calculator.")

no_tip_bill = input("What is the total bill? $")
percentage_tip = input("What percentage tip would you like to give? ")
number_people = input("How many people are splitting the bill? ")

bill_float = float(no_tip_bill)
percentage = int(percentage_tip)
people_int = int(number_people)

bill_total_split = ((percentage / 100) + 1) * bill_float / people_int
bill_2dp = "{:.2f}".format(bill_total_split)

print(f"Each person should pay: ${bill_2dp}")