# Cristian Garcia
# 11/05/24

# Problem 1 say_my_name takes a name and has a 50/50 chance of giveing you a nice or mean message. multiply_if taskes a list of random numbers and determins if it should be mutipled by 5. unique_elemtns takes a list of numbers and returns them in assending order.


import random # Imports random module
import resources # Imports resources module

def say_my_name(name): # Define the function say_my_name that takes a name as input

    # Use random.choice to randomly choose one of two greeting
    choice = random.choice ([f"Hello {name}", f"Have a terrible day {name}"])
    print(choice)

# Calls the funtion
say_my_name("Cristian")



# Define the function multiply_if that processes a list of random numbers
def multiply_if():

    # Generate a list of 10 random numbers between 1 and 50
    random_list = [random.randint(1, 50) for _ in range(10)]

    # Stores list of random numbers numbers
    new_numbers = []

    # Repeat over each number in the random_list
    for num in random_list:

        #Calls the lets_see function
        # It checks if the number is within a certain range
        if resources.lets_see(num):

            # If number is in range multiply it by 5
            new_numbers.append(num * 5)
        else:

            # If number is not in range do not multiply and add it to list as is
            new_numbers.append(num)
    return new_numbers

# Calls the multiply_if function and store the result in updated_list   
updated_list = multiply_if()
print(updated_list)



# Define the function unique_elements that takes a list as input
def unique_elements(list):

    # A list that sores unique_elements
    unique_list = []

    # Repeat through each item in the input list
    for item in list:

        # Check if item is not in unique list 
        if item not in unique_list:

            # If item is not in the unique list add it to it
            unique_list.append(item)

            # Return the unique_list sorted in ascending order
    return sorted(unique_list)

list = [1, 1, 5, 4, 4, 3, 2, 6]

# Call the unique_elements function with the input_list and store the result in the variable result
result = unique_elements(list)
print(result)