import pandas as pd

def test_run():
    df = pd.read_csv("AAPL.csv")
    # print(df) print all the in the csv file
    # print(df.head()) print the first five rows
    # print(df.tail()) print the last five rows
    print(df[10:21]) # data splicing

if __name__ == "__main__":
    test_run()
