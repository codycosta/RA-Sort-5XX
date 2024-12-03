# new script to test refactors/improvements to the program

'''
Planned changes:

1.  remove the step to delete empty folders
    - instead just create the needed folders

2.  clump sorting into one step instead of individual base and threshold steps

'''

# ****************************************************************************
''' Test code changes here '''

import os, shutil, glob

# RA file storage
root_dir = os.getcwd()

# loop through each file and find both scan type and threshold
for RA in glob.glob(f'{root_dir}/RA*.txt'):
    # Tested and working
    if 'CETUS' in RA:
        if not os.path.exists(f'{root_dir}/CETUS'):
            os.mkdir(f'{root_dir}/CETUS')
            print(f'{root_dir}\\CETUS')
        shutil.move(RA, f'{root_dir}/CETUS')
        continue

    if 'SPICA' in RA:
        # Still untested, need MC files to test
        if 'MC' in RA:
            if '-DDB-' in RA or '-D2D-' in RA:
                threshold_idx_start = RA.index('dbdd') + 4
                threshold = RA[threshold_idx_start: threshold_idx_start + 2]
                if threshold == 'sl':
                    threshold = RA[threshold_idx_start + 2: threshold_idx_start + 4]

                if 'COG' in RA or '260C-' in RA or '320C-' in RA or '400C-' in RA:
                    scan_type = 'COG'
                elif 'EPSM' in RA or '260E-' in RA or '320E-' in RA or '400E-' in RA:
                    scan_type = 'EPSM'
            
            elif '-SL-' in RA:
                scan_type = 'SL'
                threshold_idx_start = RA.index('-P') - 2
                threshold = RA[threshold_idx_start: threshold_idx_start + 2]
        
        # Tested and working
        else:
            threshold_idx_start = RA.index('-P') - 2
            threshold = RA[threshold_idx_start: threshold_idx_start + 2]

            if 'COG' in RA or '260C-' in RA or '320C-' in RA or '400C-' in RA:
                scan_type = 'COG'
            elif 'EPSM' in RA or '260E-' in RA or '320E-' in RA or '400E-' in RA:
                scan_type = 'EPSM'
                if 'UXRsl' in RA:
                    scan_type = 'SL'
                    
    destination = f'{root_dir}\\{scan_type}\\{threshold}'
    if not os.path.exists(destination):
        os.makedirs(destination)
        print(destination)

    # move file
    shutil.move(RA, destination)

# so far all is working within the testing environment, performs as intended
