def option_greeks(price, strike_price, expiration_time, interest_rate, volatility):
delta = (price - strike_price) / expiration_time
theta = (volatility * price) / (2 * math.sqrt(expiration_time))
gamma = (price * math.sqrt(expiration_time)) / (volatility * strike_price)
vega = (price * math.sqrt(expiration_time)) / 100
