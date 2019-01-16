#Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.
import random

random_numbers = [5,7,8,3,45,6,7,8]
print(random_numbers)

# With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is [2, 5], the final list will be [4, 25].

new_list = []

new_list= [ num **2 for num in random_numbers]

print(new_list)
