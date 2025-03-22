 # Stage 1: creating 4 funtiocns, a dictionary with 4 operations, testing how the operations work 
# when we use the functions by adding () with arguments

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,   
}

for symbol in operations:
    print(symbol)
    
# stage 2 and complete code


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,   
}

def calculate():

    continue_calculations = True
    
    try:
        num1 = float(input('Enter the first number: '))
    except ValueError:
        print('Invalid entry,please, start over.')
        return
    

    while continue_calculations:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Enter the opertion you would like to perform: ')
        
        if operation_symbol not in operations:
            print('Invalid entry,please, start over.')
            return
        try:
            num2 = float(input('Enter the second number: '))
        except ValueError:
            print('Invalid entry,please, start over.')
            return 
        
        answer = (operations[operation_symbol](num1, num2))
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        should_continue = input(f"To continue calculation with {answer}, enter 'y', to restart, enter 'n'").lower()

        if should_continue == 'y':
            num1 = answer

        elif should_continue == 'n':
            continue_calculations = False
            print('\n' * 100)
            calculate()
        else:
            print('Invalid entry, start over')
            return
calculate()

# Let's see how it would work if the claculate() took positional arguments: 

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-':subtract,
    '*':multiply,
    '/': divide,
}

def calculate(num1=None, operation_symbol=None, num2=None):
    # If the arguments are not provided, ask the user for input
    if num1 is None:
        try:
            num1 = float(input('Enter the first number: '))
        except ValueError:
            print('Invalid entry, please start over.')
            return

    if operation_symbol is None:
        operation_symbol = input('Enter the operation you would like to perform: ')
        if operation_symbol not in operations:
            print('Invalid operation, please start over.')
            return

    if num2 is None:
        try:
            num2 = float(input('Enter the second number: '))
        except ValueError:
            print('Invalid entry, please start over.')
            return

    # Perform the calculation
    answer = operations[operation_symbol](num1, num2)
    if answer is None:
        return

    print(f'{num1} {operation_symbol} {num2} = {answer}')

# Example of calling the function with arguments
calculate()
