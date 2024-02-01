from pyfiglet import Figlet
import sys
import random

with open("figlet_fonts.txt", 'r') as figlet_font:
    contents = figlet_font.read().splitlines()

def main():
    if len(sys.argv) == 1:
        zero = input("Input: ")
        z = Figlet(font=random.choice(contents))
        print(z.renderText(zero))
    elif len(sys.argv) == 3 and ("-f" in sys.argv or "-font" in sys.argv) and sys.argv[2] in contents:
        two = input("Input: ")
        t = Figlet(font=sys.argv[2])
        print(t.renderText(two))
    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()
