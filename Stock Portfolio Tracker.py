import csv

def stock_tracker():
    # Hardcoded dictionary defining fixed stock prices
    STOCK_PRICES = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "AMZN": 175.50,
        "GOOGL": 150.25,
        "MSFT": 400.00
    }
   
    portfolio = {}
    print("--- CodeAlpha Stock Portfolio Tracker ---")
    print("Available stocks to track:", ", ".join(STOCK_PRICES.keys()))

    while True:
        ticker = input("\nEnter Stock Ticker (or type 'calculate' to view total): ").upper().strip()
       
        if ticker == 'CALCULATE':
            break
           
        if ticker not in STOCK_PRICES:
            print("❌ We don't have mock data for that stock. Please try again.")
            continue
           
        try:
            shares = int(input(f"Enter number of shares for {ticker}: "))
            if shares <= 0:
                print("❌ Quantity must be greater than zero.")
                continue
            portfolio[ticker] = portfolio.get(ticker, 0) + shares
        except ValueError:
            print("❌ Please enter a valid integer for the number of shares.")

    # Calculate and output results
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    print("\n--- Portfolio Summary ---")
    total_value = 0.0
   
    # Structure for file exporting
    report_data = []
   
    for ticker, shares in portfolio.items():
        price = STOCK_PRICES[ticker]
        asset_value = shares * price
        total_value += asset_value
        print(f"📈 {ticker}: {shares} shares @ ${price:.2f} = ${asset_value:.2f}")
        report_data.append([ticker, shares, price, asset_value])

    print(f"\n💰 Total Investment Value: ${total_value:.2f}")

    # Exporting data to CSV (Optional requirement fulfillment)
    with open("CodeAlpha_Portfolio_Report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Ticker", "Shares Held", "Current Price", "Total Value"])
        writer.writerows(report_data)
        writer.writerow([])
        writer.writerow(["Total Portfolio Value", "", "", f"${total_value:.2f}"])
       
    print("\n💾 Report successfully saved as 'CodeAlpha_Portfolio_Report.csv'!")

if __name__ == "__main__":
    stock_tracker()
