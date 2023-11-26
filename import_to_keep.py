import pyautogui
import pyperclip
import os
from os.path import isfile, dirname, join
import time
from pathlib import Path

# get the start time
st = time.time()

notes_path = os.path.dirname(__file__) + "//notes"

#read file logic
for filename in os.listdir(notes_path):
    with open(notes_path + "//" + filename, "r") as open_file:
        #click mouse on "take a note"
        pyautogui.click(574, 214)

        title=open_file.readline()
        #set the title correctly
        pyperclip.copy(title)
        pyautogui.click(574, 214)
        pyautogui.hotkey("ctrl", "v")

        #note section
        #breaks when title/first line is long, use "tab" next time.
        pyautogui.click(339, 297)
        
        #14 sec vs 116 sec on previous readline ver

        #find a way to ignore all lines until first char.
        notes=open_file.read()
        pyperclip.copy(notes)
        pyautogui.hotkey("home")
        pyautogui.hotkey("ctrl", "v")
        
        #ends the note
        pyautogui.press("esc")
        open_file.close()


# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')