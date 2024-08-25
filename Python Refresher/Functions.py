"""
Functions
"""
from typing import final

"""
def my_functions():
    print("Inside my function")

def print_my_name(name,last_name):
    print(f"Hello {name}{last_name}")

def print_color_red():
    color="Red"
    print(color)

print_my_name("ahmed","abdallah")
"""

"""
def print_numbers(highest_number,lowest_number):
    print(highest_number)
    print(lowest_number)

# you can in python specific the parameter
print_numbers(lowest_number=3, highest_number=10)

def multiply_numbers(a,b):
    return a*b

solution=multiply_numbers(10,6)
print(solution)

def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)


number_list= [1,2,3,4,5]
print_list(number_list)
"""
def buy_item(cost_of_items):
    return cost_of_items+add_tax_to_item(cost_of_items)

def add_tax_to_item(cost_of_items):
    current_tax_rate=.03
    return cost_of_items*current_tax_rate

final_cost=buy_item(50)
print(final_cost)