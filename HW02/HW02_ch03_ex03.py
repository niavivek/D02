#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.

def print_func1():
    print ('+','- '*4 +'+','- '*4 +'+')

def print_func2():
    print ('|',' '*8+'|',' '*8+'|')

def print_box():
    print_func1()
    print_func2()
    print_func2()
    print_func2()
    print_func2()
    
def print_func():
    print_box()
    print_box()
    print_func1()
    


# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body
def print_func12():
    print ('+','- '*4+'+','- '*4+'+',end=' ')
    print ('- '*4+'+','- '*4+'+')

def print_func22():
    print ('|',' '*8+'|',' '*8+'|',end=' ')
    print (' '*8+'|',' '*8+'|')
    
def print_func_box():
    print_func12()
    print_func22()
    print_func22()
    print_func22()
    print_func22()
    
def print_func_four():
    print_func_box()
    print_func_box()
    print_func_box()
    print_func_box()
    print_func12()










# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    print_func()
    print_func_four()
    



if __name__ == "__main__":
    main()
