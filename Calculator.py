def add(n1, n2):
    return n1+n2


def substract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


# creating a dictionary which will store these operations
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
# creating a calculator function


def calculator():
    # getting inputs
    num1 = float(input("What's the first number:"))
    for symbol in operations:
        print(symbol)
    # creating a flag
    should_continue = True
    # Iterating through the loop
    while should_continue:
        operation_symbol = input("Pick a symbol from above: ")
        num2 = float(float(input("What's the next number: ")))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation:") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
