
num = 0

for number in range(1, 101):
    num += number
    if num % 3 == 0:
        print("Fizz")
    print(num)