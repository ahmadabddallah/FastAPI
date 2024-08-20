"""
For & While Loops
"""
def summation(my_list):
    sum=0
    for x in my_list:
        sum+=x
    return sum

my_list=[1,2,3,4,5]
"""
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
"""

"""


for iterator in range(3,6):
    print(iterator)

   # print(iterator)

print(summation(my_list))
"""

"""
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for x in days_of_week:
    if x=="Monday":
        break
    print(f"Happy {x}!")
"""

i =0
while i<5:
    i+=1;
    print(i)