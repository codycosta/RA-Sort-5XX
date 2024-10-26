
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


import os
import shutil
import time


# check we are in the current directory when running
print(f'\nRunning script in current folder:\t{os.getcwd()}')
print('Creating base folders...\n')


# create new base folders [CETUS, COG, EPSM, SL]
base_folders = ['CETUS', 'COG', 'EPSM', 'SL']

for folder in base_folders:
    if not os.path.exists(folder):
        print(f'creating folder:\t{os.getcwd()}\\{folder}')
        os.mkdir(folder)
        time.sleep(1/4)


# create sub folders for COG and EPSM for each threshold range [65, 75, and 85]
thresholds = ['65', '75', '85']

os.chdir('COG')
print(f'\n\nchanging folder to:\t{os.getcwd()}')
print('Creating COG thresholds...\n')

for threshold in thresholds:
    if not os.path.exists(threshold):
        print(f'creating folder:\t{os.getcwd()}\\{threshold}')
        os.mkdir(threshold)
        time.sleep(1/4)


os.chdir('../EPSM')
print(f'\n\nchanging folder to:\t{os.getcwd()}')
print('Creating EPSM thresholds...\n')

for threshold in thresholds:
    if not os.path.exists(threshold):
        print(f'creating folder:\t{os.getcwd()}\\{threshold}')
        os.mkdir(threshold)
        time.sleep(1/4)


# sub directories made, now we can begin organizing


# list files in parent directory and separate into base folders
os.chdir('../')


for file in os.listdir():
    
    name = os.path.splitext(file)[0]
    # print(name)

    # CETUS data
    if 'CETUS400V5' in name:
        shutil.move(file, 'CETUS')

    elif 'SPICA200V7' in name:

        # STARLIGHT DATA
        if 'UXRsl' in name or 'sl' in name and '-SL-' in name:
            shutil.move(file, 'SL')

        # COG DATA
        if 'COG' in name or '260C-' in name or '320C-' in name or '400C-' in name:
            shutil.move(file, 'COG')

        # EPSM DATA
        if 'EPSM' in name or '260E-' in name or '320E-' in name or '400E-' in name:
            if 'sl' not in name:
                shutil.move(file, 'EPSM')

            elif 'sl' in name and '-D2D-' in name or 'sl' in name and '-DDB-' in name:
                shutil.move(file, 'EPSM')


# categorize COG and EPSM data into threshold folders
print(f'\n\nChanging directory back to root folder:\t{os.getcwd()}')
print('Organizing CETUS/ and SL/ data...\n\n')

# COG DATA
os.chdir('COG')
print(os.getcwd())
print('Organizing COG thresholds...\n')
time.sleep(1/2)

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


# EPSM DATA
os.chdir('../EPSM')
print(os.getcwd())
print('Organizing EPSM thresholds...\n')
time.sleep(1/2)

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


print('\nDone :)\nSome folders may be empty, remove at your own disgression\n\n')
