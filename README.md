# Component_3 - BBC Micro:Bit Python IDE

## res -> py

`pyuic5 file.ui -o file.py`

`pyrcc5 res.qrc -o res_rc.py`

## Regex for later

Match square brackets `\['([\S\s]*?)\]`

def + 1 word `\bdef\b\s*(\w+)`

comments `#(.*)`

## Notes / Used sources

Icons from https://feathericons.com/

Qt5 Stuff:
https://stackoverflow.com/
http://zetcode.com/gui/pyqt5
http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/
http://pyqt.sourceforge.net/Docs/PyQt4/qfiledialog.html

Syntax highlighter help:
https://github.com/art1415926535/PyQt5-syntax-highlighting
http://carsonfarmer.com/2009/07/syntax-highlighting-with-pyqt/
https://regex101.com/
http://www.rexegg.com/regex-quickstart.html
http://www.december.com/html/spec/colorsvg.html

## ToDo

 - Implement regex from above
 - Look into line numbers
 - Look into word-completion
 - Add all buttons
 - Inserting tabs when enter is pressed
 - Test generated .hex with real microbit
 - Look into Flashing, RELP, & viewing microbit's internal files
