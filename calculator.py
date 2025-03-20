"""
The Calculator library allows you to perform basic calculation operations between two integers.
"""

def add(arg1,arg2):
    try:
        return int(arg1)+int(arg2)
    except ValueError: 
        print("One of the arguments is not an integer.") 

def substract(arg1,arg2):
    try:
        return int(arg1)-int(arg2)
    except ValueError: 
        print("One of the arguments is not an integer..") 


def multiply(arg1,arg2):
    try:
        return int(arg1)*int(arg2)
    except ValueError: 
        print("One of the arguments is not an integer..") 

def divide(arg1,arg2):
    try:
        return int(arg1)/int(arg2)
    except ValueError: 
        print("One of the arguments is not an integer..") 
    except ZeroDivisionError:
        print("You devide by 0.")

def ope(operateur,arg1,arg2):   
    if operateur=='+':
        return add(arg1,arg2)        
    elif operateur=="-":
        return substract(arg1,arg2)
    elif operateur=="x":
        return multiply(arg1,arg2)
    elif operateur=="/":
        return divide(arg1,arg2)
    else:
        print("Unknown operator {}.".format(operateur))