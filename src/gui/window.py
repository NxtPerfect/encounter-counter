import tkinter as tk
from tkinter import ttk

class Gui(tk.Tk):
    window: tk.Tk
    window_width: int
    window_height: int
    count: int

    def __init__(self, width:int=200, height:int=400, count:int=0):
        self.window = tk.Tk()
        self.window.title("Encounter Counter")

        self.window_width = width
        self.window_height = height
        self.count = count

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        center_x = int(screen_width/2 - self.window_width/2)
        center_y = int(screen_height/2 - self.window_height/2)

        self.window.minsize(300, 150)
        self.window.maxsize(1920, 1080)
        self.window.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=10)

        # self.topMenu = ttk.Frame();
        self.stats = ttk.Button(self.window, width="", text="Stats")
        self.stats.grid(column=0, row=0, sticky='nw')
        self.settings = ttk.Button(self.window, width="", text="Settings")
        self.settings.grid(column=1, row=0, sticky='nw')

        self.countLabel = ttk.Label(self.window, text=f'{count:,}')
        self.countLabel.grid(row=1, sticky='nsew')

        # Check if settings icon works
        try:
            self.window.iconbitmap('assets/icon.ico')
        except:
            photo = tk.Image("photo", file='assets/icon.png')
            self.window.wm_iconphoto(True, photo)
            self.window.tk.call('wm','iconphoto',self.window._w,photo)

        # Transparency
        self.window.attributes('-alpha', 0.9)
        # Stay on top of other windows
        self.window.attributes('-topmost', 1)

    def show(self):
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        finally:
            self.window.mainloop()
