import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if twelve_hour := re.search(r"^([0-9][0-2]?):?([0-5]?[0-9])?\s(AM|PM)\sto\s([0-9][0-2]?):?([0-5]?[0-9]?)\s(AM|PM)$", s):
        if int(twelve_hour.group(1)) > 12 or int(twelve_hour.group(4)) > 12:
            raise ValueError
        first_time = create_time(int(twelve_hour.group(1)), twelve_hour.group(2), twelve_hour.group(3))
        second_time = create_time(int(twelve_hour.group(4)), twelve_hour.group(5), twelve_hour.group(6))
        return first_time + " to " + second_time
    else:
        raise ValueError

def create_time(hour, minute, am_pm):
        if am_pm == "PM":
            if hour == 12:
                 hour = 12
            else:
                 hour += 12
        else:
            if hour == 12:
                 hour = 0

        if minute == None:
             minute = ":00"
             time = f"{hour:02}{minute:02}"
        else:
             time = f"{hour:02}:{minute:02}"

        return time


if __name__ == "__main__":
    main()
