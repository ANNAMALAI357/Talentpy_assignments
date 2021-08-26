from main import OperatingSystem as OS
mem = OS()
print("Please the os operation you want to do:")
print("""1.directory of the given path 
2.Show the current directory
3.copy files from one folder to another""")
i = int(input())
if(i==1):
    Path = input("Enter the path to be searched: ")
    print(mem.show_directories(Path))
elif(i==2):
    print(mem.get_current_directory())
elif(i==3):
    source = input("enter the source of the file to be copied: ")
    destination = input("enter the destination of the file: ")
    print(mem.copyFile(source,destination))
else:
    print("Invalid option")
