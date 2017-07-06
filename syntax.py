from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QSyntaxHighlighter, QColor, QTextCharFormat, QFont

boolean     = ["False", "None", "True"]

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

        single_line_text_format = QTextCharFormat()
        slt_colour = QColor()
        slt_colour.setRgb(124, 179, 41)
        single_line_text_format.setForeground(slt_colour)

        slt_pattern1 = QRegExp( '\".*\"' )
        slt_pattern1.setMinimal(True)  # Don't be greedy :(
        self.highlighting_rules.append({"pattern":slt_pattern1, "format":single_line_text_format})

        slt_pattern2 = QRegExp( "\'(.*)\'" )
        slt_pattern2.setMinimal(True)
        self.highlighting_rules.append({"pattern":slt_pattern2, "format":single_line_text_format})

        quote_format = QTextCharFormat()
        quote_colour = QColor()
        quote_colour.setNamedColor("grey")
        quote_format.setForeground(quote_colour)
        quote_pattern = QRegExp("\#.*")
        self.highlighting_rules.append({"pattern":quote_pattern, "format":quote_format})

        num_format = QTextCharFormat()
        num_colour = QColor()
        num_colour.setNamedColor("darkorange")
        num_format.setForeground(num_colour)
        num_pattern = QRegExp("[0-9]")
        self.highlighting_rules.append({"pattern":num_pattern, "format":num_format})
        hex_pattern = QRegExp("0[xX][0-9a-fA-F]+")
        self.highlighting_rules.append({"pattern":hex_pattern, "format":num_format})

    def highlightBlock(self, text):
        for rule_dict in self.highlighting_rules:
            expression = QRegExp(rule_dict["pattern"])
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, rule_dict["format"])
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)
