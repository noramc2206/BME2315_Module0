# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX Write your pseudocode here XXX

INPUT integer N

SET sum to 0 
SET fib1 to 0
SET fib2 to 1

SET i = 0

WHILE i < N
    
     SET sum to sum + fib1

     SET nextFib to fib1 + fib2
     SET fib1 to fib2 
     SET fib2 to nextFib

     SET i to i + 1 
END WHILE  

OUTPUT sum 

"""
# Citation: I used AI to help me understand the structure of the fibonacci calculation. 
# Ai also helped me in correctly aligning my pseudocode with that structure. 
# The final pseudocode was done by me. 

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 # sets a number for how many fibonacci numbers to print 

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # sets a value for how long the while loop will run
total = 0 # sets a value for the sum of the fibonacci numbers 

while count < N: # starts a while loop for creating a sum of the fibonacci numbers 
    total = total + a # should set the sum to itself plus the first fibonacci number(corrected from b to a) 

    next_value = a + b # finds the next fibonacci number in the sequence by adding the first two together
    a = b # sets the first fibonacci number to the value of the next number 
    b = next_value # resets the second fibonacci number to the value of itself plus the number prior 

    count = count + 1 

print(total) # outputs the final sum 

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
import numpy as np #importing the numpy library

data = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] #create a list with the first ten fibonacci sequence numbers 
arr = np.array(data) #convert the list into an array 

fib_std = np.std(arr) #calculate the standard deviation using numpy library 
print(fib_std) #print the standard deviation

# Citation: I used AI to learn how to import and use the numpy library for calculating standard deviation
# the final code/comments were written by me 

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.
def fibonacci_sum(N): 
    fib1 = 0 # sets first fibonacci number
    fib2 = 1 # sets second fibonacci number
    count = 0 # sets value for how long the while loop will run
    total = 0 # sets value for the sum of the fibonacci numbers 

    while count < N: # starts a while loop for creating a sum of the fibonacci numbers 
        total = total + fib1 # sets the sum to itself plus the first fibonacci number 

        next_value = fib1 + fib2 # finds the next fibonacci number in the sequence by adding the first two together
        fib1 = fib2 # sets the first fibonacci number to the value of the next number 
        fib2 = next_value # resets the second fibonacci number to the value of itself plus the number prior 

        count = count + 1
    return total # returns the sum of the first N fibonacci numbers 

N_vals = [5, 10, 15, 20, 25, 30] #creates list for the N values 
sums = [ ] #creates list to be filled with sums from the N values 

for N in N_vals: #for loop that goes through the function for each N value 
    sums.append(fibonacci_sum(N))

print(sums) #prints the sums as a list 

# Citation: I used AI to help me understand how to structure the Fibonacci
# function and use a loop to calculate and store the sums for different N values.
# The final code was written by me.

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 #changed from str to int to allow for comparison in while loop
    b = 1 #changed from str to int to have correct fibonacci calculations
    index = 0 #defines the index value 

    while a <= limit: #type error because a was a str while limit was an int
        next_value = a + b
        a = b
        b = next_value
        index += 1 #UnboundLocalError because the index is being used before it has been defined with a value 

    return index

# Citation: I used AI to help me understand the error messages. 
#  The final corrections/comments were written by me.

result = find_fib_above_limit(50) 
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 != 0:  # This line checks if the Fibonacci number is ODD!
            total = total + b #fixed this part to correctly increment the total
        a, b = b, a + b
    return total


# Add your test cases here
print(sum_even_fib(10)) # returned 8 but should be 10 
print(sum_even_fib(1))# returned 0 but should be 2 
print(sum_even_fib(7)) #returned 2 but should be 10

# Citation: I used AI to help me understand how to test the function with
# different inputs and identify the errors in the original code. The final
# test cases and corrected code were written by me.
# %%

