
# Cody Costa    KLA ATE3
# 10/24/24

# //////////////////////////////////////////////////////////////////////////////////////////////////////

# RA-sort.py
# script to help sort RA files into different folders based on scan type and residual threshold prior to placement in excel
# for use with 5XX SPICA and CETUS mask inspection RA files

# //////////////////////////////////////////////////////////////////////////////////////////////////////

# Root Directory/ (where RA files are stored, ready to be sorted)

#   RA-sort.py

#   COG/
#   --> 65/
#   --> 75/
#   --> 85/

#   EPSM/
#   --> 65/
#   --> 75/
#   --> 85/

#   CETUS/

#   SL/

# //////////////////////////////////////////////////////////////////////////////////////////////////////

# running python 3.12 at the time of development
# python version 3.7 or later should be supported due to the use of f strings


# usage:    ~\ >>   python [path to RA-sort.py]

# //////////////////////////////////////////////////////////////////////////////////////////////////////

# How to run:

# STEP 1:   Ensure first you have a version of python installed on your machine

# you can download your prefered version from:  https://www.python.org/
# if you are unsure which version to run, a safe bet is to install the latest release


# STEP 2:   Edit your system path variable to allow your machine to call upon python

# NOTE: RealPython has a very good guide on how to do this (with pictures) here:  https://realpython.com/add-python-to-path/

# press the windows key
# type 'env', and click on the box that says "Edit the sytem environment variables"
# click Environment variables near the bottom of the window
# down under the "system variables" section find the variable named Path and click, then click the edit button below
# click New
# type in the path to your python executable in the new line, found in:     C:\Users\<USER>\AppData\Local\Programs\Python\Python312 <-- or whichever version you are running
# click OK on all the open windows to close them
# your system path variable should now include python


# STEP 3:   Turn off python execution aliases

# press the windows key
# type 'App execution aliases' and click the first result
# scroll down until you find 2 programs named 'App Installer' with python.exe and python3.exe listed under the name
# turn both of these off
# your system should be ready to run the file now :)


# STEP 4:   Reference the file when running

# if your python file exists in Downloads\ and your RA files exist in Documents\
# you would run the script as such:

#       ~ >>  cd Documents        (navigate to directory where RA files are held to sort)
#       ~/Documents >>  python ../Downloads/RA-sort.py



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Needed Python Packages'''

import os
import sys
import shutil
import time     # well maybe this one isn't really needed



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Create base folders for scan types'''

# record root directory location (folder the script was run in)
root = os.getcwd()

print(f'\nRunning script in current folder:\t{root}')
print('\nCreating base folders...\n')


# create new base folders [CETUS, COG, EPSM, SL]
base_folders = ['CETUS', 'COG', 'EPSM', 'SL']

for folder in base_folders:
    if not os.path.exists(folder):
        print(f'created folder:\t{os.getcwd()}\\{folder}')
        os.mkdir(folder)
        time.sleep(1/8)



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Create sub folders for thresholds'''

thresholds = ['65', '75', '85']

for folder in ['COG', 'EPSM']:
    os.chdir(f'{root}/{folder}')

    print(f'\n\nCreating {folder} thresholds...\n')

    for t in thresholds:
        if not os.path.exists(t):
            print(f'created folder:\t{os.getcwd()}\\{t}')
            os.mkdir(t)
            time.sleep(1/8)



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Sort RA files first into base directory destinations'''

# list files in parent directory and separate into base folders
os.chdir('../')
for file in os.listdir():
    
    name = os.path.splitext(file)[0]

    # CETUS
    if 'CETUS400V5' in name:
        shutil.move(file, 'CETUS')

    elif 'SPICA200V7' in name:

        # STARLIGHT
        if 'UXRsl' in name or 'sl' in name and '-SL-' in name:
            shutil.move(file, 'SL')

        # COG
        if 'COG' in name or '260C-' in name or '320C-' in name or '400C-' in name:
            shutil.move(file, 'COG')

        # EPSM
        if 'EPSM' in name or '260E-' in name or '320E-' in name or '400E-' in name:
            if 'sl' not in name:
                shutil.move(file, 'EPSM')

            elif 'sl' in name and '-D2D-' in name or 'sl' in name and '-DDB-' in name:
                shutil.move(file, 'EPSM')



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Sort RA files into respective thresholds'''

print('\n\nOrganizing CETUS/ and SL/ data...\n')
time.sleep(1/8)

for folder in ['COG', 'EPSM']:
    os.chdir(f'{root}/{folder}')

    print(f'Organizing {folder} thresholds...\n')

    for file in os.listdir():
        name = os.path.splitext(file)[0]

        if 'MC' in name:
            shutil.move(file, '75')

        elif '65-P' in name and 'MC' not in name:
            shutil.move(file, '65')

        elif '75-P' in name and 'MC' not in name:
            shutil.move(file, '75')

        elif '85-P' in name and 'MC' not in name:
            shutil.move(file, '85')

    time.sleep(1/2)



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Delete any empty folders'''

print('\nRemoving any empty directories...\n')
os.chdir(root)

for folder in base_folders:

    # check base folders for emptiness
    if not os.listdir(folder):
        print(f'removed folder:\t{root}\\{folder}')
        shutil.rmtree(folder)

    else:
        os.chdir(folder)

        # check thresholds for emptiness
        for item in os.listdir():

            if os.path.splitext(item)[1] == '.txt':
                continue
            
            if not os.listdir(item):
                print(f'removed folder:\t{os.getcwd()}\\{item}')
                shutil.rmtree(item)

    os.chdir(root)



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Optional inclusion to copy/move matching excel sheets into each folder'''

# my excel folder (relative to root) is '../../blank-workbooks/'

if len(sys.argv) > 1:

    excel = sys.argv[1]

    print(f'\n\ncmd argument given, user chose to copy excel workbooks to folders...\n')

    os.chdir(root)
    os.chdir(excel)

    excel_dir = os.getcwd()

    for folder in os.listdir(root): # CETUS, COG, EPSM, SL      base folders
        os.chdir(f'{root}/{folder}')


        numRAs = sum(['.P0.' in file for file in os.listdir()])

        os.chdir(excel_dir)
        for file in os.listdir():
            if folder in file:
                print(f'copying {file}\tto:\t{root}\\{folder}\\*')
                shutil.copy(file, f'{root}/{folder}')

                if numRAs > 10:
                    shutil.move(f'{root}/{folder}/{file}', f'{root}/{folder}/{os.path.splitext(file)[0]}(2){os.path.splitext(file)[1]}')
                    shutil.copy(file, f'{root}/{folder}')

    os.chdir(root)
    for folder in ['COG', 'EPSM']:

        excel_book = os.listdir(folder)[-1]

        for thresholds in os.listdir(folder)[:-1]:
                shutil.copy(f'{root}/{folder}/{excel_book}', f'{root}/{folder}/{thresholds}')

                # if len(os.listdir(f'{folder}/{thresholds}')) > 11:
                if sum(['.P0.' in file for file in os.listdir(f'{folder}/{thresholds}')]) > 10:
                    shutil.move(f'{root}/{folder}/{thresholds}/{excel_book}', f'{root}/{folder}/{thresholds}/{os.path.splitext(excel_book)[0]}(2){os.path.splitext(excel_book)[1]}')
                    shutil.copy(f'{root}/{folder}/{excel_book}', f'{root}/{folder}/{thresholds}')

        os.remove(f'{folder}/{excel_book}')



# display terminal message for when program finishes

print(
'''\n\n////////////////////////////////////////////\n
PROCESS COMPLETED SUCCESSFULLY\n
////////////////////////////////////////////\n'''
)
