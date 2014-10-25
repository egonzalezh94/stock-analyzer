class StockDay(object):
    
    def __init__(self, date, open, high, low, close, volume, adj_close):
        self.date = date        
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.adj_close = adj_close

    def get_day_increase(self):
        return (self.close - self.open)

    def get_day_decrease(self):
        return (self.open - self.close)

    def get_day_percent_increase(self):
        return ((self.close - self.open)/self.open) * 100

    def get_day_percent_decrease(self):
        return ((self.open - self.close)/self.close) * 100

    def get_date(self):
        return self.date

