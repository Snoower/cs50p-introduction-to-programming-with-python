import random


def main():
    level = get_level()
    correct_answers = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x+y
        tries = 0

        while tries < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    correct_answers += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                tries += 1
                pass

        if tries == 3:
            print(correct_answer)

    print(f"Score: {correct_answers}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in {1,2,3}:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()


