import os
import os.path
import sys
import urllib2

import stock_history

STOCKS_DIR = 'stocks'


class StockCollection(object):
    """A container for a collection of stock histories.  Stock data can be
       downloaded from Yahoo Finance.  The collection can be loaded from disk
       and then used for analysis.
    """
    
    def __init__(self):
        self.stocks = {}

    def download_stock(self, symbol):
        """Download historical data for stock symbol."""

        # Create stocks directory if necessary
        if not os.path.exists(STOCKS_DIR):
            os.mkdir(STOCKS_DIR)

        # Download the historical stock data
        url = 'http://real-chart.finance.yahoo.com/table.csv?s=' + symbol + '&c=1800'
        response = urllib2.urlopen(url)
        html = response.read()

        filename = STOCKS_DIR + '/' + symbol.upper() + '.csv'
        f = open(filename, 'w')
        f.write(html)
        f.close()

    def download(self, symbols):
        """Download historical data for each stock in the symbols list."""
        
        for symbol in symbols:
            print 'Downloading %s.' % (symbol)
            self.download_stock(symbol)

    def load_stock(self, filename):
        """Load a stock file from csv file into stock collection."""
        
        symbol = filename.split('.')[0]
        stock_path = STOCKS_DIR + '/' + filename
        history = stock_history.StockHistory(symbol, stock_path)
        self.stocks[symbol] = history        

    def load(self):
        """Load stocks from stocks directory."""
        if os.path.exists(STOCKS_DIR):
            stock_files = os.listdir(STOCKS_DIR)
            for stock_file in stock_files:
                self.load_stock(stock_file)

    def list(self):
        """Return the stocks found in the stocks directory."""
        
        return self.stocks.keys()

    def refresh(self):
        """Re-download the historical data from all stocks in the stocks dir."""

        self.download(self.list())
 
    def max_day_increase(self, symbols):
        for symbol in symbols:
            symbol = symbol.upper()
            if symbol not in self.stocks:
                print "%s is not in list" % (symbol)
            else:
                history = self.stocks[symbol]
                history.get_max_increase()

    def max_day_decrease(self, symbols):
        for symbol in symbols:
            symbol = symbol.upper()
            if symbol not in self.stocks:
                print "%s is not in list" % (symbol)
            else:
                history = self.stocks[symbol]
                history.get_max_decrease()

    def max_day_percent_increase(self, symbols):
        for symbol in symbols:
            symbol = symbol.upper()
            if symbol not in self.stocks:
                print "%s is not in list" % (symbol)
            else:
                history = self.stocks[symbol]
                history.get_max_percent_increase()

    def max_day_percent_decrease(self, symbols):
        for symbol in symbols:
            symbol = symbol.upper()
            if symbol not in self.stocks:
                print "%s is not in list" % (symbol)
            else:
                history = self.stocks[symbol]
                history.get_max_percent_decrease()

    def max_day_volume(self, symbols):
        for symbol in symbols:
            symbol = symbol.upper()
            if symbol not in self.stocks:
                print "%s is not in list" % (symbol)
            else:
                history = self.stocks[symbol]
                history.get_max_volume()

    def max_month_increase(self, symbols):
        for symbol in symbols:
            symbol = symbol.upper()
            if symbol not in self.stocks:
                print "%s is not in list" % (symbol)
            else:
                history = self.stocks[symbol]
                history.get_max_month()

    def max_year_increase(self, symbols):
        for symbol in symbols:
            symbol = symbol.upper()
            if symbol not in self.stocks:
                print "%s is not in list" % (symbol)
            else:
                history = self.stocks[symbol]
                history.get_max_year()

    def what_if(self, purchase_date, amount_invested, symbols):

        for symbol in symbols:
            symbol = symbol.upper()
            if symbol not in self.stocks:
                print "%s is not in list" % (symbol)
            else:
                history = self.stocks[symbol]
                self.purchase_date = purchase_date
                self.amount_invested = amount_invested
                history.get_what_if()

    def top_3(self):
        max_diff = 0
        max_diff2 = 0
        max_diff3 = 0
        max_symb = None
        max_symb2 = None
        max_symb3 = None
        diff_list=[]
        for symb in self.list():
            history = self.stocks[symb]
            #history.get_top_3()
            diff = history.get_top_3()
            if diff > max_diff:
                max_diff = diff
                max_symb = symb
            elif max_diff > max_diff2:
                tmp = max_diff2
                tmp_symb = max_symb2
                max_diff2 = max_diff
                max_symb2 = max_symb
                max_diff = tmp
                max_symb = tmp_symb

        
            elif max_diff2 > max_diff3:

                tmp = max_diff3
                tmp_symb = max_symb3
                max_diff3 = max_diff
                max_symb3 = max_symb
                max_diff = tmp
                max_symb = tmp_symb

        print max_diff, max_symb, max_diff2, max_symb2, max_diff3, max_symb3
        

        
