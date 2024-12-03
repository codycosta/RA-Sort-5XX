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

scan_types = ['CETUS', 'COG', 'EPSM', 'SL']
thresholds = ['65', '75', '85']

# RA file storage
root_dir = os.getcwd()

# loop through each file and find both scan type and threshold
for RA in glob.glob(f'{root_dir}/RA*.txt'):
    file_name = os.path.splitext(RA)[0]
    if not os.path.splitext(RA)[1] or os.path.splitext(RA)[1] != '.txt':
        continue

    if 'CETUS' in file_name:
        if not os.path.exists(f'{root_dir}/CETUS'):
            os.mkdir(f'{root_dir}/CETUS')
        shutil.move(RA, f'{root_dir}/CETUS')
        continue

    if 'SPICA' in file_name:
        if 'MC' in file_name:
            if '-DDB-' in file_name or '-D2D-' in file_name:
                threshold_idx_start = file_name.index('dbdd') + 4
                threshold = file_name[threshold_idx_start: threshold_idx_start + 2]
                if threshold == 'sl':
                    threshold = file_name[threshold_idx_start + 2: threshold_idx_start + 4]

                if 'COG' in file_name or '260C-' in file_name or '320C-' in file_name or '400C-' in file_name:
                    scan_type = 'COG'
                elif 'EPSM' in file_name or '260E-' in file_name or '320E-' in file_name or '400E-' in file_name:
                    scan_type = 'EPSM'
            
            elif '-SL-' in file_name:
                scan_type = 'SL'
                threshold_idx_start = file_name.index('-P') - 2
                threshold = file_name[threshold_idx_start: threshold_idx_start + 2]

        else:
            threshold_idx_start = file_name.index('-P') - 2
            threshold = file_name[threshold_idx_start: threshold_idx_start + 2]

            if 'COG' in file_name or '260C-' in file_name or '320C-' in file_name or '400C-' in file_name:
                scan_type = 'COG'
            elif 'EPSM' in file_name or '260E-' in file_name or '320E-' in file_name or '400E-' in file_name:
                scan_type = 'EPSM'
                if 'UXRsl' in file_name:
                    scan_type = 'SL'
                    


    destination = f'{root_dir}/{scan_type}/{threshold}'
    print(destination)

    # only create unique destination folders
    if not os.path.exists(f'{root_dir}/{scan_type}'):
        os.mkdir(f'{root_dir}/{scan_type}')
    if not os.path.exists(destination):
        os.mkdir(destination)

    # move file
    shutil.move(RA, destination)

# so far all is working within the testing environment, performs as intended
