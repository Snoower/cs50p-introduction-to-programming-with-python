import sys
import csv

def main():
    students = []
    try:
        if len(sys.argv) <= 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            if ".csv" not in sys.argv[1]:
                sys.exit("Not a CSV file")
            else:
                sys.exit("Too many command-line arguments")
        else:
            with open(sys.argv[1]) as table:
                reader = csv.DictReader(table)
                for row in reader:
                    first_name = row['name'].split()[1]
                    last_name = row['name'].split()[0].replace(",", "")
                    students.append({"first": first_name, "last": last_name, "house": row['house']})
            output_file = f"{sys.argv[1]}".replace("before","after")
            field_names = students[0].keys()
            with open(output_file, 'w') as after:
                writer = csv.DictWriter(after, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(students)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
