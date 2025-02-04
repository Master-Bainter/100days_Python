#Code below this line

number = int(input("Please input a number: "))
even_odd = number % 2

if even_odd == 0:
    print(f"The number is even: {number}" )
else:
    print(f"The number is odd: {number}")