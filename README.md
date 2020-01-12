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

#### Future developments:
- ~~Add Python `curses` window functionality to overwrite previous bingo board instead of printing a new board below every time the board is refreshed~~ Workaround done: use `os.system()` to clear screen instead of creating a `curses` window. Made compatible with both Unix and Windows systems.
- ~~Auto hit wild cards~~ Done
- Integration with Google Sheets with Google API
- Logic when Bingo
- Special effects when Bingo
- Interaction with other Bingo players
