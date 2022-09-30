diameter = int(input("Enter diameter of pizza in inches:"))
pizza_cost = diameter / 2
pizza_cost_add = pizza_cost + 1.75
subtotal = pizza_cost_add * 1.13
rounded = subtotal * 100
rounded2 = round(rounded)
final_cost = rounded2 / 100
print("The cost of the pizza is:")
print(final_cost)
