def main():
        is_due = True
        coke = 50
        while is_due:
            print(f"Amount Due: {coke}")
            coin  = int(input("Insert Coin: "))
            if coin == 5 or coin == 10 or coin == 25:
                coke -= coin
                if coke == 0:
                    is_due = False
                    print("Change Owed: 0")
                elif coke < 0:
                    coke = coke * -1
                    print(f"Change Owed: {coke}")
                    break
            else:
                print("Sorry, this machine only accepts coins in denominations: 25 cents, 10 cents, and 5 cents")
main()
