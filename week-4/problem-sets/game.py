import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1:
                rand_int = random.randint(1, level)
                while True:
                    try:
                        guess = int(input("Guess: "))
                        if guess < rand_int:
                            print("Too small!")
                        elif guess > rand_int:
                            print("Too large!")
                        else:
                            print("Just right!")
                            sys.exit()
                    except ValueError:
                        pass
        except ValueError:
            pass

main()
