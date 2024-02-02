def main():
    greeting = input("Greeting: ")
    print_value = value(greeting)
    print(f"${print_value}")


def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
