"""
FINAL PROJECT SUBMISSION
STUDENT NAME: ONI LUCA
STUDENT CODE: 20200008
PART: B
CLASS: CS340 – INTRODUCTION TO ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING USING PYTHON
EXTRA WORK --- DATA SCRAPING From the website. ---
"""

# LIBRARIES USED IN THIS PART OF THE PROJECT

import pandas as pd
import csv
import tabulate
from datetime import datetime, timedelta
from operator import itemgetter
from statistics import mean
import matplotlib.pyplot as plt; plt.rcdefaults()
from pathlib import Path

# *****EXTRA WORK --- SCRAPING DATA FROM THE WEBSITE USING PANDAS AND CREATING AN INPUT FILE FROM SCRATCH*****

def datascraping():
    dt=pd.read_html('https://www.formula1.com/en/results.html/2018/races.html')[0]
    pd.set_option('display.max_columns', None)
    dt=dt.loc[:,'Grand Prix':'Time']
    dt['Grand Prix']=dt['Grand Prix'].str.replace(" ","_")
    dt['Winner']=dt['Winner'].str.replace("  ","_").str[:-4]
    dt['Car']=dt['Car'].str.upper().str.replace("RED BULL RACING TAG HEUER","RED_BULL")
    dt['Date']=dt['Date'].str.replace(" ","-")
    dt['Time']=pd.to_datetime(dt['Time'],format='%H:%M:%S.%f').dt.strftime('%H:%M:%S.%f')
    dt['Time']=dt['Time'].str[:-3]
    dt.columns= dt.columns.astype("str")
    dt.columns=dt.columns.str.upper().str.replace(" ","_")
    dt.to_csv('partA_input_data1.txt', encoding='utf-8', index=False)
    print(pd.read_csv('partA_input_data1.txt'))

#CREATING A LIST OF DICTIONARIES CONTAINING THE DATA FROM THE FILE

def listcreation():
    datafile = open("partA_input_data.txt", newline='')
    my_reader = csv.DictReader(datafile)
    global my_list
    my_list= []
    for row in my_reader:
        my_list.append(dict(row))
    datafile.close()
    for x in my_list:
        x["LAPS"] = int(x["LAPS"])
        x["DATE"] = datetime.strptime(x["DATE"],"%d-%b-%Y").date()
        x["TIME"] = datetime.strptime(x["TIME"], "%H:%M:%S.%f").time()

"""
    Menu option 1: Reads the 6 columns of data from file partA_input_data.txt and neatly
    displays it on screen.
"""

def op1():
    header = my_list[0].keys()
    rows = [x.values() for x in my_list]
    print(tabulate.tabulate(rows, header))

"""
    Menu option 2: Asks the user for a limit of laps to search by, then displays only the race
    results which involve that number of home laps or greater, sorted alphabetically by Grand Prix
    name. 
"""

def op2(limiter):
    res = [{k: v for (k, v) in i.items()}
           for i in my_list if i.get('LAPS') > limiter]
    header = res[0].keys()
    rows = [x.values() for x in res]
    print(tabulate.tabulate(rows, header))

"""
    Menu option 3: Calculates the average lap time per race then saves this new information as a
    7th column in file partA_output_data.txt. After saving into the file, it should also read
    back and display all 7 columns of data on the screen (the 6 original columns + the new one
    based on the calculations). 
"""

def op3():
    op3_list = my_list
    for x in op3_list:
        time = datetime.strptime(x["TIME"].strftime("%H:%M:%S.%f"), "%H:%M:%S.%f")
        dividable_time = timedelta(hours=time.hour, minutes=time.minute, seconds=time.second, microseconds=time.microsecond)
        avg_tpl = dividable_time / int(x["LAPS"])
        x['AVG TIME PER LAP'] = avg_tpl

    myFile = open('partA_output_data.txt', 'w')
    writer = csv.DictWriter(myFile, fieldnames=op3_list[0].keys())
    writer.writeheader()
    writer.writerows(op3_list)
    myFile.close()

    datafile = open("partA_output_data.txt", newline='')
    my_reader = csv.DictReader(datafile)
    new_list = []
    for row in my_reader:
        new_list.append(dict(row))
    datafile.close()
    header = new_list[0].keys()
    rows = [x.values() for x in new_list]
    print(tabulate.tabulate(rows, header))

