import tkinter as tk
from tkinter import ttk

from src.constants import SRC_ROOT_DIR

PNG_ICON_PATH = SRC_ROOT_DIR + "/../assets/icon.png"
ICO_ICON_PATH = SRC_ROOT_DIR + "/../assets/icon.ico"

class Gui(tk.Tk):
    window: tk.Tk
    windowWidth: int
    windowHeight: int
    count: int
    countVar: tk.IntVar

    def __init__(self, width:int = 400, height:int = 200, count:int = 0):
        self.window = tk.Tk()
        self.window.title("Encounter Counter")

        self.window.bind("<KeyRelease>", self.handleKeys)

        self.windowWidth = width
        self.windowHeight = height
        self.count = count

        self.setWindowDimensionsAndCenter()

        self.setGrid()
        self.setTopMenu()
        self.setCountLabel(count)

        self.setIcon()

        # Transparency
        self.window.attributes('-alpha', 0.9)
        # Stay on top of other windows
        self.window.attributes('-topmost', 1)

    def setWindowDimensionsAndCenter(self):
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()

        centerX = int(screenWidth/2 - self.windowWidth/2)
        centerY = int(screenHeight/2 - self.windowHeight/2)

        self.window.minsize(300, 150)
        self.window.maxsize(screenWidth, screenHeight)
        self.window.geometry(f'{self.windowWidth}x{self.windowHeight}+{centerX}+{centerY}')

    def setGrid(self):
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=10)

    def setTopMenu(self):
        self.stats = ttk.Button(self.window, width="", text="Stats")
        self.stats.grid(column=0, row=0, sticky='nw')
        self.settings = ttk.Button(self.window, width="", text="Settings")
        self.settings.grid(column=1, row=0, sticky='nw')

    def setCountLabel(self, count):
        self.countVar = tk.IntVar()
        self.countVar.set(count)
        self.countLabel = ttk.Label(self.window, textvariable=self.countVar, font=("Ubuntu", 40))
        self.countLabel.grid(column=1, row=1, sticky='nsw')

    def setIcon(self):
        # Check if settings icon works
        try:
            self.window.iconbitmap(ICO_ICON_PATH)
        except:
            photo = tk.Image("photo", file=PNG_ICON_PATH, master=self.window)
            self.window.wm_iconphoto(True, photo)
            self.window.tk.call('wm','iconphoto',self.window._w,photo)

    def handleKeys(self, event):
        print(event.keysym)
        
        if event.keysym == "equal":
            self.incrementEncounters()
        elif event.keysym == "minus":
            self.decrementEncounters()
        print(self.countVar.get())

    def incrementEncounters(self, count:int = 1):
        curValue = self.countVar.get()
        self.countVar.set(curValue + count)

    def decrementEncounters(self, count:int = 1):
        curValue = self.countVar.get()
        self.countVar.set(curValue - count if curValue > 0 else 0)


    def show(self):
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        finally:
            self.window.mainloop()
