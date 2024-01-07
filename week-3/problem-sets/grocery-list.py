grocery_list = []
counts = {}

try:
    while True:
        grocery = input().upper()
        grocery_list.append(grocery)
        grocery_list.sort()

except EOFError:
    for g in grocery_list:
        counts[g] = counts.get(g, 0) + 1
    for g, count in counts.items():
        print(f"{count} {g}")
