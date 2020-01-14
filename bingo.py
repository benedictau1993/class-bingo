import os
import sys
import math
import numpy as np
import pandas as pd
import random
import subprocess
from colorclass import Color, Windows
from terminaltables import SingleTable
from termcolor import colored, cprint

# Elements in the list objects should not exceed 40 alpha-numeric characters, and not contain quotation marks or apostrophes.
datamining = ("Student visibly uncomfortable", 
				 "Calls out someone for using buzzwords",
				 "Still teaching at 4:31",
				 "Thats not interesting",
				 "Jab at B school",
				 "Flies through slides like Shree did",
				 "Ignores irrelevant question",
				 "Laptop battery warning",
				 "Flexes with breadth of knowledge",
				 "[WILD CARD]")

nonlinear = ("Is everyone finished? (no response)",
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
				"[WILD CARD]")

winterclasses = {1: datamining, 2: nonlinear}

bingo3 = ({1,2,3}, {4,5,6}, {7,8,9}, {1,4,7}, {2,5,8}, {3,6,9}, {1,5,9}, {3,5,7})
bingo4 = ({1,2,3,4}, {5,6,7,8}, {9,10,11,12}, {13,14,15,16}, {1,5,9,13}, {2,6,10,14}, {3,7,11,15}, {4,8,12,16}, {1,6,11,16}, {4,7,10,13})

colors = ("autoblack", "autored", "autogreen", "autoyellow", "autoblue", "automagenta", "autocyan", "autowhite")
randcolor = random.choice(colors)

def resolutioncheck():	# grabs console width and checks if width > 180
	while int(subprocess.Popen(["tput", "cols"], stdout=subprocess.PIPE).communicate()[0]) < 180:
		print("\n\n")
		print("****************************************")
		print("************* DOLLAR BINGO *************")
		print("****************************************")
		print("\nThe width of your current console is",int(subprocess.Popen(["tput", "cols"], stdout=subprocess.PIPE).communicate()[0]))
		print("which is less than the recommended 180.")
		print("Please adjust your console and press ENTER.\n\n")
		input("Press ENTER to continue... ")
		os.system('cls' if os.name == 'nt' else 'clear')

def printtitle():	# prints in random color from list
	print("\n\n\n\n\n")
	print(Color('{}              ██████╗  ██████╗ ██╗     ██╗      █████╗ ██████╗     ██████╗ ██╗███╗   ██╗ ██████╗  ██████╗ {}'.format("{"+randcolor+"}", "{/"+randcolor+"}")))
	print(Color('{}              ██╔══██╗██╔═══██╗██║     ██║     ██╔══██╗██╔══██╗    ██╔══██╗██║████╗  ██║██╔════╝ ██╔═══██╗{}'.format("{"+randcolor+"}", "{/"+randcolor+"}")))
	print(Color('{}              ██║  ██║██║   ██║██║     ██║     ███████║██████╔╝    ██████╔╝██║██╔██╗ ██║██║  ███╗██║   ██║{}'.format("{"+randcolor+"}", "{/"+randcolor+"}")))
	print(Color('{}              ██║  ██║██║   ██║██║     ██║     ██╔══██║██╔══██╗    ██╔══██╗██║██║╚██╗██║██║   ██║██║   ██║{}'.format("{"+randcolor+"}", "{/"+randcolor+"}")))
	print(Color('{}              ██████╔╝╚██████╔╝███████╗███████╗██║  ██║██║  ██║    ██████╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝{}'.format("{"+randcolor+"}", "{/"+randcolor+"}")))
	print(Color('{}              ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ {}'.format("{"+randcolor+"}", "{/"+randcolor+"}")))

