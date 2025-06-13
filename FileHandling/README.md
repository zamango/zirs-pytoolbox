# FILEHANDLING

## This is a python module that contains classes I've pulled from my projects. They handle file operations like reading and writing to files, and other file-related tasks.

### Classes in this module:

#### Versionfinder : Lists the latest version of a directory in a given path based off folder name.

#### FolderLister : Lists all child directories in a given path

#### RecentFileFinder : Finds the most recently modified file within the child directories of a given path.
####    - Looks inside each immediate subdirectory of `fileroot`
####    - For each subdirectory, it checks the file located at `desendpath` (relative to each subdirectory) if decendpath is provided
####    - Returns the full path to the most recently modified file

## Usage - How to use the classes in this module:

```python
# Example: Use VersionFinder
root_path = Path("C:/Game/Saves")
latest_version_folder = VersionFinder.dirintlatest(root_path)

if latest_version_folder:
    print(f"Latest version folder: {latest_version_folder}")

# Example: Use FolderLister
folders = FolderLister.list_folders(root_path)
if folders:
    for folder in folders:
        print(folder)

# Example: Use RecentFileFinder
recent_file = RecentFileFinder.recentmfile(root_path, Path("subfolder/savefile.dat"))
if recent_file:
    print(f"Most recent file: {recent_file}") ```

