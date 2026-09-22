#varibles are the best way to store the dat but if you want your data to be persisitent even after your program is finished then you have to use files
#A file has two properties:filename and location
from pathlib import Path
print(Path('spam','bacon','eggs'))
print(str(Path('spam','bacon','eggs')))
#for combining two paths we have to / operator which is normally used for divison
print(Path('spam')/'bacon'/'eggs')
#Acessing the curretn working directory
import os
print(Path.cwd())#shows the current working directory
#os.chdir('C:\\Windows\\System32')
#os.chdir() is used to change the directory from any other directory
#There is no pathlib function for changing the working directory. You must use os.chdir().
#Accessing the home directory
print(Path.home())
#Absolute vs Relative Paths
#an absolute path,which is always begins with the root folder(C:\ on windows)
#a relative path,which is relative to the program's current direcotry
#there are also dot(.) and dot-dot(..) folders.A sigle dot is ashorthand notation for this folder adn two dots means the parent folder
#creating new folder
# os.mkdirs(c:\\delcious\\walnut\\waffles)
#os.mkdirs will create any necessay intermediate folders to ensure that the full path exists.
print(Path.cwd().is_absolute())
print(Path('C:/users/dharm/My-AI-engineer-journey').is_absolute())
#.is_absolute() gives true if the directory written is correct else false
#the parts of a filepath:
#the anchor,which is the root folder of the filesystem
#on windows,the drive,which is the single letter that often denotes a physical harddrive or other storage device
#the parent,which is the folder that contains the file
#the name of the file,made up of the stem
p=Path('c:/users/AI/spam.txt')
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)
print(p.parts)
print(p.parts[3])
print(Path('C:/users/dharm/My-AI-engineer-journey').stat())
#.stat() method is size of file in bytes.you can divide by 1024,by 1024** 2,by 1024 ** 3 to get the size in KB,MB, or GB respectively.
#glob() method is for listing any content in the folder that matches the glob pattern
#.exists() return true if the path exists,and return false if it doesnt exist
#.is_file() return true if the path exists and is a file,and returns false otherwise
#.is_dir() return true if the path exists and is a directory,and returns false if not
p=Path('spam.txt')
p.write_text('Hello world')
print(p.read_text())
#path object is used for only basic interactions with the file.
#themore common way of writing toa file involves using open() function and file objects
p=open(Path.cwd() / 'spam.txt',encoding='UTF-8')
print(p.read())

file=open('bacon.txt','w')
file.write('Hello World\n')
file.close()
file=open('bacon.txt','a')
file.write('Bacon is not a vegetable.')
file.close()
file=open('bacon.txt','r')
print(file.read())
file.close()
#by using with you can close the file automatically after doing the operations
with open('bacon.txt','r') as file:
    print(file.read())

#You can save variables in your Python programs to binary shelf files using the shelve module. This lets your program restore that data to the variables the next time it is run. You could use this technique to add Save and Open features to your program; for example, if you ran a program and entered some configuration settings, you could save those settings to a shelf file and then have the program load the settings the next time it is run.
import shelve
shelf_file = shelve.open('mydata')
shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']
shelf_file.close()
shelf_file = shelve.open('mydata')
print(shelf_file['cats'])
#shelve module frees you from worrying about how to store your programs data
#just like dictioanries we have keys(). and values() methods that will return list-like values
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()