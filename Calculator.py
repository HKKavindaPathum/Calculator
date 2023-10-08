# Declare a list to store previous operations
calculation_history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

def select_op(choice):
    if choice == '#':
        return -1
    elif choice == '$':
        return 0
    elif choice == '?':
        history()
        
        
    elif choice in ('+', '-', '*', '/', '^', '%'):
        while True:
            num1s = str(input("Enter first number: "))
            print(num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1
            try:
                num1 = float(num1s)
                break
            except ValueError:
                print("Not a valid number, please enter again")
                continue

        while True:
            num2s = str(input("Enter second number: "))
            print(num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1
            try:
                num2 = float(num2s)
                break
            except ValueError:
                print("Not a valid number, please enter again")
                continue
            
            

        result = 0.0
        last_calculation = ""
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            if num2 == 0.0:
                print("float division by zero")
                print(num1,"/",num2,"= None")
                result='None'
            else:
                result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            if num2 == 0.0:
                print("float division by zero")
                print(num1,"/",num2,"= None")
                result='None'
            else:
                result = remainder(num1, num2)
        else:
            print("Something Went Wrong")



        last_calculation = "{0} {1} {2} = {3}".format(num1, choice, num2, result)
        if num2 != 0.0:
            print(last_calculation)
            
        # Save the operation in the history list
        calculation_history.append(last_calculation)

    else:
        print("Unrecognized operation")

def history():
    if not calculation_history:
        print("No past calculations to show")
    else:
        for i, operation in enumerate(calculation_history, start=1):
            print(f"{operation}")

while True:
    print("Select operation.")
    print("1.Add      : +")
    print("2.Subtract : -")
    print("3.Multiply : *")
    print("4.Divide   : /")
    print("5.Power    : ^")
    print("6.Remainder: %")
    print("7.Terminate: #")
    print("8.Reset    : $")
    print("8.History  : ?")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if select_op(choice) == -1:
        # program ends here
        print("Done. Terminating")
        exit()
