import os, shutil, glob

root = os.getcwd()

for item in glob.glob(f'{root}/*'):
    if 'backup' not in item:
        shutil.rmtree(item, True)

back_dir = glob.glob(f'{root}/bac*')[-1]
print(f'restoring workspace from:\t{back_dir}')

for item in glob.glob(f'{back_dir}/*'):
    shutil.copy(item, root)