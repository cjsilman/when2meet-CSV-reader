import polars as pl
import datetime
from datetime import datetime

df = pl.read_csv("G:/Desktop/All Python Projects/CSV Scheduler/availabilities.csv")

names = df.columns[1:]

def main():
    while True:
        print(
            "\nCSV Scheduler\n"
            f"{'-'*50}\n"
            "1. Check availability of a certain individual: i.e John Smith\n"
            "2. See when certain individuals are all available: i.e. John Smith, Sarah May\n"
            "q. To quit\n"
        )

        response = input("Please enter what you would like to do: ")

        if response == "1":
            name = input("Please input a name: ")
            grabAvailability(df, name)

        elif response == "2":
            nameList = []
            names = input("Please input names: ")
            names = names.split(",")
            for name in names:
                name = name.strip()
                nameList.append(name)
            seeEquivalentTimes(df, *nameList)

        elif response == "q" or response == "Q":
            break

        else:
            print("Invalid Input\n")

def grabAvailability(df, name):
    try:
        df = filterName(df, name)
    except:
        print(f"\n\n[ERR] Invalid name: {name}")
        return

    df = df[["Time", f"{name}"]]
    printTimes(df)

def seeEquivalentTimes(df, *names):
    
    for name in names:
        try:
            df = filterName(df, name)
        except:
            print(f"\n\n[ERR] Invalid name: {name}")
            return

    printTimes(df)

def filterName(dataframe, name):
    dataframe = dataframe.filter(
        (pl.col(name)==1)
    )
    return dataframe



def printTimes(df):
    previous = None
    for time in (df["Time"]):
        directtime = datetime.fromtimestamp(time)
    
        if previous != directtime.strftime('%A'):
            print(directtime.strftime('%A'))
            previous = directtime.strftime('%A')

        print(f"{' '*4}{str(directtime)[11:]}")




if __name__ == '__main__':
    main()