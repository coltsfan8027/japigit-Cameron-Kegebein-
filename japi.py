import json
import urllib.request
def getPrice(stockSymbol):
    f = open("japi.out", 'a')
    customURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+ stockSymbol +'&apikey=10SGW02MK9A60RT0'
    
    connection = urllib.request.urlopen(customURL)

    responseString = connection.read().decode()

    responseDict = json.loads(responseString)

    print(responseDict, file=f)
    print("The current price of ", responseDict['Global Quote']['05. price'], file=f)
    print(responseString, file=f)
    


def main():
    f = open("japi.out", 'a')

    stockSymbol = input("Enter the stock symbol in all caps: ")

    print(getPrice(stockSymbol), file=f)
    while(input("Run another or enter quit to terminate: ") != 'quit'):
        stockSymbol = input("Enter the stock symbol in all caps: ")

        print(getPrice(stockSymbol), file=f)
    print("Stock Quotes retrieved successfully!")
main()