def add(a,b):
    return a+b
def subtract(a,b):   
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def calculator():
    operations_dict={"+":add,"-":subtract,"*":multiply,"/":divide} 
    number1=float(input("Enter first number:"))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an operation:")
        number2=float(input("Enter second number:"))
        calculator_function=operations_dict[op_symbol] 
        output=calculator_function(number1,number2)  
        print(f"{number1} {op_symbol} {number2} = {output}") 
        calcultor_continue=input(f"Enter 'y' to calculation continue with {output} or'n' to start a new caalculaation or 'x' to exit").lower()
        if calcultor_continue=='y':
            number1=output
        elif calcultor_continue=='n': 
            continue_flag=False
            calculator()
        else:
            continue_flag=False
            print("Rest Position") 
calculator()              