#Designing and deploting command line programs
#in this we will learn how to run programs in the command line interface
#cmd is more convenient way to run the programs
#program is a complete sotware,large or small with instructions that a computer carries out
#Script A program that an interpreter runs from its source-code form rather than from a compiled, machine-code form. This is a very loose term. Python programs are often called scripts even though Python code can be compiled like other languages (as you’ll learn in “Compiling Python Programs with PyInstaller” on page 285).
# Command A program that is often run from a text-based terminal and doesn’t have a graphical user interface (GUI). All configuration is done up front by specifying command line arguments before running the command (although interactive commands may sometimes interrupt their operation with an “Are you sure? Y/N” question for the user). Both dir and ls, explained in “The cd, pwd, dir, and ls Commands” on page 260, are examples of commands.

# Shell script A single text file that conveniently runs several bundled terminal commands in one batch. This way, a user can run one shell script instead of manually entering several commands individually. On macOS and Linux, shell script files have a .sh file extension (or no extension), while Windows uses the term batch file for shell scripts with a .bat file extension.

# Application A program that has a GUI and contains multiple related features. Excel and Firefox are examples of applications. Applications usually have several files that an installer program sets up on your computer (and that an uninstaller program can remove), rather than consisting of just a single executable file copied to a computer.

# App A common name for mobile phone and tablet applications, but the term can be used for desktop applications as well.

# Web app A program that runs on a web server, and which users interact with over the internet through a web browser.

# You’re welcome to nitpick about precise definitions; these explanations should merely give you a general sense of the terms’ usage. If you want to become familiar with more terminology, my book Beyond the Basic Stuff with Python (No Starch Press, 2020) has additional definitions in its “Programming Jargon” chapter.

#cd is used to go to the respective lovation that we want to 
#dir is used to list the files and folders there inside the location
#you can list all the executable files in the CWD by running dir *.exe

#all the running programs no matter what the language written in have a set of string variables called environment variables
#one of those is a path environment varible,which contains the list of folders the terminal checks when you enter the name of a program
#if you want to know the path of the directory then run echo %PATH% or simply path

#editing environment varibles
# To edit them, click the Start menu and then enter Edit environment variables for your account, which should open the Environment Variables window.
# Select Path from the User variable list on the top of the screen (not the System variable list on the bottom of the screen), click Edit, add the new folder name C:\Users\al\Scripts in the text field that appears with a semicolon separator, and click OK.
#if you want to find out which folder in the path environment varible a program is located in,then use (where fielname) command
#note that it can find the file on that particular location

#virtual environment
#seperate installations of python that have their own set of installed third-party packages is called a virtual environment.
#To create a virtual environment, cd to your Scripts folder and run python –m venv .venv (using python3 on macOS and Linux):
#Activation changes the PATH environment variable so that python or python3 runs the Python interpreter inside the .venv folder instead of the original one
#To deactivate the virtual environment, run deactivate.bat (on Windows) 

#installing python packages with pip
#python comes with command line package manager program called pip(recursive acronym for pip installs package)
#in python a package is a collection of python code made available on PyPi
#o install a package from PyPI, enter the following into the terminal:
#to install a package from PyPi –m pip install package_name
#To list all the packages you have installed along with their version numbers, run python –m pip list:

#for checking whether a particular module is there or not
# try:
#     import nonexistentModule
# except ModuleNotFoundError:
#     print('This code runs if nonexistentModule was not found.')
# Colorful Text with Bext
# You can print colorful text using the third-party Bext package built on top of Jonathan Hartley’s Colorama package. Install Bext with pip by following the instructions in Appendix A. Bext only works in programs run from a terminal window, and not from Mu or most other code editors. To have print() produce colorful text, call the fg() and bg() functions to change the (foreground) text color or the background color with a string argument such as 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'purple', 'cyan', or 'white'. You can also pass 'reset' to change the color back to the terminal window’s default color. For example, enter the following into the interactive shell:

# >>> import bext
# >>> bext.fg('red')
# >>> print('This text is red.')
# This text is red.
# >>> bext.bg('blue')
# >>> print('Red text on blue background is an ugly color scheme.')
# Red text on blue background is an ugly color scheme.
# >>> bext.fg('reset')
# >>> bext.bg('reset')
# >>> print('The text is normal again. Ah, much better.')
# The text is normal again. Ah, much better.
#Terminal clearing
