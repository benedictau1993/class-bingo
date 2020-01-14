# Bingo!

This is a quick and dirty weekend project to build a Bingo game in Python 3. 

## Getting Started

The program requires a terminal resolution of at least 180 characters across. If its resolution is less than 180, the program will yell at you and ask you to adjust it. 

The program also requires the following Python packages:
- `numpy`, `pandas`, `colorclass`, `terminaltables`, `termcolor`

Install the above prerequisists with `pip` or your favourite package manager. 

## Deployment

`git clone` this repository then execute the python script in the Terminal: `cd [dir]; python bingo.py`.

Elements in the list objects should not exceed 40 alpha-numeric characters or contain quotation marks or apostrophes.

## Built With

- [Sublime Text](https://www.sublimetext.com/) - The text editor used

## Future developments:
- ~~Add Python curses window functionality to overwrite previous bingo board instead of printing a new board below every time the board is refreshed~~ Workaround done: use os.system() to clear screen instead of creating a curses window. Made compatible with both Unix and Windows systems.
- ~~Auto hit wild cards~~ Done with issubset().
- ~Logic when Bingo~ Done with subset().
- ~Special effects when Bingo~ Done. Blinking ASCII text art in UNIX terminals; however termcolor.cprint() is not supported on Windows terminals.
- ~Auto resolution check before program starts~ Done with subprocess.Popen().
- ~Bingo special effect only flashes at first Bingo so it's less annoying~ Done.
- Add auto pip install missing packages: this would be cool but a kitten would die whenever somebody uses `import pip` in code as a workaround for proper packaging
- Add method to securely add and store new elements for board. Perhaps in a separate file. Regex will be useful. 
- Integration with Google Sheets with Google API: use Google Sheets as a repo for board elements
- Interaction with other Bingo players; real time score updates for online players

## Author

- **Benedict Au** - [GitHub](https://github.com/benedictau1993/)

## License

This project is licensed under the MIT License.

## Acknowledgments

- Hat tip to the professors in the University of Chicago Master of Science in Analytics programme for providing the inspiration for this project
