def profit(stock_prices):

    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices!')

    min_stock_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for price in stock_prices[1:]:
        comparison_profit = price - min_stock_price
        max_profit = max(max_profit, comparison_profit)
        min_stock_price = min(min_stock_price, price)

    return max_profit

print profit([10, 20, 30, 40, 100])

