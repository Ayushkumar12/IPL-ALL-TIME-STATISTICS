import pandas as pd
import matplotlib.pyplot as plt

ipl = pd.read_csv('ipl.csv',encoding='latin1', index_col=0)

ch = 'y'
while ch == 'y' or ch == 'Y':
    print("Main Menu")
    print("1. Fetch Data")
    print("2. Dataframe Statistics")
    print("3. Display Records")
    print("4. Search specific row/column")
    print("5. Data Visualization")
    print("6. Data analytics")
    print("7. Exit")
    ch1 = int(input("Enter your choice"))
    if ch1 == 1:
        print("DISPLAYING ALL TIME IPL STATISTICS DATA")
        print("=============================")
        print(ipl)
    elif ch1 == 2:
        while (True):
            print("Dataframe Statistics Menu")
            print("1. Display all column names")
            print("2. Display the indexes")
            print("3. Display the shape")
            print("4. Display the dimension")
            print("5. Display the data types of all columns")
            print("6. Display the size")
            print("7. Exit")
            ch2 = int(input("Enter choice"))
            if ch2 == 1:
                print(ipl.columns)
            elif ch2 == 2:
                print(ipl.index)
            elif ch2 == 3:
                print(ipl.shape)
            elif ch2 == 4:
                print(ipl.ndim)
            elif ch2 == 5:
                print(ipl.dtypes)
            elif ch2 == 6:
                print(ipl.size)
            elif ch2 == 7:
                break
    elif ch1 == 3:
        while (True):
            print("Display Records Menu")
            print("1. Top 5 Resords")
            print("2. Bottom 5 Records")
            print("3. Specific number of records from the top")
            print("4. Specific number of records from the bottom")
            print("5. Details of a specific Player")
            print("6. Display details of all Players")
            print("7. Exit")
            ch3 = int(input("Enter choice"))
            if ch3 == 1:
                print(ipl.head())
            elif ch3 == 2:
                print(ipl.tail())
            elif ch3 == 3:
                n = int(input("Enter how many records you want to display from the top"))
                print(ipl.head(n))
            elif ch3 == 4:
                n = int(input("Enter how many records you want to display from the bottom"))
                print(ipl.tail(n))
            elif ch3 == 5:
                plyr = input("Enter the player name for which you want to see the details")
                print(ipl.loc[plyr])
            elif ch3 == 6:
                print("Overall Statistics of players of the IPL")
                print(ipl)
            elif ch3 == 7:
                break
    elif ch1 == 4:
        while (True):
            print("Search Menu")
            print("1. Search for the details of a specific player")
            print("2. Search details of a specific as per a specific column heading")
            print("3. Exit")
            ch4 = int(input("Enter choice"))
            if ch4 == 1:
                plyr = input("Enter the name of the player whose details you want to see")
                print(ipl.loc[plyr])
            elif ch4 == 2:
                col = input("Enter column/heading name whose details you want to see")
                print(ipl[col])
            elif ch4 == 3:
                break
    elif ch1 == 5:
        while (True):
            print("Data Visualization Menu")
            print("1. Line Plot--> No. of matches played by each player")
            print("2. Histogram-->No. of runs scored by players")
            print("3. Horizontal Bar Plot-->strike rate of each player")
            print("4. Vertical bar plot-->No. of 4s and 6s of each player")
            print("5. Exit")
            ch5 = int(input("Enter choice"))
            if ch5 == 1:
                plt.plot(ipl.index, ipl['matches'])
                plt.title("No. of matches played by each player")
                plt.xlabel("PLAYERS")
                plt.ylabel("NO. OF MATCHES")
                plt.xticks(rotation=90)
                plt.show()
            elif ch5 == 2:
                plt.hist(ipl['runs'], bins=5, edgecolor="black", color='red')
                plt.title("No. of runs scored by players")
                plt.xlabel("RUNS")
                plt.ylabel("FREQUENCY")
                plt.show()
            elif ch5 == 3:
                plt.barh(ipl.index, ipl['strike rate'], color=['b', 'c', 'g', 'k', 'm', 'r', 'b', 'y'])
                plt.title("STRIKE RATE OF EACH PLAYER")
                plt.xlabel("PLAYERS")
                plt.ylabel("STRIKE RATES")
                plt.show()
            elif ch5 == 4:
                plt.bar(ipl.index, ipl['4s'], label="No. of 4s")
                plt.bar(ipl.index, ipl['6s'], label="No. of 6s")
                plt.title("No. of 4s and 6s of each player")
                plt.xticks(ipl.index)
                plt.xlabel("PLAYERS")
                plt.ylabel("NO. OF 4s AND 6s")
                plt.legend()
                plt.xticks(rotation=90)
                plt.show()
            elif ch5 == 5:
                break
    elif ch1 == 6:
        while (True):
            print("Data Analytics Menu")
            print("1. Player with maximum number of matches played")
            print("2. Player with minimum number of matches played")
            print("3. Player with maximum number of inns")
            print("4. Player with minimum number of inns")
            print("5. Player with maximum number of centuries")
            print("6. Player with maximum number of half-centuries")
            print("7. Exit")
            ch6 = int(input("Enter choice:"))
            if ch6 == 1:
                m = ipl['matches'].max()
                s = ipl.loc[ipl.matches == m]
                print("Player with maximum number of matches played-", m, " is\n ", s.index)
            elif ch6 == 2:
                m = ipl['matches'].min()
                s = ipl.loc[ipl.matches == m]
                print("Player with minimum number of matches played- ", m, " is\n ", s.index)
            elif ch6 == 3:
                m = ipl['inns'].max()
                s = ipl.loc[ipl.inns == m]
                print("Player with maximum number of inns-", m, " is\n ", s.index)
            elif ch6 == 4:
                m = ipl['inns'].min()
                s = ipl.loc[ipl.inns == m]
                print("Player with minimum number of inns-", m, " is\n ", s.index)
            elif ch6 == 5:
                m = ipl['n100'].max()
                s = ipl.loc[ipl.n100 == m]
                print("Player with maximum number of centuries-", m, " is\n ", s.index)
            elif ch6 == 6:
                m = ipl['n50'].max()
                s = ipl.loc[ipl.n50 == m]
                print("Player with maximum number of half-centuries-", m, " is\n ", s.index)
            elif ch6 == 7:
                break
    elif ch1 == 7:
        break
    ch = input("Do you want to continue?(y/n)")
