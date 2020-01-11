import sys
import math
import numpy as np
import pandas as pd
import random
from colorclass import Color, Windows
from terminaltables import SingleTable


datamining = ["Student visibly uncomfortable", 
                 "Calls out someone for using buzzwords",
                 "Casually over-runs class",
                 "Thats not interesting",
                 "Jab at B school",
                 "Flies through slides like Shree",
                 "Ignores irrelevant question",
                 "Laptop battery warning",
                 "Displays breadth of knowledge"]

nonlinear = ["Is everyone finished? (No response)",
                "Blue checkered shirt + blazer",
                "Dataset where columns are flipped",
                "Yuri tells joke but doesnt smile",
                "Still teaching at 4:31",
                ">5s pause where no one answers Yuris question",
                "Financial example",
                "Entire hour of confusion",
                "Does not complete workshop",
                "Any questions? (nervous silence)",
                "Same person answers 4+ questions",
                "Leaves material for TA",
                "The answer to the question is on the slide"]

winterclasses = {1: datamining, 2: nonlinear}

def bingo():
    print("\n**********************************")
    print("****** 25 cents Class Bingo ******")
    print("********************************** \n")

    course = int(input("For which course would you like to play Bingo? Enter 1 for Data Mining, 2 for Non-linear:  "))
    if course in winterclasses: 
        dim = math.floor(math.sqrt(len(winterclasses[course])))
        df = pd.DataFrame(data = np.random.choice(winterclasses[course], dim**2, replace=False))
        df.rename(columns={0: "element"}, inplace = True)
        df["id"] = range(1,dim**2+1)
        df["element"] = df["id"].map(str) + ". " +  df["element"].map(str)
        df["hit"] = 0
        df['output'] = "Color('{}" + df["element"].astype(str) + """{}'.format("{autoyellow}", "{/autoyellow}"))"""
        array = df["output"].tolist()
        array = [eval(x) for x in array]
        grid = [array[i:i+dim] for i in range(0, len(array), dim)]
        table_instance = SingleTable(grid)
        table_instance.inner_heading_row_border = False
        table_instance.inner_row_border = True
        table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
        print(table_instance.table) 
        
        while True:
            action = input("Enter item number which you hit. Enter RESTART for a new board. Enter QUIT to leave the application:  ")
            
            if action.isdigit() and int(action) in df['id'].values:
                df.loc[df.id == int(action), "hit"] = df.loc[df.id == int(action), "hit"].replace({0:1, 1:0})
                df['output'] = "Color('{}" + df["element"].astype(str) + """{}'.format("{autoyellow}", "{/autoyellow}"))"""
                df.loc[df.hit == 1,'output'] = "Color('{}" + df.loc[df.hit == 1, "element"].astype(str) + """{}'.format("{autogreen}", "{/autogreen}"))"""
                array = df["output"].tolist()
                array = [eval(x) for x in array]
                grid = [array[i:i+dim] for i in range(0, len(array), dim)]
                table_instance = SingleTable(grid)
                table_instance.inner_heading_row_border = False
                table_instance.inner_row_border = True
                table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
                print(table_instance.table) 
                continue
                
            # elif action == "RESET":
                # df["id"] = 0
                # df['output'] = "Color('{}" + df["element"].astype(str) + """{}'.format("{autoyellow}", "{/autoyellow}"))"""
                # array = df["output"].tolist()
                # array = [eval(x) for x in array]
                # grid = [array[i:i+dim] for i in range(0, len(array), dim)]
                # table_instance = SingleTable(grid)
                # print(table_instance.table) 
                # continue
                
            elif action == "RESTART":
                break
            
            elif action == "QUIT":
            	sys.exit(0)

            else:
                print("Sorry, what you entered is not in range. \nEnter item number which you hit. Enter RESTART for a new board. Enter QUIT to leave the application:  ")
                continue
        
        bingo()
        
    else:
        print("You must enter a number:  ")
        bingo()

def main():
    Windows.enable(auto_colors=True, reset_atexit=True)
    bingo()

if __name__ == '__main__':
    main()