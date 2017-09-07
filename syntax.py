from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QSyntaxHighlighter, QColor, QTextCharFormat, QFont

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

class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        self.highlighting_rules = []
        # pattern = regex pattern, format = colour/font formatting
        # all colour names http://www.december.com/html/spec/colorsvg.html

        # Keywords
        k_format = QTextCharFormat()
        k_colour = QColor()
        k_colour.setRgb(153, 137, 234)
        k_format.setForeground(k_colour)
        k_format.setFontWeight(QFont.Bold)
        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            self.highlighting_rules.append({"pattern":pattern, "format":k_format})

        # Boolean
        b_format = QTextCharFormat()
        b_colour = QColor()
        b_colour.setRgb(234, 61, 61)
        b_format.setForeground(b_colour)
        for word in boolean:
            pattern = QRegExp("\\b" + word + "\\b")
            self.highlighting_rules.append({"pattern":pattern, "format":b_format})

        # comparators_arithmetic_bitwise
        cab_format = QTextCharFormat()
        cab_colour = QColor()
        cab_colour.setRgb(199, 146, 234)
        cab_format.setForeground(cab_colour)
        for symbol in comparators_arithmetic_bitwise:
            pattern = QRegExp("\\"+symbol)
            self.highlighting_rules.append({"pattern":pattern, "format":cab_format})

        # Custom rules
        # self.highlighting_rules.append({"pattern":pattern, "format":format})

        num_format = QTextCharFormat()
        num_colour = QColor()
        num_colour.setNamedColor("darkorange")
        num_format.setForeground(num_colour)
        num_pattern = QRegExp("[0-9]")
        hex_pattern = QRegExp("0[xX][0-9a-fA-F]+")

        string_format = QTextCharFormat()
        s_colour = QColor()
        s_colour.setRgb(124, 179, 41)
        string_format.setForeground(s_colour)

        s_pattern1 = QRegExp( '\".*\"' )
        s_pattern1.setMinimal(True)  # Don't be greedy :(

        s_pattern2 = QRegExp( "\'(.*)\'" )
        s_pattern2.setMinimal(True)

        comment_format = QTextCharFormat()
        comment_colour = QColor()
        comment_colour.setNamedColor("grey")
        comment_format.setForeground(comment_colour)
        comment_pattern = QRegExp("\#.*")

        # Add to dict in the same order they should be applied (For example,
        # string highlighting needs to be applied after symbols, so if there is
        # a symbol in a string, it will be part of the string instead of having
        # the symbol highlighting)
        self.highlighting_rules.append({"pattern":num_pattern, "format":num_format})
        self.highlighting_rules.append({"pattern":hex_pattern, "format":num_format})
        self.highlighting_rules.append({"pattern":s_pattern1, "format":string_format})
        self.highlighting_rules.append({"pattern":s_pattern2, "format":string_format})
        self.highlighting_rules.append({"pattern":comment_pattern, "format":comment_format})

    def highlightBlock(self, text):
        for rule_dict in self.highlighting_rules:
            expression = QRegExp(rule_dict["pattern"])
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, rule_dict["format"])
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)

        match_multiline(QRegExp('"""'), string_format, 1)

    def match_multiline(self, delimiter, format,  block_state):
        pass
