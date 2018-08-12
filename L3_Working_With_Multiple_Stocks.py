'''
Build a dataframe in pandas
'''
import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from csv files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols: #add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp =  pd.read_csv(symbol_to_path(symbol), index_col="Date",
                            parse_dates=True, usecols=['Date', 'Adj Close'],
                            na_values=['nan'])
        # rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        # df = df.join(df_temp,how='inner')
        df = df.join(df_temp, how='inner')
        #if symbol == 'SPY':
        #    df = df.dropna(subset=["SPY"])
    return df

def normalize_data(df):
    '''Normalize stock prices using the first row of the dataframe.'''
    df = df/df.ix[0,:]
    return df

def plot_data(df, title="Stock prices"):
    '''Plot stock prices'''
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def test_run():
    # Create the date range
    start_date = '2018-07-11'
    end_date = '2018-08-10'
    dates=pd.date_range(start_date,end_date)

    # Choose stock symbols to read
    symbols = ['SPY','AAPL','GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)

    # Slice by row range (dates) using DataFrame.ix[] selector
    # print (df.ix['2018-07-01':'2018-07-31']) # the month of August

    # Slice by column (symbols)
    # print(df['GOOG'])
    # print(df[['GOOG','GLD']])

    # Slicing by row and column
    df_slice = df.ix['2018-07-01':'2018-07-31',['SPY', 'AAPL','IBM','GOOG','GLD']]

    df_slice = normalize_data(df_slice)

    print(df_slice)

    plot_data(df_slice)





if __name__ == '__main__':
    test_run()