"""
    Menu option 4: Asks the user for a field to sort by, then whether the order should be
    ascending or descending. Displays on screen all data contained in the file sorted according to
    the user's instructions. This option refers to the 7-column file generated in option 3 and
    assumes it exists, otherwise the program should inform the user to execute option 3 first and
    then get back to option 4.
"""

def op4(index,order):
    def display():
        header = templist[0].keys()
        rows = [x.values() for x in templist]
        print(tabulate.tabulate(rows, header))
    datafile = open("partA_output_data.txt", newline='')
    my_reader = csv.DictReader(datafile)
    global op4_list
    op4_list = []
    for row in my_reader:
        op4_list.append(dict(row))
    datafile.close()
    # Displaying records depending on the column and order *(ascending or descending)
    if index == 1:
        if order == 0:
            templist = sorted(op4_list, key=itemgetter("GRAND_PRIX"))
            display()
        elif order == 1:
            templist = sorted(op4_list, key=itemgetter("GRAND_PRIX"), reverse=True)
            display()
        else:
            print("Invalid entry! Try again.")
    elif index ==2:
        if order == 0:
            templist = sorted(op4_list, key=itemgetter("DATE"))
            display()
        elif order ==1:
            templist = sorted(op4_list, key=itemgetter("DATE"), reverse=True)
            display()
        else:
            print("Invalid entry! Try again.")
    elif index == 3:
        if order == 0:
            templist = sorted(op4_list, key=itemgetter("WINNER"))
            display()
        elif order ==1:
            templist = sorted(op4_list, key=itemgetter("WINNER"), reverse=True)
            display()
        else:
            print("Invalid entry! Try again.")
    elif index == 4:
        if order ==0:
            templist = sorted(op4_list, key=itemgetter("CAR"))
            display()
        elif order == 1:
            templist = sorted(op4_list, key=itemgetter("CAR"), reverse=True)
            display()
        else:
            print("Invalid entry! Try again.")
    elif index == 5:
        if order == 0:
            templist = sorted(op4_list, key=itemgetter("LAPS"))
            display()
        elif order==1:
            templist = sorted(op4_list, key=itemgetter("LAPS"), reverse=True)
            display()
        else:
            print("Invalid entry! Try again.")
    elif index == 6:
        if order ==0:
            templist = sorted(op4_list, key=itemgetter("TIME"))
            display()
        elif order == 1:
            templist = sorted(op4_list, key=itemgetter("TIME"), reverse=True)
            display()
        else:
            print("Invalid entry! Try again.")
    elif index == 7:
        if order == 0:
            templist = sorted(op4_list, key=itemgetter("AVG TIME PER LAP"))
            display()
        elif order == 1:
            templist = sorted(op4_list, key=itemgetter("AVG TIME PER LAP"), reverse=True)
            display()
        else:
            print("Invalid entry! Try again.")
    else:
        print("TERMINATION!")

"""
    Menu option 5: Calculates the total average lap time per driver -across all Grand Prix races
    and presents it as a GUI column graph in a pop-up window (x-axis: driver names. y-axis:
    average lap time in minutes).
"""

