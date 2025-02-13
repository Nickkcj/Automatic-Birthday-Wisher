import pandas
import datetime as dt

data = pandas.read_csv("birthdays.csv", header=0)

def check_birthday():
    now = dt.datetime.now()
    for i in range(len(data)):
        if data.loc[i].iloc[3] == now.month and data.loc[i].iloc[4] == now.day:
            return data.loc[i].iloc[0], data.loc[i].iloc[1]
        
    return False, False