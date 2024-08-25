"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those value
"""

def info(firstname,lastname,age):
    info_dict={
        "firstname":firstname,
        "lastname":lastname,
        "age":age
    }
    return info_dict

first_name=input(print("Please enter first name"))
last_name=input(print("Please enter last name"))
age=input(print("Please enter age "))

person_Data=info(first_name,last_name,age)

print(person_Data)