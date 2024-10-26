
# script to reset the testing env for RA-sort.py

import os
import shutil

base_folders = ['CETUS', 'COG', 'EPSM', 'SL']

for folder in base_folders:
    if os.path.exists(folder):
        shutil.rmtree(folder)

os.chdir('backup')

for file in os.listdir():
    shutil.copy(file, '../')

