def main():
    while True:
        fraction = convert("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split('/')
    if int(x) > int(y) or x.isdigit() is False or y.isdigit() is False:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    else:
        tank = round(int(x)/int(y) * 100)
        return tank

def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif percentage <= 1:
        return "E"
    elif percentage > 100:
        pass
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
