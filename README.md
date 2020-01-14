# Bingo!

This is a Bingo board generator for the Terminal. It is written in Python 3.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project.

### Prerequisites

The program requires a terminal resolution of at least `180` characters across. Parse `tput cols` in the terminal to grab the width of the console window. 

The program also requires the following Python packages:
- `os`, `sys`, `math`, `numpy`, `pandas`, `random`, `colorclass`, `terminaltables`, `termcolor`

## Deployment

`git clone` this repository and install the above prerequisists with `pip` or your favourite package manager. Then execute the python script in the Terminal: `cd [dir]; python bingo.py`.

Elements in the list objects should not exceed 40 alpha-numeric characters, and not contain quotation marks or apostrophes.

## Built With

- [Sublime Text](https://www.sublimetext.com/) - The text editor used

## Future developments:
- ~~Add Python curses window functionality to overwrite previous bingo board instead of printing a new board below every time the board is refreshed~~ Workaround done: use os.system() to clear screen instead of creating a curses window. Made compatible with both Unix and Windows systems.
- ~~Auto hit wild cards~~ Done with issubset().
- ~Logic when Bingo~ Done with subset().
- ~Special effects when Bingo~ Done. Blinking ASCII text art in UNIX terminals; termcolor.cprint() is not supported on Windows terminals
- ~Auto resolution check before program starts~ Done with subprocess.Popen().
- ~Bingo special effect only flashes at first Bingo so it's less annoying~ Done.
- Add method to securely append new elements for board. Regex will be useful. 
- Integration with Google Sheets with Google API: use Google Sheets as a repo for board elements
- Interaction with other Bingo players; real time score updates for online players

## Author

- **Benedict Au** - [GitHub](https://github.com/benedictau1993/)

## License

This project is licensed under the MIT License.

## Acknowledgments

- Hat tip to the professors in the University of Chicago Master of Science in Analytics programme for providing the inspiration for this project
