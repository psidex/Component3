from sys import path
path.append("lib/py_hex")
from os import remove
from de_compiler import de_compile
from compiler import compile_to_hex

script = """
from microbit import *

while True:
    display.scroll("1234")
    sleep(500)

"""
filename = "test.hex"

with open(filename, "wb") as out:
    out.write(compile_to_hex(script.encode("utf-8")))

d = de_compile(filename)

remove(filename)

assert d == script, "py_hex failed"
print("[test] py_hex passed")
