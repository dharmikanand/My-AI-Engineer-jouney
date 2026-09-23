#organizing of files and folders can be automated by python
#the shutil module
#the shutil module has functions to let copy,move,remove and delete files in your python programs
from pathlib import Path
h=Path.cwd()
(h / 'spam').mkdir(exist_ok=True)
with open(h/'spam/file1.txt','w',encoding='UTF-8') as file:
    file.write('Hello')
#this will create a folder named spam with file named file1.txt.
#shutil module provides functions like shutil.copy(source,destination) will copy at the path source to the folder at the path
import shutil
shutil.copy(h/'spam/file1.txt',h/'spam/file2.txt') 
#it will copy the info in the source file to destination fiel if not there it will create anew file adn copy into it with creating the name that you gave in the destination
#shutil.move(source,destination) will move the files from source to destination
(h/'spam2').mkdir()
shutil.move(h/'spam/file1.txt',h/'spam2')
#you can permenantly delete files and folders with functions in the os module
import shutil
shutil.rmtree('C:/Users/dharm/My-AI-Engineer-journey/spam')
#Calling shutil.rmtree(path) will delete (that is, remove) the entire folder tree at path, including all the files and subfolders it contains.
import os
os.unlink('C:/Users/dharm/My-AI-Engineer-journey/spam2/file1.txt')
#Calling os.unlink(path) will delete the single file at path.
os.rmdir('C:/Users/dharm/My-AI-Engineer-journey/spam2')
#Calling os.rmdir(path) will delete the folder at path. This folder must be empty.
import send2trash
#send2trash.send2trash('file1.txt') 
#this will delete the file adn move it into recycle bin

#if you want to list all the files and subfolders ina folder,call os.listdir
import os
print(os.listdir('C:/Users/dharm/My-AI-Engineer-journey'))
#we can also get list of path objects in a folder by calling the iterdir() method
from pathlib import Path
home=Path.cwd()
print(home.iterdir())

#os.walk() function will return three values unlike range()
# import os, shutil
# from pathlib import Path
# h = Path.home()

# for folder_name, subfolders, filenames in os.walk(h / 'spam'):
#     print('The current folder is ' + folder_name)

#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)

#     for filename in filenames:
#         print('FILE INSIDE ' + folder_name + ': '+ filename)
#         # Rename file to uppercase:
#         p = Path(folder_name)
#         shutil.move(p / filename, p / filename.upper())
   
#     print('')

#os.walk() returns lists of strings for the subfolder adn filename variables,you can use the return vlaues in their own for loops

#Compressing files into zip files
import zipfile
with open('C:/Users/dharm/My-AI-Engineer-journey/file1.txt','w',encoding='utf-8') as file_obj:
    file_obj.write("hello"*10000)
with zipfile.ZipFile('example.zip','w') as example_zip:
     example_zip.write('file1.txt',compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
import zipfile
example_zip=zipfile.ZipFile('example.zip')
print(example_zip.namelist())
file_info=example_zip.getinfo('file1.txt')
print(file_info.file_size)
print(file_info.compress_size)
#extracting files from zipfiles
import zipfile
example_zip=zipfile.ZipFile('example.zip')
example_zip.extractall()
example_zip.close()
