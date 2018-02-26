from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["tkinter"], excludes = [], include_files = [r"C:\Users\Brian\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll", \
                 r"C:\Users\Brian\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll"])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('mboxreader.py', base=base)
]

setup(name='MBox-Reader',
      version = '1.0',
      description = 'Anaylze an mbox file, exported from MGail, to find your most common email senders.',
      options = dict(build_exe = buildOptions),
      executables = executables)
