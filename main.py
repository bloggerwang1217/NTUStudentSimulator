import tkinter as tk
import sys


def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]


window = tk.Tk()
window.geometry("1280x720")
window.resizable(0, 0)
window.title("為美好的台大生活獻上祝福")

import system.beginning as bg

data = {}
bg.start_game(window, data)

window.mainloop()