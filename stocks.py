import sys


import stock_collection
        

if __name__ == '__main__':
    
    command = sys.argv[1]

    collection = stock_collection.StockCollection()
    collection.load()

    if command == 'list':
        symbols = collection.list()
        print symbols
    
    elif command == 'download':
        collection.download(sys.argv[2:])    
        print 'Download complete.'

    elif command == 'refresh':
        collection.refresh()
        print 'Refresh complete.'

    elif command == 'max_day_increase':
        collection.max_day_increase(sys.argv[2:])

    elif command == 'max_day_decrease':
        collection.max_day_decrease(sys.argv[2:])

    elif command == 'max_day_percent_increase':
        collection.max_day_percent_increase(sys.argv[2:])

    elif command == 'max_day_percent_decrease':
        collection.max_day_percent_decrease(sys.argv[2:])

    elif command == 'max_month_increase':
        collection.max_month_increase(sys.argv[2:])

    elif command == 'max_year_increase':
        collection.max_year_increase(sys.argv[2:])

    elif command == 'what_if':
        #purchase_date = sys.argv[2]
        #amount_invested = sys.argv[3]
        collection.what_if(sys.argv[2],sys.argv[3], sys.argv[4:])

    elif command == 'top_3':
        collection.top_3()

    elif command == 'help':
        print "Not supported yet"

    else:
        print 'Command not recognized: %s' % (command)














