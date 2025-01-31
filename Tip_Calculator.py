#code below this line

bill = float(input("How much was the bill? "))
tip = float(input("How much do you want to tip? 10, 12, or 15 percent?"))
num_people = int(input("How many people will be splitting the bill? "))

if tip == 10:
    tip = .1
elif tip == 12:
    tip = .12
elif tip == 15:
    tip = .15
else:
    print("Sorry that isn't a selection")
    exit()

total = (bill + bill * tip) / num_people
total = round(total,2)
print(f"Each person should pay: ${total:.2f}")
#print("$" + str(bill))