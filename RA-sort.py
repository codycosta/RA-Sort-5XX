
'''

Author:     Cody Costa    
Company:    KLA Corporation
Title:      ATE3, 5XX BE LEAD
Date:       10/24/24

'''

# //////////////////////////////////////////////////////////////////////////////////////////////////////

# RA-sort.py
# script to help sort RA files into different folders based on scan type and residual threshold prior to placement in excel
# for use with 5XX SPICA and CETUS mask inspection RA files

# //////////////////////////////////////////////////////////////////////////////////////////////////////

# Root Directory/ (where RA files are stored, ready to be sorted)

#   RA-sort.py

#   CETUS/
#   COG/
#       |--> 65/
#       |--> 75/
#       |--> 85/
#   EPSM/
#       |--> 65/
#       |--> 75/
#       |--> 85/
#   SL/
#       |--> 65/
#       |--> 75/
#       |--> 85/

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

import os           # filesystem manipulation
import sys          # command line argument handling
import shutil       # high level file usage (copy, rename, etc)
import glob         # filename pattern matching
import time         # run timer
import datetime     # timestamp RA backup folders

os.system('')       # inject null character to terminal handler to reset ANSI bug for color coding



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Functions for terminal message coloring'''

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Display Title Message'''

print(
r'''
$$$$$$$\   $$$$$$\                                         $$\                             
$$  __$$\ $$  __$$\                                        $$ |                            
$$ |  $$ |$$ /  $$ |         $$$$$$$\  $$$$$$\   $$$$$$\ $$$$$$\        $$$$$$\  $$\   $$\ 
$$$$$$$  |$$$$$$$$ |$$$$$$\ $$  _____|$$  __$$\ $$  __$$\\_$$  _|      $$  __$$\ $$ |  $$ |
$$  __$$< $$  __$$ |\______|\$$$$$$\  $$ /  $$ |$$ |  \__| $$ |        $$ /  $$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |         \____$$\ $$ |  $$ |$$ |       $$ |$$\     $$ |  $$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |        $$$$$$$  |\$$$$$$  |$$ |       \$$$$  |$$\ $$$$$$$  |\$$$$$$$ |
\__|  \__|\__|  \__|        \_______/  \______/ \__|        \____/ \__|$$  ____/  \____$$ |
                                                                       $$ |      $$\   $$ |
                                                                       $$ |      \$$$$$$  |
                                                                       \__|       \______/      v1.2.1
''')
time.sleep(1)
time_start = datetime.datetime.now()

err_flag = False



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Create backup folder with all pulled RAs to easily reset the workspace if something goes wrong'''

# record root directory location (folder the script was run in)
root = os.getcwd()
print(f'\nRunning script in current folder:\t{root}')

# running in root directory
archive_folder = f'backup-{datetime.datetime.now().strftime('%Y-%m-%d')}'

if not os.path.exists(archive_folder):
    print('\nCreating RA backup folder...\n')
    print(f'created folder:\t{os.getcwd()}\\{archive_folder}\n')
    os.mkdir(archive_folder)

for file in glob.glob('RA*.txt'):
    shutil.copy(file, archive_folder)



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Create base folders for scan types'''

print('\nCreating base folders...\n')

# create new base folders [CETUS, COG, EPSM, SL]
base_folders = ['CETUS', 'COG', 'EPSM', 'SL']

for folder in base_folders:
    if not os.path.exists(folder):
        print(f'created folder:\t{os.getcwd()}\\{folder}')
        os.mkdir(folder)



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Create COG, EPSM, SL threshold folders'''

thresholds = ['65', '75', '85']

for folder in ['COG', 'EPSM', 'SL']:
    os.chdir(f'{root}/{folder}')

    print(f'\n\nCreating {folder} thresholds...\n')

    for t in thresholds:
        if not os.path.exists(t):
            print(f'created folder:\t{os.getcwd()}\\{t}')
            os.mkdir(t)



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Sort RA files first into base directory destinations'''

# list files in parent directory and separate into base folders
os.chdir(root)
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

