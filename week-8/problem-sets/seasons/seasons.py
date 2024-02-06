from datetime import date, datetime, timedelta
import inflect
import re
import sys

p = inflect.engine()

class Date:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    @classmethod
    def get(cls):
        date_str = (input("Date of Birth: "))
        date_obj = cls.convert(date_str)
        return date_obj

    @classmethod
    def convert(cls, date_str):
        if m := re.match(r"^([0-2][0-9][0-9][0-9])-([0-1]?[0-9])-([0-3]?[0-9])$", date_str):
            birth_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            current_date = date.today()
            time_lapse = current_date - birth_date
            minutes = int(time_lapse.total_seconds() / 60)
            output = p.number_to_words(minutes).replace(" and", "")
            return output.capitalize()

        else:
            sys.exit("Invalid date")

def main():
    birth_date = Date.get()
    print(f"{birth_date} minutes")

if __name__ == "__main__":
    main()
