def main():
    fraction = get_fraction("Fraction: ")
    if fraction == 'F':
        print("F")
    elif fraction == 'E':
        print("E")
    else:
        print(f"{fraction}%")

def get_fraction(prompt):
    while True:
        try:
            fraction = input(prompt)
            values = fraction.split('/')
            variable1, variable2 = map(int, values)
            percentage = round(variable1/variable2 * 100)
            if 99 <= percentage <= 100:
                return 'F'
            elif percentage <= 1:
                return 'E'
            elif percentage > 100:
                pass
            else:
                return percentage
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
