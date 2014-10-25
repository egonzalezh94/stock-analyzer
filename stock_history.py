import stock_day

class StockHistory(object):
    """A container for a list of historical stock day data.""" 
    
    def __init__(self, symbol, filename):
        self.symbol = symbol
        self.history = []
        
        f = open(filename, 'r')
        stock_lines = f.readlines()

        stock_lines = stock_lines[1:]

        for line in stock_lines:
            line = line.strip()
            values = line.split(',')
            day = stock_day.StockDay(values[0], float(values[1]), float(values[2]),
                                    float(values[3]), float(values[4]), float(values[5]),
                                    float(values[6]))
            self.history.append(day)

    def get_max_increase(self):
        """Find trading day with maximum increase between open and close"""
        max_diff = 0.0
        max_date = None

        for day in self.history:
            diff = day.get_day_increase()
            if diff > max_diff:
                max_diff = diff
                max_date = day
        print "%s: %s open = %.2f close = %.2f diff = %.2f" % (self.symbol, max_date.date,
                                                             max_date.open, max_date.close,
                                                             max_diff)


    def get_max_decrease(self):
        """Find trading day with maximum decrease between open and close"""
        max_diff = 0.0
        max_date = None

        for day in self.history:
            diff = day.get_day_decrease()
            if diff > max_diff:
                max_diff = diff
                max_date = day
        print "%s: %s open = %.2f close = %.2f diff = %.2f" % (self.symbol, max_date.date,
                                                             max_date.open, max_date.close,
                                                             max_diff)


    def get_max_percent_increase(self):
        """Find trading day with maximum increase between open and close"""
        max_diff = 0.0
        max_date = None  
        for day in self.history:
            diff = day.get_day_percent_increase()
            if diff > max_diff:
                max_diff = diff
                max_date = day
        print "%s: %s open = %.2f close = %.2f diff = %.2f" % (self.symbol, max_date.date,
                                                             max_date.open, max_date.close,
                                                             max_diff)


    def get_max_percent_decrease(self):
        """Find trading day with maximum percent decrease between open and close"""
        max_diff = 0.0
        max_date = None   
        for day in self.history:
            diff = day.get_day_percent_decrease()
            if diff > max_diff:
                max_diff = diff
                max_date = day
        print "%s: %s open = %.2f close = %.2f diff = %.2f" % (self.symbol, max_date.date,
                                                             max_date.open, max_date.close,
                                                             max_diff)


    def get_max_month(self):
        """Find trading month with maximum increase between open and close"""
        lastday = self.history[0]
        lastday_split = lastday.date.split('-')
        prevmonth = lastday_split[1]
        prevmonth_last_close = lastday.close #prevmonth_close
        prevday = lastday

        maxincrease = 0
        info = self.history[1:]        
        for day in info:
            y = day.date
            current_date = y.split('-')
            current_month = current_date[1]
            if current_month != prevmonth:
                prevmonth_first_close = prevday.close
                month_close = day.close
                temp = prevmonth_last_close - prevmonth_first_close
 
                if temp > maxincrease:
                    yes = prevmonth_last_close
                    maxincrease = temp
                    maxdate = prevday
                prevmonth_last_close = month_close
            prevday = day
            prevmonth = current_month
        print "%s: %s Last Day close = %.2f First Day Close = %.2f diff = %.2f" % (self.symbol, maxdate.date[:7],
                                                                             yes, maxdate.close,
                                                                             maxincrease)


    def get_max_year(self):
        lastday = self.history[0]
        lastday_split = lastday.date.split('-')
        prevyear = lastday_split[0]
        prevyear_last_close = lastday.close #prevyear_close
        prevday = lastday
        maxincrease = 0
        stuffs = self.history[0:]        
        for day in stuffs:
            y = day.date
            current_date = y.split('-')
            current_year = current_date[0]
            if current_year != prevyear:
                prevyear_first_close = prevday.close
                year_close = day.close
                temp = prevyear_last_close - prevyear_first_close
       
                if temp > maxincrease:
                    no = prevyear_last_close
                    maxincrease = temp
                    maxdate = prevday
                prevyear_last_close = year_close  
            prevday = day
            prevyear = current_year
        print "%s: %s Last Day Close = %.2f First Day Close = %.2f diff = %.2f" % (self.symbol, maxdate.date[:4],
                                                             no, maxdate.close,
                                                             maxincrease)


    def get_what_if(self, purchase_date, amount_invested):
        recent_stock = self.history[0]
        recent_closing_price = recent_stock.adj_close
        for day in self.history:
            if day.date == purchase_date:
                purchase_price = day.open
                shares = (amount_invested/purchase_price)
                outcome = shares * amount_invested
                earned = outcome - amount_invested
                print "%s: %f" % (self.symbol, earned)
                break
        else:
            print self.symbol, "Stock market was closed or company was not public at this time."

    def get_top_3(self):
        recent_day = self.history[0]
        open_price = recent_day.open
        close_price = recent_day.close
        increase = (close_price - open_price) * 100
        return "%.2f" %(increase)

