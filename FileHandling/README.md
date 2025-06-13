# FileHandling.py

This is `filehandling.py`, a Python module that provides useful utilities for handling file and directory operations. 
It includes functions to find the latest version directories, list subdirectories, and locate the most recently modified file within a directory structure. 
These utilities can be used across various projects to streamline file management tasks.

## Classes

### `VersionFinder`
The `VersionFinder` class provides functionality for identifying the latest version directory in a given path based on the directory name, not timestamps.

#### `dirintlatest(root_dir: Path, version_pattern: Optional[Pattern] = None) -> Optional[Path]`
- **Parameters**:
  - `root_dir`: The root directory in which to search for version directories.
  - `version_pattern`: An optional regex pattern to match version directories (defaults to `r"^(\d+)\.(\d+)(?:\.(\d+))?$"`).
- **Returns**: The path of the latest version directory found, or `None` if no version directories are found.

### `SaveLister`
The `SaveLister` class provides a method for listing all child directories in a given path.

#### `list_saves(sav_root: Path) -> Optional[Path]`
- **Parameters**:
  - `sav_root`: The root directory to search for subdirectories.
- **Returns**: A list of subdirectories (as paths), or `None` if no subdirectories are found.

### `RecentFileFinder`
The `RecentFileFinder` class helps locate the most recently modified file in child directories under a given path.

#### `recent_playattpath(fileroot: Path, desendpath: Path) -> Optional[Path]`
- **Parameters**:
  - `fileroot`: The root directory where the search begins.
  - `desendpath`: The relative path to the file within each child directory to check for modification time.
- **Returns**: The full path of the most recently modified file, or `None` if no valid file is found.

## Usage Example

```python
from filehandling import VersionFinder, SaveLister, RecentFileFinder
from pathlib import Path

# Example of finding the latest version directory
root_dir = Path("/path/to/directories")
latest_version_dir = VersionFinder.dirintlatest(root_dir)
print(f"The latest version directory is: {latest_version_dir}")

# Example of listing save directories
sav_root = Path("/path/to/saves")
save_dirs = SaveLister.list_saves(sav_root)
print(f"Save directories: {save_dirs}")

# Example of finding the most recently modified file
fileroot = Path("/path/to/files")
desendpath = "file_to_check.txt"
recent_file = RecentFileFinder.recent_playattpath(fileroot, desendpath)
print(f"The most recently modified file is: {recent_file}")


