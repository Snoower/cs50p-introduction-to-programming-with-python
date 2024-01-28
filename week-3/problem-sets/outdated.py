def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ")
        if '/' in date or ',' in date:
            try:
                m, d, y = date.split("/")
                if (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int (d) <= 31):
                    y = y.strip()
                    break
            except:
                try:
                    m2, d2, y = date.split(" ")
                    for month in range(len(months)):
                        if m2 == months[month]:
                            m = month + 1
                    d = d2.replace(",", "")
                    if (int(m) > 0 or int(m) < 13) and (int(d) > 0 and int (d) <= 31):
                        y = y.strip()
                        break
                except:
                    pass
        else:
            print("Wrong format.")
    print(f"{y}-{int(m):02}-{int(d):02}")

main()
