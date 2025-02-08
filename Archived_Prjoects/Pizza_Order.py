#Code below this line

pizza_size = input("What size pizza would you like? S, M, or L? ").lower()
pizza_cost = int()
pepperoni = input("Do you want pepperoni? Y or N: ").lower()
s_pep_cost = 2
m_l_pep_cost = 3
ex_cheese = input("Do you want extra cheese? Y or N: ").lower()
cheese_cost = 1

if pizza_size == "S".lower():
    pizza_cost = 15
    if pepperoni == "Y".lower():
        pizza_cost = pizza_cost + s_pep_cost
    else:
        pizza_cost = pizza_cost
    if ex_cheese == "Y".lower():
        pizza_cost = pizza_cost + cheese_cost
    else:
        pizza_cost = pizza_cost
elif pizza_size == "M".lower():
    pizza_cost = 20
    if pepperoni == "Y".lower():
        pizza_cost = pizza_cost + m_l_pep_cost
    else:
        pizza_cost = pizza_cost
    if ex_cheese == "Y".lower():
        pizza_cost = pizza_cost + cheese_cost
    else:
        pizza_cost = pizza_cost
else:
    pizza_cost = 25
    if pepperoni == "Y".lower():
        pizza_cost = pizza_cost + m_l_pep_cost
    else:
        pizza_cost = pizza_cost
    if ex_cheese == "Y".lower():
        pizza_cost = pizza_cost + cheese_cost
    else:
        pizza_cost = pizza_cost

print(f"${pizza_cost}")