from cx_Freeze import *

includefiles = ['cal.ico.jpg']
base = None
if sys.platform =='win32':
    base = "win32GUI"

shortcut_table = [
    ("DesktopShortcut", # Shortcut
     "DesktopFolder", # Directory_
     "My Calculator", # Name
     "TARGETDIR", # Component )
     "[TARGETDIR]\SMARTCALCULATOR.exe", # Target
     None, # Arguements
     None, # Description
     None, # Hotkey
     None, # Icon
     None, # IconIndex
     None, # ShowCmd
     "TARGETDIR", # Wkdir
     )
]
msi_data = {"Shortcut": shortcut_table}

# change some default MSI options and specify the use of above defined tables
bdist_msi_options = {'data':msi_data}
setup(
    version="0.1",
    description="My Calculator",
    author="Yash Kumar",
    name="My Calculator",
    options={'build_exe':{'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executable=[
        Executable(
            script="smartcalculator.py",
            base=base,
            icon='cal.ico.jpg',
        )
    ]
)