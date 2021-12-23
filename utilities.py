"""
Version 3.0.1

## UPGRADES
++ Upgraded TIMER function to a decorator function
++ Upgraded the LOGFILE to a Class with 2 functions


## ADDITIONS
++ Added ABS_PATH function to build absolute paths for files
++ Added documentation entries for all functions
++ Added EXECUTE function to launch/open a file
"""


# ---------- Importing standard libraries
import time
from datetime import datetime
import os
import sys

# ---------- Importing other libraries
from colored import fg, bg, attr

# GET FOLDER
def curr_folder():
    """
    Returns current folder. Usefull for concatenating with file names to build absolute file path.
    """
    foldername = os.path.dirname(os.path.realpath(__file__))
    return foldername

def abs_path(file):
    """
    Returns absolute file path (current folder + relative file name).
    """
    foldername = os.path.dirname(os.path.realpath(__file__))
    filename = "\\" + file
    abs_path = foldername + filename
    return abs_path

# EXECUTE / OPEN file/app
def execute(path):
    os.startfile(path)

# GET USERNAME
def login_name():
    """
    Returns the OS logged in user.
    """
    return os.getlogin()

# LOG START
class LogFile:
    """
    Creates a logfile in the working directory and writes all the PRINT function output.
    Use "LogFile.start()" to start the log capture.
    Use "LogFile.close()" to close the log capture.
    """
    def start():
        """
        Opens the logfile and starts writing the PRINT outputs to it.
        """
        now = datetime.now()
        now = now.strftime("%Y/%m/%d %H:%M:%S")
        old_stdout = sys.stdout
        filename = "logfile.log"
        log_file = open( filename,"a+")
        sys.stdout = log_file
        print("\n---------------------------------------------------------------------------------------\n" + ":: LOG TIME - " + now +"\n---------------------------------------------------------------------------------------")
        return log_file
        
    def close():
        """
        Closes the logfile at the end of the script or session.
        """
        filename = "logfile.log"
        log_file = open( filename,"a+")
        sys.stdout
        log_file.close()

# START THE APP
def start_color(appname):
    """
    Formats a text with a specific color (BLUE).
    """
    reset = attr('reset')
    blue = fg('#0000FF')
    color = blue
    text = str(appname)
    print("_______________________________________________________________")
    print(color + "---------------------------------------------------------------\n:::: " + text + "\n---------------------------------------------------------------\n" + reset)
    

def start(appname):
    """
    Wraps some text into a few lines of spacers. Good when starting a script or a section of a script.
    """
    text = str(appname)
    print("_______________________________________________________________")
    print("---------------------------------------------------------------\n:::: " + text + "\n---------------------------------------------------------------\n")

# PROGRESS INDICATOR
def progress(perc, step):
    """
    Returns the % of completeness of a script.
    """
    if perc == 0:
        return "[__________] 00%  | "+ step
    if perc == 20:
        return "[::________] 20%  | "+ step
    if perc == 40:
        return "[::::______] 40%  | "+ step
    if perc == 60:
        return "[::::::____] 60%  | "+ step
    if perc == 80:
        return "[::::::::__] 80%  | "+ step
    if perc == 100:
        return color_text('green',"[::::::::::] 100% | "+ step)
    if perc == 69:
        return color_text('red',"[::ERROR!::] !!!! | "+ step)

# SECTION
def section_start(section):
    """
    Wrapper around a Section header name.
    """
    print("---------------------------------------------------------------\n" + ":::: " + section)

def section_end():
    """
    Adds a closing spacer line.
    """
    print("--------------------------------///----------------------------\n")

# ENTRY 
def entry(text):
    """
    Wrapper around a simple script text entry.
    """
    print(":: " + text)

# SEPARATOR
def separator_line():
    """
    Adds a simple spacer line.
    """
    print("---------------------------------------------------------------")

def separator_thick():
    """
    Adds a thick spacer line.
    """
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

# COPYRIGHT
def copyright():
    """
    Adds a copyright entry.
    """
    print("---------------------------------------------------------------")
    print(":::: COPYRIGHT (c) Costin Nadolu ")
    print("---------------------------------------------------------------")

# TIMER (decorator)
def timer(func):
    """
    Returns the time taken for a function to run.
    Can be used only to time function execution time.
    Use it as a decorator before the function definition "@timer".
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        time_sec = time.time() - start_time
        time_min = time_sec / 60
        time_hour = time_min / 60
        print("-------------------------------")
        print(":: TIME taken")
        print(":: %s sec" % round(time_sec,3), "|or| %s min" % round(time_min,3), "|or| %s hours" % round(time_hour,3))
        print("-------------------------------")
        return result
    return wrapper
    
# COLORED OUTPUT
# color_text('red', "some text ...")
# color_text('green', "some text ...")
# color_text('blue', "some text ...")
def color_text(color, value):
    """
    Formats the text output to screen in red / green / blue font.
    """
    reset = attr('reset')
    red = fg('#FF0000')
    green = fg('#008000')
    blue = fg('#0000FF')
   
    if color == 'red':
        color = red
    elif color == 'green':
        color = green
    elif color == 'blue':
        color = blue
    print(color + str(value) + reset)



# color_bg('red', "some text ...")
# color_bg('green', "some text ...")
# color_bg('blue', "some text ...")
def color_bg(color, value):
    """
    Formats the text output to screen in with red / green / blue background.
    """
    reset = attr('reset')
    red = bg('#FF0000')
    green = bg('#008000')
    blue = bg('#0000FF')
   
    if color == 'red':
        color = red
    elif color == 'green':
        color = green
    elif color == 'blue':
        color = blue
    print(color + str(value) + reset)
     