import sys

def main():
    try:
        if len(sys.argv) <= 1:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif ".py" not in sys.argv[1]:
            sys.exit("Not a Python file")
        else:
            print(count(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")

def is_whitespace(line):
    return not line.strip()

def is_comment(line):
    return line.strip().startswith("#")

def count(file):
    count = 0
    with open(file, 'r') as program:
        for line in program:
            if not is_whitespace(line) and not is_comment(line):
                count += 1
    return count


if __name__ == "__main__":
    main()
