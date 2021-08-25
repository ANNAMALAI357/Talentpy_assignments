from main import OperatingSystem as OS
import os
import shutil
mem = OS()
print("Please the os operation you want to do:")
print("""1.directory of the given path 
2.Show the current directory
3.copy files from one folder to another""")
i = int(input())
if(i==1):
    print(mem.show_directories())
elif(i==2):
    print(mem.get_current_directory())
elif(i==3):
    print(mem.copyFile())
else:
    print("Invalid option")
