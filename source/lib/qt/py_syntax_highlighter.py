import json
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QSyntaxHighlighter, QColor, QTextCharFormat, QFont

"""
Example usage:
self.highlighter = python_syntax_highlighter(self.text_editor.document())

Most of these words are from
>>> import keyword
>>> print(keyword.kwlist)
"""

boolean = ["False", "None", "True"]

keywords = [
    "and", "as", "assert", "break", "class", "continue", "def", "del", "elif",
    "else", "except", "finally", "for", "from", "global", "if", "import", "in",
    "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try",
    "while", "with", "yield", "self"
]

comparators_arithmetic_bitwise = [
    "<", ">", "!", "+", "-", "*", "/", "%", "=", "|", "^", "&", "~"
]

class python_syntax_highlighter(QSyntaxHighlighter):
    def __init__(self, document):
        # Load theme
        themeDict = json.load(open("theme.json"))

        # Init highlighter with given text document
        QSyntaxHighlighter.__init__(self, document)

        self.highlighting_rules = []
        """
        pattern = regex pattern to find, format = QTextCharFormat -> colour/font
        all colour names @ http://www.december.com/html/spec/colorsvg.html
        """

        # Keywords
        k_format = QTextCharFormat()
        k_colour = QColor()
        k_colour.setRgb(*[int(i) for i in themeDict["keyword"].split(",")])
        k_format.setForeground(k_colour)
        k_format.setFontWeight(QFont.Bold)
        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            self.highlighting_rules.append({"pattern":pattern, "format":k_format})

        # Boolean
        b_format = QTextCharFormat()
        b_colour = QColor()
        b_colour.setRgb(*[int(i) for i in themeDict["boolean"].split(",")])
        b_format.setForeground(b_colour)
        for word in boolean:
            pattern = QRegExp("\\b" + word + "\\b")
            self.highlighting_rules.append({"pattern":pattern, "format":b_format})

        # Comparators, arithmetic & bitwise
        cab_format = QTextCharFormat()
        cab_colour = QColor()
        cab_colour.setRgb(*[int(i) for i in themeDict["comparators-arithmetic-bitwise"].split(",")])
        cab_format.setForeground(cab_colour)
        for symbol in comparators_arithmetic_bitwise:
            pattern = QRegExp("\\"+symbol)
            self.highlighting_rules.append({"pattern":pattern, "format":cab_format})

        num_format = QTextCharFormat()
        num_colour = QColor()
        num_colour.setRgb(*[int(i) for i in themeDict["number"].split(",")])
        num_format.setForeground(num_colour)
        num_pattern = QRegExp("[0-9]")
        hex_pattern = QRegExp("0[xX][0-9a-fA-F]+")

        self.string_format = QTextCharFormat()
        s_colour = QColor()
        s_colour.setRgb(*[int(i) for i in themeDict["string"].split(",")])
        self.string_format.setForeground(s_colour)

        s_pattern1 = QRegExp( '\".*\"' )
        s_pattern1.setMinimal(True)  # Don't be greedy :(

        s_pattern2 = QRegExp( "\'(.*)\'" )
        s_pattern2.setMinimal(True)

        func_format = QTextCharFormat()
        func_colour = QColor()
        func_colour.setRgb(*[int(i) for i in themeDict["function"].split(",")])
        func_format.setForeground(func_colour)
        func_patten = QRegExp("([\w\-]+)(?=\()")

        comment_format = QTextCharFormat()
        comment_colour = QColor()
        comment_colour.setRgb(*[int(i) for i in themeDict["comment"].split(",")])
        comment_format.setForeground(comment_colour)
        comment_pattern = QRegExp("\#.*")

        """
        Add to dict in the same order they should be applied (For example,
        string highlighting needs to be applied after symbols, so if there is
        a symbol in a string, it will be part of the string instead of having
        the symbol highlighting)
        """
        self.highlighting_rules.append({"pattern":num_pattern, "format":num_format})
        self.highlighting_rules.append({"pattern":hex_pattern, "format":num_format})
        self.highlighting_rules.append({"pattern":func_patten, "format":func_format})
        self.highlighting_rules.append({"pattern":s_pattern1, "format":self.string_format})
        self.highlighting_rules.append({"pattern":s_pattern2, "format":self.string_format})
        self.highlighting_rules.append({"pattern":comment_pattern, "format":comment_format})

    def highlightBlock(self, text):
        """
        For each rule, see if the pattern matches anything in "the current text block"

        """
        for rule_dict in self.highlighting_rules:
            expression = QRegExp(rule_dict["pattern"])
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, rule_dict["format"])
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)

        self.match_multiline_comment(text, QRegExp('"""'), 1)
        self.match_multiline_comment(text, QRegExp("'''"), 2)

    def match_multiline_comment(self, text, delimiter, block_state):
        """
        Not perfect but it's good enough :)
        """
        # If inside multiline comment, start at index 0
        if self.previousBlockState() == block_state:
            start = 0
            offset = 0
        # Else start at the index
        else:
            start = delimiter.indexIn(text)
            offset = 3  # Len of """ / '''

        # If there is a match
        if start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + offset)

            # If found
            if end >= start + offset:
                # Format up to and including delimiter ("""/''')
                length = end + 3
                self.setCurrentBlockState(0)  # We have finished highlighting the text
            else:
                # Format whole line and let next call know it is still in multi-line "mode"
                self.setCurrentBlockState(block_state)
                length = len(text)

            # Format text from start -> length using self.string_format
            self.setFormat(start, length, self.string_format)
