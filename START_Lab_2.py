#new
def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    pass
#Define a function.
def isPalindrome(string):
    if (string == string[::-1]) :
        return ("The string is a palidrome")
    else:
        return ("The string is not a palidrome")
#Enter input string.
string = input ("Enter string: ")
print(isPalindrome(string))

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    pass

def fib(index):
    if index <= 2:
        return [0, 1][:index]

    sequence = fib(index - 1)

    sequence.append(sum(sequence[-2:]))

    return sequence

print(fib(9))

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    pass

def count_substring(str1, str2):
    i=len(str2)
    count=0
    for i in range(len(str1)-len(str2)+1):
        if(str1[i:i+len(str2)] == str2 ):      
            count+=1
    return count  
str1 = input ("Enter your sentence: ")
str2 = input ("Enter the sub-string you want to count: ")
print (count_substring(str1, str2))

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    pass

    return sum_list

    #Input: input_list 1 : [1, 3, 4, 6, 8]
#            input _list 2 : [4, 5, 6, 2, 10]
#Output: output_list[5, 8, 10, 8, 18]
#Explanation: Every element of the input_list1 is added to its respective element 
#of input_list2 and got the output_list.

import numpy as np

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print("list1: " + str(list1))
print("list2: " + str(list2))

res_array = np.array(list1) + np.array(list2)    
res_list = res_array.tolist()
print(res_array)

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = None

    return password

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    pass
import re
    #password = input("insert password: ")
    
    if len(password) < 8:
        return ("The password must contain at least 8 characters")
          
    if not re.search("[A-Z]", password):
        return ("The password must contain at least one uppercase letter")
           
    if not re.search("[a-z]", password):
        return ("The password must contain at least one lowercase letter")
        
    if not re.search("[0-9]", password):
        return ("The password must contain at least one number")
            
    else:
        return ("Password is valid")

password = input("insert password: ")
    
print(isValidPassword(password))


