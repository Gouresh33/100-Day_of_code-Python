from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

calculator_oper = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    print(logo)
    should_con = True
    first_num = float(input("Enter first number: "))

    while should_con:

        for symbol in calculator_oper:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        second_num = float(input("Enter second number: "))
        answer = calculator_oper[operation_symbol](first_num, second_num)
        print(f"{first_num} {operation_symbol} {second_num} = {answer}")
        yes_or_no = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if yes_or_no == 'y':
            first_num = answer
        else:
            should_con = False
            print("\n" * 30)
            calculator()

calculator()