# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1:
# https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2:
# https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

bill = float(input("Enter your total bill: $"))

tip_percentage = int(input("Enter the tip percentage that you want to give: "))

persons_number = int(input("How many people to split the bill? "))

per_person_bill = "{:.2f}".format(round((bill / persons_number) * (1 + (tip_percentage / 100)), 2))

print(f"Each person should pay: ${per_person_bill}")