def printbingo(bingo_score):	# cprint() allows flashing text in most UNIX terminals, but not Windows
	if bingo_score == 0:		# flashes during intial Bingo only
		print("\n")
		cprint('                                   ╔═════════════════════════════════════════════════╗', 'yellow', attrs = ['blink'])
		cprint('                                   ║                                                 ║', 'yellow', attrs = ['blink'])
		cprint('                                   ║  ██████╗ ██╗███╗   ██╗ ██████╗  ██████╗ ██╗██╗  ║', 'yellow', attrs = ['blink'])
		cprint('                                   ║  ██╔══██╗██║████╗  ██║██╔════╝ ██╔═══██╗██║██║  ║', 'yellow', attrs = ['blink'])
		cprint('                                   ║  ██████╔╝██║██╔██╗ ██║██║  ███╗██║   ██║██║██║  ║', 'yellow', attrs = ['blink'])
		cprint('                                   ║  ██╔══██╗██║██║╚██╗██║██║   ██║██║   ██║╚═╝╚═╝  ║', 'yellow', attrs = ['blink'])
		cprint('                                   ║  ██████╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝██╗██╗  ║', 'yellow', attrs = ['blink'])
		cprint('                                   ║  ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ║', 'yellow', attrs = ['blink'])
		cprint('                                   ║                                                 ║', 'yellow', attrs = ['blink'])
		cprint('                                   ╚═════════════════════════════════════════════════╝', 'yellow', attrs = ['blink'])
		return (bingo_score + 1)	# return the value, and assign/overwrite it outside the function

	else:						# stops flashing after intial Bingo so it's less annoying to user
		print("\n")
		print(Color('{yellow}                                   ╔═════════════════════════════════════════════════╗{/yellow}'))
		print(Color('{yellow}                                   ║                                                 ║{/yellow}'))
		print(Color('{yellow}                                   ║  ██████╗ ██╗███╗   ██╗ ██████╗  ██████╗ ██╗██╗  ║{/yellow}'))
		print(Color('{yellow}                                   ║  ██╔══██╗██║████╗  ██║██╔════╝ ██╔═══██╗██║██║  ║{/yellow}'))
		print(Color('{yellow}                                   ║  ██████╔╝██║██╔██╗ ██║██║  ███╗██║   ██║██║██║  ║{/yellow}'))
		print(Color('{yellow}                                   ║  ██╔══██╗██║██║╚██╗██║██║   ██║██║   ██║╚═╝╚═╝  ║{/yellow}'))
		print(Color('{yellow}                                   ║  ██████╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝██╗██╗  ║{/yellow}'))
		print(Color('{yellow}                                   ║  ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ║{/yellow}'))
		print(Color('{yellow}                                   ║                                                 ║{/yellow}'))
		print(Color('{yellow}                                   ╚═════════════════════════════════════════════════╝{/yellow}'))

