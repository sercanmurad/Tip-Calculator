
print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
percantage=int(input("What percantage would you like to give ? 10,12 or 15? "))
bill_percantage=total_bill*(percantage/100)
bill=total_bill+bill_percantage
people=int(input("How many people to split the bill?"))
each_person=round(bill/people, 2)
each_person="{:.2f}".format(each_person)
print(f"Each person should pay:${each_person}")
