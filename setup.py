import cx_Freeze

executables=[cx_Freeze.Executable("23.py")]

cx_Freeze.setup(

name="slither",
options={"build.exe":{"packages":["pygame"],"include_files":["apple2.png","Untitled.png"]}},

description = "funny game",

executables = executables






    )
