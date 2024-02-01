import sys
import requests

def main():
    if len(sys.argv) <= 1:
        sys.exit("Missing command-line argument")
    else:
        argument = sys.argv[1]
        try:
            float_value = float(argument)
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            r = response.json()
            usd_rate_float = r["bpi"]["USD"]["rate_float"]
            bitcoin_price_in_usd = usd_rate_float * float_value
            print(f"${bitcoin_price_in_usd:,.4f}")
        except:
            sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()
