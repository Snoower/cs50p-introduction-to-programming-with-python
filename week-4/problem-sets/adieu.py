import sys
import inflect

isOngoing = True
names_list = []

while isOngoing:
    try:
        p = inflect.engine()
        name = input("Name: ")
        names_list.append(name)
        name_list = p.join((names_list))
        print("Adieu, adieu, to " + name_list)
    except EOFError:
        isOngoing = False
        print("\nExiting")
        sys.exit
