def main():
    camel = input("camelCase: ").strip()
    print(snake_case(camel))


def snake_case(camel):
    letters = [camel[0].lower()]
    for c in camel[1:]:
        if c in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            letters.append('_')
            letters.append(c.lower())
        else:
            letters.append(c)
    return ''.join(letters)

main()
