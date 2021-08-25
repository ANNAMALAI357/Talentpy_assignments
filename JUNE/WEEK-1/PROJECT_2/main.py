"""
Create a simple python class OperatingSystem with following methods 
Hint: Use OS module
1. show_directories(“path”) -> This function should print list of directories in a given
path. Example: show_directories(“C://myfolder") should list files inside myfolder of
C drive.
2. get_current_working_directory() -> This function should print the current working
directory.
3. copyFile(source, destination) -> This function should copy a file from a given
source path to given destination path. For example: source : C:/talentpy/test.txt
and destination is D:/talent/myfolder. Then this function should copy test.txt to D:/
talent/myfolder.
Create another file runner.py and import OperatingSystem class and call show_directories,
get_current_working_directory and copyFile methods.
"""

import os
import shutil
class OperatingSystem:
    def __init__(self):
        pass
    def show_directories(self):
        Path = input("Enter the path to be searched: ")
        return os.path.dirname(Path)
    def get_current_directory(self):
        current = os.getcwd()
        return current
    def copyFile(self):
        source = input("enter the source of the file to be copied: ")
        destination = input("enter the destination of the file: ")
        return shutil.copyfile(source,destination)
