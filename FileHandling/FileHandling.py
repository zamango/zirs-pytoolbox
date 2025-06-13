import os
import re
from pathlib import Path
from typing import Optional, Pattern

class VersionFinder:
    # Lists the latest version of a directory in a given path based off folder name, not timestamps.
    @staticmethod
    def dirintlatest(root_dir: Path, version_pattern: Optional[Pattern] = None) -> Optional[Path]:
        version_dirs = []
        if version_pattern is None:
            version_pattern = re.compile(r"^(\d+)\.(\d+)(?:\.(\d+))?$")
        try:
            for child in root_dir.iterdir():
                if not child.is_dir():
                    continue

                match = version_pattern.match(child.name)
                if not match:
                    continue

                parts = match.groups(default="0")
                version_tuple = tuple(int(p) for p in parts)
                version_dirs.append((version_tuple, child))
        except (FileNotFoundError, PermissionError):
            return None

        if not version_dirs:
            return None

        latest_version, latest_dir = max(version_dirs, key=lambda x: x[0])
        return latest_dir

class SaveLister:
    # Lists all child directories in a given path
    @staticmethod
    def list_saves(sav_root: Path) -> Optional[Path]:
        candidates = []
        try:
            for item in sav_root.iterdir():
                if item.is_dir():
                    candidates.append((item.name, item))
        except (FileNotFoundError, PermissionError):
            return None

        if not candidates:
            return None
        return candidates

class RecentFileFinder:
    ''' 
    Finds the most recently modified file within the child directories of a given path.

    - Looks inside each immediate subdirectory of `fileroot`
    - For each subdirectory, it checks the file located at `desendpath` (relative to each subdirectory)
    - Returns the full path to the most recently modified file, or None if no valid files are found
    '''
    @staticmethod
    def recent_playattpath(fileroot: Path, desendpath: Path) -> Optional[Path]:
        autosaves = []
        datemod = []
        try:
            for child in fileroot.iterdir():
                if not child.is_dir():
                    continue
                autosaves.append(child)
        except (FileNotFoundError, PermissionError):
            return None

        if not autosaves:
            return None

        try:
            for autosave in autosaves:
                d8modified = os.path.getmtime(autosave / desendpath)
                datemod.append((d8modified, autosave))
        except (FileNotFoundError, PermissionError):
            return None

        if not datemod:
            return None

        latest_mod, latest_autosav = max(datemod, key=lambda x: x[0])
        recentplayattpath = fileroot / latest_autosav / desendpath
        return recentplayattpath


