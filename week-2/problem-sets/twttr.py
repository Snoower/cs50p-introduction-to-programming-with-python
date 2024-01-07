def main():
    text = input("Input: ").strip()
    print(strip_vowels(text))


def strip_vowels(text):
    letters = [text[0]]
    for c in text[1:]:
        if c in ("aeiouAEIOU"):
            letters.append("")
        else:
            letters.append(c)
    return ''.join(letters)

main()

