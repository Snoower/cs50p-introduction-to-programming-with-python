import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if input := re.search(r'.+src="https?://?(www\.)?youtube\.com/embed/([\w\d]+)"', s):
        return "https://youtu.be/" + input.group(2)


if __name__ == "__main__":
    main()
