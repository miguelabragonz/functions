'''
@author: amayamunoz
'''

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by 
calling the function and printing what is returned
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def subtractions(num1,num2):
    diOfNumbers = num2 - num2
    return diOfNumbers 
#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def division(num):
    finalNumber = ((num/2)*77) + 10000
    return finalNumber 
#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def equalCheck(num1, num2):
    if num1 == num2:
        return"True"
    else:
        return"False"
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def checkGreater(num1, num2):
    if num1> num2:
        return num1
    elif num1 == num2:
        return num1
    else:
        return num2
#5) Define a function that takes in two words and returns a string that contains both words combined.
str1 = ""
str2 = ""
def combineString(str1, str2):
    finalString = str(str1 + "" + str2)
    return finalString
#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def coolNum(num1, num2, num3):
    if num1 == num2 or num1 == num3:
        finalAnswer = "True"
    else:
        finalAnswer = "False"
        return finalAnswer
#7) Define a function that prints your name.
def myName(name):
    return name 

name = ""
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
favoriteColor = "blue" 

def checkColor(newColor):
    if newColor == favoriteColor:
        answer = ("That's my fovorite color")
    else:
        answer = ("That's not my favorite color. Try Again")
    return answer 
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.

'''YOUR OWN FUNCTION'''

#10) Create your own function that solves any problem you can think of.

def subtraction(num1,num2):
    difference = num1 - num2
    return difference
        



