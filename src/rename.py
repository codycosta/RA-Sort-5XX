
# utility script to rename files in bulk, useful for correcting consistent typos and incorrect labeling

import shutil
import glob
import sys


# define input arguments
if len(sys.argv) != 4:
    raise Exception('file usage:\t python [path to rename.py] [substring to replace] [replacement substring] [files to apply changes to]')

substring_to_replace = sys.argv[1]
new_substring = sys.argv[2]
files_to_apply_changes = glob.glob(sys.argv[3])


# check for good inputs
if not glob.glob(f'*{substring_to_replace}*'):
    raise ValueError(f'no results found for substring: \'{substring_to_replace}\' in current folder')

if not files_to_apply_changes:
    raise ValueError(f'no results found for: \'{sys.argv[3]}\' in current folder')


for file in files_to_apply_changes:

    if substring_to_replace not in file:
        continue

    # mark string slice to replace
    substring_index_start = file.index(substring_to_replace)
    substring_index_end = substring_index_start + len(substring_to_replace)

    # concatenate strings to form new file name
    new_filename = file[:substring_index_start] + new_substring + file[substring_index_end:]

    # rename file
    shutil.move(file, new_filename)
    print(f'Renamed {file} to:\t{new_filename}')

print()
