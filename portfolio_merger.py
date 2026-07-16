class Portfolio:
    def __init__(self, cash, stock_value):
        self.cash = cash
        self.stock_value = stock_value

    def __add__(self, other):
        if not isinstance(other, Portfolio):
            raise TypeError("Can only add another Portfolio instance.")
        return Portfolio(self.cash + other.cash, self.stock_value + other.stock_value)

    def __repr__(self):
        return f"Portfolio(cash={self.cash}, stock_value={self.stock_value})"


if __name__ == "__main__":
    p1 = Portfolio(5000, 12000)
    p2 = Portfolio(3000, 4000)
    merged = p1 + p2
    print(merged)

    try:
        p1 + 100
    except TypeError as e:
        print(e)
