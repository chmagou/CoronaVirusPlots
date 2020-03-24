import numpy as np
import matplotlib.pyplot as plt
import csv
import scraper
import datetime
import time
from matplotlib.dates import (DateFormatter, drange)

def saveData(cases, deaths):
    try: 
        cases_file = open("cases.txt", "a")
        cases_file.write(", "+ str(cases))
    except IOError as ioe1:
        print("Error: Case file not found: " + str(ioe1))
    try:
        deaths_file = open("deaths.txt", "a")
        deaths_file.write(", "+ str(deaths))
    except IOError as ioe2:
        print("Error: Case file not found: " + str(ioe2))

    cases_file.close()
    deaths_file.close()

def loadData(file):
    myList = []
    try:
        with open(file, 'r') as readfile:
            c = csv.reader(readfile, delimiter=',')
            for elements in c:
                for item in elements:
                    myList.append(int(item))
    except IOError as ioe:
        print("File not found: "+ str(ioe))
    return myList

def plotData():
    plt.title('Coronavirus Cases in Greece')
    number_of_cases = loadData("cases.txt")
    number_of_deaths = loadData("deaths.txt")
    formatter = DateFormatter('%d/%m/%y')
    startDate = datetime.date(2020, 2, 25)
    endDate = datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
    delta = datetime.timedelta(days=1)
    dates = drange(startDate, endDate, delta)
    fig, ax = plt.subplots()
    try:
        plt.plot(dates, number_of_cases)
        plt.plot(dates, number_of_deaths, color='red')
        ax.xaxis.set_major_formatter(formatter)
        plt.xlabel('Date')
        plt.ylabel('Cases')
        plt.show()
    except Exception as e:
        print("Error with the plot: " + str(e))
        print("Check plot again tomorrow!")

new_data = scraper.check_cases('greece')
new_cases_nr = new_data[0]
new_deaths_nr = new_data[1]
print('Total cases in Greece are: '+ str(new_cases_nr))
print('Total deaths in Greece are: '+ str(new_deaths_nr))
saveData(new_cases_nr, new_deaths_nr)
plotData()
time.sleep(86400) #check once a day