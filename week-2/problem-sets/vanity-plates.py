def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if two_letter_check(s) and length_check(s) and number_check(s) and second_number_check(s) and third_number_check(s) and character_check(s):
        return True
    else:
        return False


def two_letter_check(s):
    # “All vanity plates must start with at least two letters.”
    for c in s[0:1]:
        if c in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
             return True
        else:
             return False

def length_check(s):
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if 2 < len(s) <= 6:
        return True
    else:
        return False

def number_check(s):
    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    for c in s[0:2]:
        if c in ("0123456789"):
            return False
        else:
            return True

def second_number_check(s):
    firstnum = None
    for c in s:
        if c.isdigit():
            firstnum = c
            break
    if firstnum == None:
        return True
    if int(firstnum) == 0:
        return False
    else:
        return True

def third_number_check(s):
    for c in s:
        if len(s) > 4:
            if s[2].isdigit():
                return False
            else:
                return True
        else:
            return True

def character_check(s):
    # “No periods, spaces, or punctuation marks are allowed.”
    if "." not in s and " " not in s and "?" not in s and "!" not in s:
        return True
    else:
        return False


main()


