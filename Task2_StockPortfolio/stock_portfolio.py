# CodeAlpha Internship - Stock Portfolio Tracker

# Stock prices stored in a dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 180
}

print("====================================")
print("       STOCK PORTFOLIO TRACKER")
print("====================================")

total_investment = 0

# Ask how many different stocks the user wants to enter
number_of_stocks = int(input("How many stocks do you want to enter? "))

for i in range(number_of_stocks):

    stock = input("Enter stock symbol (AAPL/TSLA/GOOGL/MSFT/AMZN): ").upper()

    if stock in stock_prices:

        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        print("Stock:", stock)
        print("Price per share: $", price)
        print("Quantity:", quantity)
        print("Investment: $", investment)
        print()

    else:
        print("Stock not available in our list.")
        print()

print("====================================")
print("Total Investment: $", total_investment)
print("====================================")
