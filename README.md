## Let's play Bingo!
##### Benedict Au | Jan 2020

This is a bingo board generator for the Terminal, rather than IPython. It is written in Python 3.

#### Program requirements

Terminal resolution: at least 180 char across. 
The program also requires the following dependencies:
- numpy
- pandas
- random
- colorclass
- terminaltables
- termcolor

#### Future developments:
- ~~Add Python curses window functionality to overwrite previous bingo board instead of printing a new board below every time the board is refreshed~~ Workaround done: use os.system() to clear screen instead of creating a curses window. Made compatible with both Unix and Windows systems.
- ~~Auto hit wild cards~~ Done. 
- ~Logic when Bingo~ Done with subset()
- ~Special effects when Bingo~ Done. Blinking ASCII text art in UNIX terminals; termcolor.cprint() is not supported on Windows terminals
- Integration with Google Sheets with Google API: use Google Sheets as a repo for board elements
- Interaction with other Bingo players; real time score updates for online players
