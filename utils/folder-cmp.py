
# taken from copilot google answers, will test and revise to use as a solid folder comparator

import filecmp
import os

def compare_folders(dir1, dir2):
    """Compares two folders for equality."""

    # Compare the directories
    comparison = filecmp.dircmp(dir1, dir2)

    # Check if any files differ
    if comparison.diff_files:
        print("Different files:", comparison.diff_files)

    # Check for files only present in one directory
    if comparison.left_only:
        print("Files only in", dir1, ":", comparison.left_only)
    if comparison.right_only:
        print("Files only in", dir2, ":", comparison.right_only)

    # Recursively compare subdirectories
    for common_dir in comparison.common_dirs:
        compare_folders(os.path.join(dir1, common_dir), os.path.join(dir2, common_dir))

# Example usage:
dir1 = "folder1"
dir2 = "folder2"
compare_folders(dir1, dir2)