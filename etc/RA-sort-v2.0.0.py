# new script to test refactors/improvements to the program

'''

Author:     Cody Costa    
Company:    KLA Corporation
Title:      ATE3, 5XX BE LEAD
Date:       12/3/2024

*************************************

Planned changes:

1.  remove the step to delete empty folders
    - instead just create the needed folders

2.  clump sorting into one step instead of individual base and threshold steps

'''

# ****************************************************************************
''' Test code changes here '''

import os, shutil, glob, sys, datetime, time
version = '2.0.0'
os.system('')


def prRed(skk): 
    print(f"\033[91m {skk}\033[00m")

def prGreen(skk): 
    print(f"\033[92m {skk}\033[00m")

def prYellow(skk): 
    print(f"\033[93m {skk}\033[00m")

def prCyan(skk): 
    print(f"\033[96m {skk}\033[00m")


def display_title_msg() -> None:
    print(
f'''
8888888b.         d8888                                  888                          
888   Y88b       d88888                                  888                          
888    888      d88P888                                  888                          
888   d88P     d88P 888        .d8888b   .d88b.  888d888 888888     88888b.  888  888 
8888888P"     d88P  888        88K      d88""88b 888P"   888        888 "88b 888  888 
888 T88b     d88P   888 888888 "Y8888b. 888  888 888     888        888  888 888  888 
888  T88b   d8888888888             X88 Y88..88P 888     Y88b.  d8b 888 d88P Y88b 888 
888   T88b d88P     888         88888P'  "Y88P"  888      "Y888 Y8P 88888P"   "Y88888 
                                                                    888           888 
                                                                    888      Y8b d88P 
                                                                    888       "Y88P"        v{version}
'''
    )
    time.sleep(1)


def backup_src(root_dir: str) -> None:
    prCyan('backing up RA files')
    archive_folder = f'backup-{datetime.datetime.now().strftime('%Y-%m-%d')}'
    if not os.path.exists(f'{root_dir}/{archive_folder}'):
        os.mkdir(f'{root_dir}/{archive_folder}')
        print(f'populating RA backup folder:\t{os.getcwd()}\\{archive_folder}')
        for file in glob.glob(f'{root_dir}/RA*.txt'):
            shutil.copy(file, archive_folder)
    else:
        prYellow(f'Existing backup found:\t{root_dir}\\{archive_folder}')


def src_file_sort(root_dir: str) -> None:
    prCyan('sorting source RA files')
    Destinations = []
    # loop through each file and find both scan type and threshold
    for RA in glob.glob(f'{root_dir}/RA*.txt'):
        if 'CETUS' in RA:
            if not os.path.exists(f'{root_dir}/CETUS'):
                os.mkdir(f'{root_dir}/CETUS')
                print(f'populating destination folder:\t{root_dir}\\CETUS')
                Destinations.append(f'{root_dir}/CETUS')
            shutil.move(RA, f'{root_dir}/CETUS')

        elif 'SPICA' in RA:
            if 'COG' in RA or '260C-' in RA or '320C-' in RA or '400C-' in RA:
                scan_type = 'COG'
            elif 'EPSM' in RA or '260E-' in RA or '320E-' in RA or '400E-' in RA:
                scan_type = 'EPSM'

            if 'MC' in RA:
                if '-DDB-' in RA or '-D2D-' in RA:
                    threshold_idx_start = RA.index('dbdd') + 4
                    threshold = RA[threshold_idx_start: threshold_idx_start + 2]
                    if threshold == 'sl':
                        threshold = RA[threshold_idx_start + 2: threshold_idx_start + 4]

                elif '-SL-' in RA:
                    scan_type = 'SL'
                    threshold_idx_start = RA.index('-P') - 2
                    threshold = RA[threshold_idx_start: threshold_idx_start + 2]
            
            else:
                threshold_idx_start = RA.index('-P') - 2
                threshold = RA[threshold_idx_start: threshold_idx_start + 2]
                if 'UXRsl' in RA and scan_type == 'EPSM':
                    scan_type = 'SL'
                        
        destination = f'{root_dir}\\{scan_type}\\{threshold}'
        if not os.path.exists(destination):
            os.makedirs(destination)
            print(f'populating destination folder:\t{destination}')
            Destinations.append(destination)

        # move file
        shutil.move(RA, destination)
    
    # return data for excel files
    if len(sys.argv) == 2:
        excel_file_sort(root_dir, Destinations)


def excel_file_sort(root_dir:str, Destinations: list) -> None:
    prCyan('transferring appropriate excel files')
    excel_dir = sys.argv[1]
    scan_types = ['CETUS', 'COG', 'EPSM', 'SL']
    try:
        os.chdir(root_dir)
        os.chdir(excel_dir)
        excel_dir = os.getcwd()
    except FileNotFoundError:
        prRed(f'{excel_dir} folder not found')
        raise SystemExit
    
    for folder in Destinations:
        numRAs = len(glob.glob('RA*P0*.txt'))
        for Type in scan_types:
            if Type in folder:
                scan_type = Type
                break
        try:
            matching_excel_book = glob.glob(f'{excel_dir}/*{scan_type}*')[0]
        except IndexError:
            prRed(f'excel file for scan type {scan_type} not found')
        else:
            shutil.copy(matching_excel_book, folder)
            print(f'copied {os.path.basename(matching_excel_book)} to:\t{folder}')
            if numRAs > 10:
                shutil.copy(
                    f'{os.path.splitext(matching_excel_book)[0]}(2){os.path.splitext(matching_excel_book)[1]}', folder
                )
                print(f'copied {os.path.basename(matching_excel_book)} to:\t{folder}')


def main() -> None:
    display_title_msg()
    time_start = datetime.datetime.now()
    root_dir = os.getcwd()

    backup_src(root_dir)
    src_file_sort(root_dir)

    prGreen(f'runtime:\t {datetime.datetime.now() - time_start}')

main()

# program runs almost twice as fast as v1.2.4
# missing all the visual fluff however

# running about 25% faster than v1.2.4
# added RA backup folder creation step which takes time
