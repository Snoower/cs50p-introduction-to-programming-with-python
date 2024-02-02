import sys
import csv
from tabulate import tabulate

list = []

def main():
    try:
        if len(sys.argv) <= 1:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif ".csv" not in sys.argv[1]:
            sys.exit("Not a CSV file")
        else:
            with open(sys.argv[1]) as table:
                reader = csv.reader(table)
                headers = next(reader)
                for row in reader:
                    list.append(row)
            print(tabulate(list, headers=headers, tablefmt='grid'))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
