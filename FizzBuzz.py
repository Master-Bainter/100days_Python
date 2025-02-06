
num = 0

for number in range(1, 101):
    if number % 3 == 0:
        print("Fizz")
    else:
        print(number)
    if number % 5 == 0:
        print("Buzz")
    else:
        print(number)