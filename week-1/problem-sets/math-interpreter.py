def main():
    expression = input("Expression : ").lower().strip()
    calculate(expression)

def calculate(ex):
    x, y, z = ex.split(" ")
    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/":
        print(float(x) / float(z))
    else:
        print("Incorrect format. Please try again!")

main()
