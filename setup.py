from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"
  

executables = [Executable("Polyboard.py", base=base, icon="final.ico")]

packages = ["pynput", "tkinter", "pyperclip", "os", "sys", "plyer", "win10toast"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Polyboard",
    options = options,
    version = "1.0.1",
    description = 'Copy paste widget',
    executables = executables
)
