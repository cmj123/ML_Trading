import pandas as pd

def get_mean_volume(symbol):
    """
    Return the maximum closing value for stocj indicated by symbol
    Note: Data for a stocj is stored in fileL data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol)) # read in Data
    return (df['Volume'].mean()) #compute and return max
    # return(df['Close'])

def test_run():
    """
    Function called by Test Run.
    """
    for symbol in ['AAPL', 'IBM']:
        print("Mean volume")
        print(symbol, get_mean_volume(symbol))

if __name__ == "__main__":
    test_run()
