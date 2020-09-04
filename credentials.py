from Robinhood import Robinhood
my_trader = Robinhood()
logged_in = my_trader.login(username="USERNAME HERE", password="PASSWORD HERE")
stock_instrument = my_trader.instruments("GEVO")[0]
quote_info = my_trader.quote_data("GEVO")
buy_order = my_trader.place_market_buy_order(stock_instrument["url"], "GEVO", "GFD", 1)
sell_order = my_trader.place_market_sell_order(stock_instrument["url"], "GEVO", "GFD", 1)