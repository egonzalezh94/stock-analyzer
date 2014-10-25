import sys

import stock_collection
        
if __name__ == '__main__':

    if (len(sys.argv) < 2):
        print "No command was given, type 'help' for available options."
    else:
        command = sys.argv[1].lower()

        collection = stock_collection.StockCollection()
        collection.load()

        if command == 'list':
            symbols = collection.list()
            if (len(symbols) == 0):
                symbols = "No stocks are currently saved."
            print symbols
        
        elif command == 'download':
            if (len(sys.argv) < 3):
                print "Please specify the stocks that are to be downloaded."
            else:
                collection.download(sys.argv[2:])    
                print 'Download complete.'

        elif command == 'refresh':
            collection.refresh()
            print 'Refresh complete.'

        elif command == 'max_day_increase':
            if (len(sys.argv) < 3):
                print "Please specify the stocks that are to be compared."
            else:
                collection.max_day_increase(sys.argv[2:])

        elif command == 'max_day_decrease':
            if (len(sys.argv) < 3):
                print "Please specify the stocks that are to be compared."
            else:
                collection.max_day_decrease(sys.argv[2:])

        elif command == 'max_day_percent_increase':
            if (len(sys.argv) < 3):
                print "Please specify the stocks that are to be compared."
            else:
                collection.max_day_percent_increase(sys.argv[2:])

        elif command == 'max_day_percent_decrease':
            if (len(sys.argv) < 3):
                print "Please specify the stocks that are to be compared."
            else:
                collection.max_day_percent_decrease(sys.argv[2:])

        elif command == 'max_month_increase':
            if (len(sys.argv) < 3):
                print "Please specify the stocks that are to be compared."
            else:
                collection.max_month_increase(sys.argv[2:])

        elif command == 'max_year_increase':
            if (len(sys.argv) < 3):
                print "Please specify the stocks that are to be compared."
            else:
                collection.max_year_increase(sys.argv[2:])

        elif command == 'what_if':
            #purchase_date = sys.argv[2]
            #amount_invested = sys.argv[3]
            collection.what_if(sys.argv[2],sys.argv[3], sys.argv[4:])

        elif command == 'top_3':
            collection.top_3()

        elif command == 'help':
            print """Available options are:
            list
            download
            refresh
            max_day_increase
            max_day_increase
            max_day_percent_increase
            max_day_percent_decrease
            max_month_increase
            max_year_increase
            what_if
            help"""

        else:
            print 'Command not recognized: %s' % (command)














