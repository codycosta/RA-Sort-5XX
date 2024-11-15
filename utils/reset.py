
# script to reset the testing env for RA-sort.py

import os
import shutil
import glob

# base_folders = ['CETUS', 'COG', 'EPSM', 'SL']
root = os.getcwd()

for folder in os.listdir():
    if 'backup' not in folder:
        shutil.rmtree(folder)

backup_folder = glob.glob('backup')[0]
os.chdir(backup_folder)

print(f'\nRestoring workspace from:\t{root}\\{backup_folder}\n')

for file in os.listdir():
    shutil.copy(file, '../')