def op5():
    op5_list=my_list
    for x in op5_list:
        time = datetime.strptime(x["TIME"].strftime("%H:%M:%S.%f"), "%H:%M:%S.%f")
        dividable_time = timedelta(hours=time.hour, minutes=time.minute, seconds=time.second, microseconds=time.microsecond)
        avg_tpl = dividable_time / int(x["LAPS"])
        x["TOTALAVGTIME"] = int(avg_tpl.total_seconds()) / 60

    graph_list = {
        winner: mean(x['TOTALAVGTIME'] for x in op5_list if x['WINNER'] == winner)
        for winner in set(x['WINNER'] for x in op5_list)
    }

    keys = graph_list.keys()
    values = graph_list.values()
    plt.bar(keys, values, align='center', alpha=0.5)
    plt.xticks(rotation=30)
    plt.rcParams.update({'font.size': 12})
    plt.xlabel('Grand Prix Winners')
    plt.ylabel('Average time per lap')
    plt.title('OP5 Graph of the average lap time per driver')
    plt.tight_layout()
    plt.show()

listcreation()

#PROGRAM MENU
def progmenu():
    while True :
        # ERROR HANDLING ON USER INPUT
        try:
            print("\n")
            print(" Fall 2023 CS 340 PROJECT ")
            print(" Option 1: Display Data of the 2018 Formula 1 racing season.")
            print(" Option 2: Display Data based on the number of home laps.")
            print(" Option 3: Display Data including the average lap time per race. *(New CVS file will be created.)")
            print(" Option 4: Display Data sorted by a specified field. *(Option 3 required.)")
            print(" Option 5: Display the total average lap time per driver. *(Displays Data in a graph format.)")
            print(" Option 6: EXIT.\n")
            choice = int(input("\nEnter the option you want to see: *(Integers only!)\n"))

        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")

        else:
            if choice == 1: #OPTION 1
                print("You have chosen option 1. \n")
                print("Here is the data provided by the Formula 1 Website for the 2018 racing season. \n \n")
                op1()
                print("\n")
            elif choice == 2:  #OPTION 2
                print("You have chosen option number 2. \n")
                while True:
                    try:
                        limiter = int(input(" Please enter a number of laps you want to limit the data display:\n"))
                        break
                    except ValueError:
                        print("Oops!  That was not a valid number.  Try again...\n")
                print("\n")
                op2(limiter)

            elif choice == 3:  #OPTION 3
                print("You have chosen option 3. \n")
                print("Here is the data including the average time per lap calculated. \n \n")
                op3()
            elif choice == 4:  # OPTION 4 * WORKS ONLY IF OPTION 3 WAS RAN BEFORE, BY CHECKING IF THE FILE CREATED IN OPTION 3 EXISTS
                path_to_file = 'partA_output_data.txt'
                path = Path(path_to_file)
                if path.is_file():

                    print("You have chosen option 4. \n")
                    print("Here is a legend depicting the columns of the table and the index: \n")
                    print(" 1. GRAND_PRIX, \n 2. DATE, "
                          "\n 3. WINNER,\n 4. CAR, \n 5. LAPS, \n 6. TIME, \n 7. AVG TIME PER LAPS, \n 8. PRESS TO EXIT OPTION 4 \n")

                    while True:
                        try:
                            index = int(
                                input(" Please enter the index of the column you want to sort the data for: \n"))
                            if index == 8:
                                print("Terminating option 4.")
                                break
                            else:
                                while True:
                                    try:
                                        order = int(input(" Press 0 for ascending or 1 for descending: \n"))
                                        op4(index, order)
                                        break
                                    except ValueError:
                                        print("Oops!  That was not a valid number.  Try again...\n")
                            break
                        except ValueError:
                            print("Oops!  That was not a valid number.  Try again...\n")

                else:
                    print("\nPlease execute option 3 for option 4 to work!")
            elif choice == 5:  # OPTION 5
                print("You have chosen option 5. \n")
                print("Loading... \n \n")
                op5()
            elif choice == 6:  # OPTION 6 --- EXIT
                print(" Thank you for checking my submission! Exiting the program. ")
                break
            elif choice == 7:  # HIDDEN OPTION --- EXTRA WORK
                print("This is a hidden menu option where i give data scraping a try.")
                datascraping()
            else:  #ERROR HANDLING In case the input is an integer, but not a valid menu option
                print("Invalid Command")

progmenu()  # STARTING THE PROGRAM

