import os
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
				 "[WILD CARD]"]

nonlinear = ["Is everyone finished? (no response)",
				"Blue checkered shirt + blazer",
				"Dataset where columns are flipped",
				"Yuri tells joke but doesnt smile",
				"Still teaching at 4:31",
				">5s pause where no one answers question",
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

def printtitle():
	print("\n")
	print(Color('{yellow}                 ██████╗  ██████╗ ██╗     ██╗      █████╗ ██████╗     ██████╗ ██╗███╗   ██╗ ██████╗  ██████╗ {/yellow}'))
	print(Color('{yellow}                 ██╔══██╗██╔═══██╗██║     ██║     ██╔══██╗██╔══██╗    ██╔══██╗██║████╗  ██║██╔════╝ ██╔═══██╗{/yellow}'))
	print(Color('{yellow}                 ██║  ██║██║   ██║██║     ██║     ███████║██████╔╝    ██████╔╝██║██╔██╗ ██║██║  ███╗██║   ██║{/yellow}'))
	print(Color('{yellow}                 ██║  ██║██║   ██║██║     ██║     ██╔══██║██╔══██╗    ██╔══██╗██║██║╚██╗██║██║   ██║██║   ██║{/yellow}'))
	print(Color('{yellow}                 ██████╔╝╚██████╔╝███████╗███████╗██║  ██║██║  ██║    ██████╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝{/yellow}'))
	print(Color('{yellow}                 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ {/yellow}'))
																			
def bingo():
	os.system('cls' if os.name == 'nt' else 'clear')
	printtitle()
	course = input("\nFor which course would you like to play Bingo? Enter 1 for Data Mining, 2 for Non-linear. Enter QUIT to leave the application:  ")
	if course.isdigit() and int(course) in winterclasses: 
		dim = math.floor(math.sqrt(len(winterclasses[int(course)])))	# dimension of the bingo board
		df = pd.DataFrame(data = np.random.choice(winterclasses[int(course)], dim**2, replace=False))	# random draw without replacement from list above
		df.rename(columns={0: "element"}, inplace = True)
		df["id"] = range(1,dim**2+1)	# assigns unique id to each item on bingo board
		df["element"] = df["id"].map(str) + ". " +  df["element"].map(str)	# appends unique id each item
		df["hit"] = 0	# binary vector that stores whether the item has been hit
		df['output'] = "Color('{}" + df["element"].astype(str) + """{}'.format("{autoblue}", "{/autoblue}"))"""		# column that holds the Color() object as string
		array = df["output"].tolist()
		array = [eval(x) for x in array]	# converts "Color()" to a Color()
		grid = [array[i:i+dim] for i in range(0, len(array), dim)]	# turn 1D Python (base Python, not NumPy) list to 2D list
		table_instance = SingleTable(grid, "Data Mining" if int(course)==1 else "Non-linear" if int(course)==2 else "")		# adds class name to top left of bingo board
		table_instance.inner_heading_row_border = False
		table_instance.inner_row_border = True
		table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center', 5: 'center'}
		print("\n")
		print(table_instance.table) 
		
		while True:
			action = input("\nEnter item number which you hit. Enter RESET to clear the board, RESTART for a new board, and QUIT to leave the application:  ")
			
			if action.isdigit() and int(action) in df['id'].values:
				os.system('cls' if os.name == 'nt' else 'clear')
				printtitle()
				df.loc[df.id == int(action), "hit"] = df.loc[df.id == int(action), "hit"].replace({0:1, 1:0})	# switches 0 <-> 1 if item has been hit/unhit
				df['output'] = "Color('{}" + df["element"].astype(str) + """{}'.format("{autoblue}", "{/autoblue}"))"""		# any item that hasn't been hit is showed in blue
				df.loc[df.hit == 1,'output'] = "Color('{}" + df.loc[df.hit == 1, "element"].astype(str) + """{}'.format("{autogreen}", "{/autogreen}"))"""				# any item that has been hit is showed in blue
				array = df["output"].tolist()
				array = [eval(x) for x in array]
				grid = [array[i:i+dim] for i in range(0, len(array), dim)]
				table_instance = SingleTable(grid, "Data Mining" if int(course)==1 else "Non-linear" if int(course)==2 else "")
				table_instance.inner_heading_row_border = False
				table_instance.inner_row_border = True
				table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center', 5: 'center'}
				print("\n")
				print(table_instance.table) 
				continue
				
			elif action == "RESET":
				os.system('cls' if os.name == 'nt' else 'clear')
				printtitle()
				df["hit"] = 0	# resets hit vector to zeros
				df['output'] = "Color('{}" + df["element"].astype(str) + """{}'.format("{autoblue}", "{/autoblue}"))"""		# hence all items should be in blue
				array = df["output"].tolist()
				array = [eval(x) for x in array]
				grid = [array[i:i+dim] for i in range(0, len(array), dim)]
				table_instance = SingleTable(grid, "Data Mining" if int(course)==1 else "Non-linear" if int(course)==2 else "")
				table_instance.inner_heading_row_border = False
				table_instance.inner_row_border = True
				table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center', 5: 'center'}
				print("\n")
				print(table_instance.table) 
				continue
				
			elif action == "RESTART":
				break
			
			elif action == "QUIT":
				os.system('cls' if os.name == 'nt' else 'clear')
				sys.exit(0)		# exits the program so no need for ^C keyboardinterrupt

			else:
				print("Sorry, what you entered was not in range.")
				continue
		
		bingo()
		
	elif course == "QUIT":
		os.system('cls' if os.name == 'nt' else 'clear')
		sys.exit(0)

	else:
		print("Sorry, what you entered was not in range. ")
		bingo()

def main():
	Windows.enable(auto_colors=True, reset_atexit=True)
	bingo()

if __name__ == '__main__':
	main()