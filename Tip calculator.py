print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill? $"))
Tip = int(input("What percentage tip would you like to give?"))
People = int(input("How many people to split the bill?"))
tip_percentage = Tip / 100
tip_total = Bill * tip_percentage
total_bill =Bill+tip_total
final =round(total_bill, round(2))
print(total_bill/People)