print('\n\nOrganizing CETUS data...\n')

for folder in ['COG', 'EPSM', 'SL']:
    os.chdir(f'{root}/{folder}')

    print(f'Organizing {folder} thresholds...\n')

    for file in os.listdir():
        name = os.path.splitext(file)[0]

        if folder == 'COG' and 'MC' in name or folder == 'EPSM' and 'MC' in name:

            if 'P150' in name:
                shutil.move(file, '65')

            else:
                threshold_start = name.index('dbdd') + 4
                threshold = name[threshold_start: threshold_start + 2]

                if threshold == 'sl':
                    threshold = name[threshold_start + 2: threshold_start + 4]
                    
                shutil.move(file, threshold)

        else:

            if '65-P' in name:
                shutil.move(file, '65')

            elif '75-P' in name:
                shutil.move(file, '75')

            elif '85-P' in name:
                shutil.move(file, '85')


            # special case for X5.3 P72i tasks that don't follow conventional algo names
            # slsd and slmd algo tasks get thrown in TR65 folder

            elif 'slmd' in name or 'slsd' in name:
                shutil.move(file, '65')



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

        if not os.listdir():
            os.chdir(root)
            print(f'removed folder:\t{root}\\{folder}')
            shutil.rmtree(folder)

    os.chdir(root)



# //////////////////////////////////////////////////////////////////////////////////////////////////////
'''Optional inclusion to copy/move matching excel sheets into each folder'''

# my excel folder (relative to root) is '../blank-workbooks/'

if len(sys.argv) > 1:

    excel = sys.argv[1]

    print(f'\n\ncmd argument given, user chose to copy excel workbooks to folders...\n')

    try:
        os.chdir(root)
        os.chdir(excel)
    
    except FileNotFoundError:
        prRed(
            f'RA excel workbook folder \'{excel}\' not found, terminating program following RA sorting...\n'
        )

        prYellow(
f'''
\n\n////////////////////////////////////////////\n
PROCESS COMPLETED PARTIALLY!
time elapsed:\t{datetime.datetime.now() - time_start}\n
////////////////////////////////////////////\n
''')

        raise SystemExit


    excel_dir = os.getcwd()

    # still in excel dir while this loop is running
    for folder in os.listdir(root): # CETUS, COG, EPSM, SL      base folders
        if 'backup' in folder:
            continue

        try:
            excel_book = glob.glob(f'*{folder}*.xls*')[0]

        except IndexError:
            prRed(
                f'Excel book that matches {folder} scan type not found in provided excel folder...\n'
            )
            err_flag = True
            continue

        else:
            destinations = glob.glob(f'{root}/{folder}/*/')

            print(f'copying {excel_book} to:\t\t{root}\\{folder}\\*')

            if destinations:
                for path in destinations:
                    numRAs = len(glob.glob(f'{path}/*.P0.*.txt'))
                    shutil.copy(excel_book, path)
                    if numRAs > 10:
                        shutil.copy(excel_book, f'{path}/{os.path.splitext(excel_book)[0]}(2){os.path.splitext(excel_book)[1]}')

            else:
                shutil.copy(excel_book, f'{root}/{folder}')
                numRAs = len(glob.glob(f'{root}/{folder}/*.P0.*.txt'))
                if numRAs > 10:
                    shutil.copy(excel_book, f'{root}/{folder}/{os.path.splitext(excel_book)[0]}(2){os.path.splitext(excel_book)[1]}')



# display terminal message for when program finishes

if not err_flag:
    prGreen(
f'''
\n\n////////////////////////////////////////////\n
PROCESS COMPLETED SUCCESSFULLY!
time elapsed:\t{datetime.datetime.now() - time_start}\n
////////////////////////////////////////////\n
''')

else:
    prYellow(
f'''
\n\n////////////////////////////////////////////\n
PROCESS COMPLETED PARTIALLY!
time elapsed:\t{datetime.datetime.now() - time_start}\n
////////////////////////////////////////////\n
''')



# eof
