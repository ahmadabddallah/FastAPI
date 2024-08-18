"""
Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.
"""

initial_amount=50
item_to_buy=15
tax=.03

reminder_money=initial_amount-(item_to_buy+(item_to_buy*tax))

print(reminder_money)