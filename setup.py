import sys
from cx_Freeze import setup, Executable

packages = ['numpy']
base = None

#if sys.platform == "win32":
#    base = "Win32GUI"

setup(
    name = "python_matrix",
    version = "1.0.0",
    description = "Python matrix solver!",
    options = {'build_exe': {'packages': packages}},
    executables = [Executable("matrix.py", base=base)]
)