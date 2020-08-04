import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os', 'dotenv', 'secrets', 'asyncio',
                                  'random', 'json', 'locale', 'dateutil'],
                     'build_exe': './/build'}
base = None
# if sys.platform == 'win32':
#     base = 'Win32GUI'

setup(
    name='LorePets',
    version='1.0',
    description='Python chat bot for Twitch',
    options={'build_exe': build_exe_options},
    executables=[Executable('LorePets.py', base=base)]
)
