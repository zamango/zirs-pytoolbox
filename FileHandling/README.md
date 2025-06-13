# FILEHANDLING

## This is a python module that contains classes I've pulled from my projects. They handle file operations like reading and writing to files, and other file-related tasks.

### Classes in this module:

#### DirectoryUtils:

##### A utility class that contains methods for working with directories and files.

#### Methods of this class:

##### - dirintlatest : Lists the latest version of a directory in a given path based on folder name.

##### - list_folders : Lists all child directories in a given path.

##### recentmfile : Finds the most recently modified file within the child directories of a given path.
##### - Looks inside each immediate subdirectory of fileroot
##### - For each subdirectory, it checks the file located at desendpath (relative to each subdirectory) if decendpath is provided
##### - Returns the full path to the most recently modified file

###### END

## Usage - How to use the classes in this module:

# Example: Use DirectoryUtils for VersionFinder
root_path = Path("C:/Game/Saves")
latest_version_folder = DirectoryUtils.dirintlatest(root_path)

if latest_version_folder:
    print(f"Latest version folder: {latest_version_folder}")

# Example: Use DirectoryUtils for FolderLister
folders = DirectoryUtils.list_folders(root_path)
if folders:
    for folder in folders:
        print(folder)

# Example: Use DirectoryUtils for RecentFileFinder
recent_file = DirectoryUtils.recentmfile(root_path, Path("subfolder/savefile.dat"))
if recent_file:
    print(f"Most recent file: {recent_file}")

##### Warning! These code snippets have been pulled from my projects. Not all of them have been tested as a standalone classes. Just inside of projects, therefore they may not function.