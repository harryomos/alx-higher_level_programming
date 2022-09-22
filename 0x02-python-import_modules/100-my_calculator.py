#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv, exit
    argc = len(argv) - 1
    operators = "+-*/"
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if not argv[2] in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = (int)(argv[1])
    b = (int)(argv[3])
    operator = f"{argv[2]}"
    if operator == "+":
        res = calc.add(a, b)
    elif operator == "-":
        res = calc.sub(a, b)
    elif operator == "*":
        res = calc.mul(a, b)
    elif operator == "/":
        res = calc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a:d} {argv[2]} {b:d} = {res}")
