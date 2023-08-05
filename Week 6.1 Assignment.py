def stock_prices():
    stocks = {
        "ESPN": 34.75,
        "AAPL": 77.49,
        "NBC": 23.98,
        "AMC": 89.48,
        "NFLX": 82.33,
        "MSGS": 47.32,
        "MUFC": 58.43,
        "FB": 92.55,
        "NKE": 47.39,
        "LSE": 36.32,
    }
    print("Stock Price Finder.")
    ticker_symbol = input("Please enter the ticker symbol here: ")
    
    stock_price = stocks.get(ticker_symbol)
    if stock_price is not None:
        print("Ticker Symbol:", ticker_symbol)
        print("Stock Price:", stock_price)
    else: 
        print("Sorry! We are working on adding that company and its price plus more. Please enter another one: ")
      

stock_prices()