def bingo():
	global bingo_score
	bingo_score = 0
	os.system('cls' if os.name == 'nt' else 'clear')
	resolutioncheck()
	printtitle()
	course = input("\n\n\n\nFor which course would you like to play Bingo? Enter 1 for Data Mining, 2 for Non-linear. Enter QUIT to leave the application:  ")
	if course.isdigit() and int(course) in winterclasses: 
		dim = min(math.floor(math.sqrt(len(winterclasses[int(course)]))), 4)	# dimension of the bingo board, maximum is 4x4
		df = pd.DataFrame(data = np.random.choice(winterclasses[int(course)], dim**2, replace=False))	# random draw without replacement from list above
		df.rename(columns={0: "element"}, inplace = True)
		df["id"] = range(1,dim**2+1)	# assigns unique id to each item on bingo board
		df["element"] = df["id"].map(str) + ". " +  df["element"].map(str)	# appends unique id each item
		df["hit"] = 0	# binary vector that stores whether the item has been hit
		df['output'] = "Color('{}" + df["element"].astype(str) + """{}'.format("{autoblack}", "{/autoblack}"))"""		# column that holds the Color() object as string
		df.loc[df["element"].str.contains("WILD CARD"), 'hit'] = 1	# auto hit WILD CARDs
		df.loc[df.hit == 1,'output'] = "Color('{}" + df.loc[df.hit == 1, "element"].astype(str) + """{}'.format("{autogreen}", "{/autogreen}"))"""	# any item that has been hit is showed in green
		array = df["output"].tolist()
		array = [eval(x) for x in array]	# converts "Color()" to a Color()
		grid = [array[i:i+dim] for i in range(0, len(array), dim)]	# turn 1D Python (base Python, not NumPy) list to 2D list
		table_instance = SingleTable(grid, "Data Mining" if int(course)==1 else "Non-linear" if int(course)==2 else "")		# adds class name to top left of bingo board
		table_instance.inner_heading_row_border = False
		table_instance.inner_row_border = True
		table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center'}
		os.system('cls' if os.name == 'nt' else 'clear')
		resolutioncheck()
		printtitle()
		print("\n")
		print(table_instance.table) 
		
		while True:
			action = input("\n\nEnter item number which you hit. Enter RESET to clear the board, RESTART for a new board, and QUIT to leave the application:  ")

			if action.isdigit() and int(action) in df['id'].values:
				os.system('cls' if os.name == 'nt' else 'clear')
				resolutioncheck()
				printtitle()
				df.loc[df.id == int(action), "hit"] = df.loc[df.id == int(action), "hit"].replace({0:1, 1:0})	# switches 0 <-> 1 if item has been hit/unhit
				df['output'] = "Color('{}" + df["element"].astype(str) + """{}'.format("{autoblack}", "{/autoblack}"))"""		# any item that hasn't been hit is showed in black
				df.loc[df["element"].str.contains("WILD CARD"), 'hit'] = 1	# auto hit WILD CARDs
				df.loc[df.hit == 1,'output'] = "Color('{}" + df.loc[df.hit == 1, "element"].astype(str) + """{}'.format("{autogreen}", "{/autogreen}"))"""				# any item that has been hit is showed in green
				array = df["output"].tolist()
				array = [eval(x) for x in array]
				grid = [array[i:i+dim] for i in range(0, len(array), dim)]
				table_instance = SingleTable(grid, "Data Mining" if int(course)==1 else "Non-linear" if int(course)==2 else "")
				table_instance.inner_heading_row_border = False
				table_instance.inner_row_border = True
				table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center'}
				print("\n")
				print(table_instance.table)

				if dim == 3 and any([set(i).issubset(set(df[df['hit']==1]["id"].tolist())) for i in bingo3]):	# if Bingo then print flashing bingo message
					bingo_score = printbingo(bingo_score)	# return the value, and assign/overwrite it outside the function:


				elif dim == 4 and any([set(i).issubset(set(df[df['hit']==1]["id"].tolist())) for i in bingo4]):	# if Bingo then print flashing bingo message
					bingo_score = printbingo(bingo_score)	# return the value, and assign/overwrite it outside the function:


				else:
					continue
				
			elif action == "RESET":
				os.system('cls' if os.name == 'nt' else 'clear')
				resolutioncheck()
				printtitle()
				bingo_score = 0
				df["hit"] = 0	# resets hit vector to zeros
				df.loc[df["element"].str.contains("WILD CARD"), 'hit'] = 1	# auto hit WILD CARDs
				df['output'] = "Color('{}" + df["element"].astype(str) + """{}'.format("{autoblack}", "{/autoblack}"))"""		# hence all items should be in black
				df.loc[df.hit == 1,'output'] = "Color('{}" + df.loc[df.hit == 1, "element"].astype(str) + """{}'.format("{autogreen}", "{/autogreen}"))"""	# any item that has been hit is showed in green
				array = df["output"].tolist()
				array = [eval(x) for x in array]
				grid = [array[i:i+dim] for i in range(0, len(array), dim)]
				table_instance = SingleTable(grid, "Data Mining" if int(course)==1 else "Non-linear" if int(course)==2 else "")
				table_instance.inner_heading_row_border = False
				table_instance.inner_row_border = True
				table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center'}
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
		cprint('\n\n\n\n                                              Press ENTER to continue... ', 'yellow', attrs = ['blink'])
		input("")
		bingo()

def main():
	Windows.enable(auto_colors=True, reset_atexit=True)
	bingo()

if __name__ == '__main__':
	main()
