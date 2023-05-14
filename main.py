print("Bill Splitting Bot!")
print(
    "put in the total bill, how many people you're splitting it between, and what percentage tip you would like to leave, and let the bot do the rest!"
)
print()

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = float(input(" what % tip would you like to leave?: "))
myBill += myBill * (tip / 100)
answer = myBill / numberOfPeople
print("You all owe", round(answer, 2))
