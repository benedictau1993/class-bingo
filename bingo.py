import sys
import math
import numpy as np
import pandas as pd
import random
from colorclass import Color, Windows
from terminaltables import SingleTable

datamining = ["Student visibly uncomfortable", 
                 "Calls out someone for using buzzwords",
                 "Still teaching at 4:31",
                 "Thats not interesting",
                 "Jab at B school",
                 "Flies through slides like Shree did",
                 "Ignores irrelevant question",
                 "Laptop battery warning",
                 "Flexes with breadth of knowledge",
                 "[WILD CARD]",
                 "[WILD CARD]"]

nonlinear = ["Is everyone finished? (no response)",
                "Blue checkered shirt + blazer",
                "Dataset where columns are flipped",
                "Yuri tells joke but doesnt smile",
                "Still teaching at 4:31",
                ">5s pause where no one answers Yuris question",
                "Financial example",
                "Entire hour of confusion",
                "ANOVA triangle",
                "Doesnt complete workshop",
                "Any questions? (nervous silence)",
                "Same person answers 4+ questions",
                "Leaves material for TA",
                "The answer to the question is on the slide",
                "[WILD CARD]",
                "[WILD CARD]"]

winterclasses = {1: datamining, 2: nonlinear}
print("\n\n")

print("██████╗  ██████╗ ██╗     ██╗      █████╗ ██████╗     ██████╗ ██╗███╗   ██╗ ██████╗  ██████╗ ")
print("██╔══██╗██╔═══██╗██║     ██║     ██╔══██╗██╔══██╗    ██╔══██╗██║████╗  ██║██╔════╝ ██╔═══██╗")
print("██║  ██║██║   ██║██║     ██║     ███████║██████╔╝    ██████╔╝██║██╔██╗ ██║██║  ███╗██║   ██║")
print("██║  ██║██║   ██║██║     ██║     ██╔══██║██╔══██╗    ██╔══██╗██║██║╚██╗██║██║   ██║██║   ██║")
print("██████╔╝╚██████╔╝███████╗███████╗██║  ██║██║  ██║    ██████╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝")
print("╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ")
                                                                                            
def bingo():
    course = input("\nFor which course would you like to play Bingo? Enter 1 for Data Mining, 2 for Non-linear. Enter QUIT to leave the application:  ")
    if course.isdigit() and int(course) in winterclasses: 
        dim = math.floor(math.sqrt(len(winterclasses[int(course)])))
        df = pd.DataFrame(data = np.random.choice(winterclasses[int(course)], dim**2, replace=False))
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
        table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center', 5: 'center'}
        print("\n")
        print(table_instance.table) 
        
        while True:
            action = input("\nEnter item number which you hit. Enter RESET to clear the board, RESTART for a new board, and QUIT to leave the application:  ")
            
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
                table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center', 5: 'center'}
                print("\n")
                print(table_instance.table) 
                continue
                
            elif action == "RESET":
                df["hit"] = 0
                df['output'] = "Color('{}" + df["element"].astype(str) + """{}'.format("{autoyellow}", "{/autoyellow}"))"""
                array = df["output"].tolist()
                array = [eval(x) for x in array]
                grid = [array[i:i+dim] for i in range(0, len(array), dim)]
                table_instance = SingleTable(grid)
                print("\n")
                print(table_instance.table) 
                continue
                
            elif action == "RESTART":
                break
            
            elif action == "QUIT":
            	sys.exit(0)

            else:
                print("Sorry, what you entered was not in range.")
                continue
        
        bingo()
        
    elif course == "QUIT":
        sys.exit(0)

    else:
        print("Sorry, what you entered was not in range. ")
        bingo()

def main():
    Windows.enable(auto_colors=True, reset_atexit=True)
    bingo()

if __name__ == '__main__':
    main()