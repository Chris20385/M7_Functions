# Cristian Garcia
# 11/05/24

# Problem 2 lets_see takes a number and tells you if it is in the range. main prints a message in resources when ran in the file directly. And prints another mesage if not ran in the file directly.


# Define the function lets_see that takes a parameter number
def lets_see(number):

    # Check if the number is in the range of 20 to 30
    if number in range(20,31):
        print (f"{number} is in range")
        return True
    else:
        print (f"{number} is not in range")
        return False


# Call the lets_see function with 27 as the argument
lets_see(27)
    


# Define the main function when running file directly 
def main():        
    print("This only happens when I run the file directly")

print("I will always get printed")

# Checks if file is being ran directly
if __name__ == "__main__":

    # If file is ran directly it calls the main function
    main()