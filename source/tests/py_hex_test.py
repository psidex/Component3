from sys import path
path.append("../lib/py_hex")
from compiler import compile_to_hex
from de_compiler import de_compile

script = """
from microbit import *

while True:
    display.scroll("1234")
    sleep(500)

"""

with open("test.hex", "wb") as out:
    out.write(compile_to_hex(script.encode("utf-8")))

d = de_compile("test.hex")

if d == script:
    print("same")
else:
    print("broke")
