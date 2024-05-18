# This is a basic and easy tip calculator program

bill = int(input("What was the total bill? "))
tipPercent = int(input("How much tip would you like to give? 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))

totalBill = bill + (bill * tipPercent / 100 )
finalCalculation = round((totalBill / people), 2)
stringConversion = str(finalCalculation)
input("Each person should pay: " + stringConversion)


