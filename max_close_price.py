import pandas as pd

def get_max_close(symbol):
    """
    Return the maximum closing value for stocj indicated by symbol
    Note: Data for a stocj is stored in fileL data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol)) # read in Data
    return (df['Close'].max()) #compute and return max
    # return(df['Close'])

def test_run():
    """
    Function called by Test Run.
    """
    for symbol in ['AAPL', 'IBM']:
        print("Max close")
        print(symbol, get_max_close(symbol))

if __name__ == "__main__":
    test_run()
