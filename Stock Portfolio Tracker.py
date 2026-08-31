stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 415,
    "NVDA": 875,
    "META": 510,
    "NFLX": 635
}
total = 0
with open("final.txt", "w") as file:
    pass
while input("Do you want to add a new one? (Y/N): ").upper() == "Y":
    stock = input("Enter stock name: ").upper()
    if stock not in stock_prices:
        print("This stock is not available.")
        continue
    shares = int(input("How many shares do you want: "))
    total_value = stock_prices[stock] * shares
    total += total_value
    with open("final.txt", "a") as file:
        file.write(f"Stock: {stock}, Shares: {shares}, Total: ${total_value}\n")
with open("final.txt", "r") as file:
    print(f"\nThank you for using our service!\nThis is your portfolio:\n{file.read()}Total Investment: ${total}")
