import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    # df = pd.read_csv("data/AAPL.csv")
    # print (df['Adj Close'])
    # df['Adj Close'].plot()
    # v# must be called to show plots
    df = pd.read_csv("data/IBM.csv")
    print (df['High'])
    df[['High', 'Close']].plot()
    plt.show()

if __name__ == "__main__":
    test_run()
