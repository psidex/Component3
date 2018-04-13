from PyQt5.QtWidgets import QFileDialog
from .py_hex.compiler import compile_to_hex
from .py_hex.de_compiler import de_compile

def save_to_hex(path, script):
    with open(path, "wb") as outhex:
        outhex.write(compile_to_hex(script.encode("utf-8")))

def save_to_py(path, script):
    with open(path, "w") as outpy:
        outpy.write(script)

def open_from_hex(filename):
    return de_compile(filename)

def open_from_py(filename):
    with open(filename, "r") as openpy:
        return openpy.read()

def open_file_dialouge(types):
    return QFileDialog.getOpenFileName(caption="Open file", directory="/home", filter=types)[0]

def save_file_dialouge(types):
    return QFileDialog.getSaveFileName(caption="Save file", directory="/home", filter=types)[0]
