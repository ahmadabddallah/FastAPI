
"""
Dictionaries
"""

user_dictionary={
    "username":"AAF",
    "name":"Ahmed",
    "age":25
}
"""
user_dictionary["Married"]=True
user_dictionary.pop("age")
user_dictionary.clear()
print(user_dictionary)

# to iterate over it

for x,y in user_dictionary.items():
    print(x,y)
for x in user_dictionary:
    print(x)
"""
print(user_dictionary)

user_dictionary2=user_dictionary.copy()

user_dictionary2.pop("age")
print(user_dictionary2)

#user_dictionary2=user_dictionary
