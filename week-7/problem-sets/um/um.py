import re


def main():
    print(count(input("Text: ")))


def count(s):
     count = 0
     sentence = s.split()
     for w in sentence:
        if re.search(r"\b[uU]m\b", w):
            count += 1
     return count


if __name__ == "__main__":
    main()
