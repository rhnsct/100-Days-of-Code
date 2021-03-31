from art import logo
import os

def clear():
    os.system('clear')


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add, 
    '-': subtract, 
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue == True:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1, num2)

        print(f"\n{num1} {operation_symbol} {num2} = {answer}\n")

        if input(f"Type 'y' to continue calculating with {answer} or 'n' to start new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()
            
    

calculator()

