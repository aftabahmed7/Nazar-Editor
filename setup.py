import cx_Freeze
import sys
import os
base =None


if sys.platform =='win32' :
    base ="win32GUI"
    

os.environ['TCL_LIBRARY']=r"C:\Users\HP\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY']=r"C:\Users\HP\AppData\Local\Programs\Python\Python311\tcl\tk8.6"


executable = [cx_Freeze.Executable("Nazar_editor.py", base=base ,icon="app_logo.ico")]


cx_Freeze.setup(
    name = "Nazar Editor",
    options ={"build_exe":{"packages":["tkinter","os"],"include_files":["app_logo.ico",'tcl86t.dll','tk86t.dll','icon2']}},
    version ="0.02",
    description ="Tkinter Application",
    executables = executable
    )
