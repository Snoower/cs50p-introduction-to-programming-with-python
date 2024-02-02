def main():
    text = str(input("Input: ").strip())
    print(shorten(text))

def shorten(word):
    letters = [word[0]]
    for c in word[1:]:
        if c in ("aeiouAEIOU"):
            letters.append("")
        else:
            letters.append(c)
    return ''.join(letters)

if __name__ == "__main__":
    main()

