import tkinter as tk
from tkinter import StringVar, ttk

from src.constants import SRC_ROOT_DIR

PNG_ICON_PATH = SRC_ROOT_DIR + "/../assets/icon.png"
ICO_ICON_PATH = SRC_ROOT_DIR + "/../assets/icon.ico"

class Gui(tk.Tk):
    window: tk.Tk
    windowWidth: int
    windowHeight: int
    count: int
    countVar: tk.IntVar
    experimentalTextRecognition: tk.IntVar # 0 = false, 1 = true
    keySingle: tk.StringVar
    keyHordeOfThree: tk.StringVar
    keyHordeOfFive: tk.StringVar

    def __init__(self, width:int = 400, height:int = 200, count:int = 0) -> None:
        self.window = tk.Tk()
        self.window.title("Encounter Counter")

        self.window.bind("<KeyRelease>", self.handleKeys)

        self.windowWidth = width
        self.windowHeight = height
        self.count = count

        self.setWindowDimensionsAndCenter()

        self.setGrid()
        self.setTopMenu()
        self.setKeybinds()
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
        self.stats = ttk.Button(self.window, width="", text="Stats", command=self.showStats)
        self.stats.grid(column=0, row=0, sticky='n')
        self.settings = ttk.Button(self.window, width="", text="Settings", command=self.showSettings)
        self.settings.grid(column=1, row=0, sticky='n')
        self.exit = ttk.Button(self.window, width="", text="Exit", command=self.closeApp)
        self.exit.grid(column=2, row=0, sticky='n')

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

    def setKeybinds(self):
        # set default keybinds
        self.experimentalTextRecognition = tk.IntVar()
        self.experimentalTextRecognition.set(0)
        self.keySingle = tk.StringVar()
        self.keySingle.set("f")
        self.keyHordeOfThree = tk.StringVar()
        self.keyHordeOfThree.set("g")
        self.keyHordeOfFive = tk.StringVar()
        self.keyHordeOfFive.set("h")

    def handleKeys(self, event):
        print(event.keysym)

        if event.keysym == self.keySingle.get():
            self.incrementEncounters()
        elif event.keysym == "i":
            self.decrementEncounters()
        elif event.keysym == self.keyHordeOfThree.get():
            self.incrementEncounters(3)
        elif event.keysym == "o":
            self.decrementEncounters(3)
        elif event.keysym == self.keyHordeOfFive.get():
            self.incrementEncounters(5)
        elif event.keysym == "p":
            self.decrementEncounters(5)
        print(self.countVar.get())

    def incrementEncounters(self, count:int = 1):
        curValue = self.countVar.get()
        self.countVar.set(curValue + count)

    def decrementEncounters(self, count:int = 1):
        curValue = self.countVar.get()
        self.countVar.set(curValue - count if curValue - count >= 0 else 0)

    def closeApp(self):
        try:
            self.window.destroy()
        except Exception as e:
            print("Failed to close window")
            print(e)

    def showStats(self):
        pass

    def showSettings(self):
        newWindow = tk.Toplevel()
        newWindow.geometry(f"{self.windowWidth}x{self.windowHeight}")

        # labelExperimentalTextRecognition = ttk.Label(newWindow, text="Set experimental text recognition")
        # labelExperimentalTextRecognition.pack()
        #
        # checkboxExperimentalTextRecognition = ttk.Checkbutton(newWindow, variable=self.experimentalTextRecognition, text="Set experimental text recognition", onvalue=1, offvalue=0, width=20)
        # checkboxExperimentalTextRecognition.pack()

        singleEncounterKeyLabel = ttk.Label(newWindow, text="Single encounter key:")
        singleEncounterKeyLabel.pack()

        singleValidate = (self.register(self.getLastKeyForKeybind), "%P")

        singleEncounterEntry = ttk.Entry(newWindow, textvariable=self.keySingle, validate="key", validatecommand=singleValidate, width=200)
        singleEncounterEntry.pack()

        threeValidate = (self.register(self.getLastKeyForKeybind), "%P")

        threeEncounterKeyLabel = ttk.Label(newWindow, text="Triple encounter key:")
        threeEncounterKeyLabel.pack()

        threeEncounterEntry = ttk.Entry(newWindow, textvariable=self.keyHordeOfThree, validate="key", validatecommand=threeValidate, width=200)
        threeEncounterEntry.pack()

        fiveValidate = (self.register(self.getLastKeyForKeybind), "%P")

        fiveEncounterKeyLabel = ttk.Label(newWindow, text="Five encounters key:")
        fiveEncounterKeyLabel.pack()

        fiveEncounterEntry = ttk.Entry(newWindow, textvariable=self.keyHordeOfFive, validate="key", validatecommand=fiveValidate, width=200)
        fiveEncounterEntry.pack()

        newWindow.mainloop()

    def getLastKeyForKeybind(self, entryText):
        if (len(entryText.get()) > 0):
            entryText.set(entryText.get()[:-1])
            return True
        return False

    def show(self):
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        finally:
            self.window.mainloop()


if __name__ == "__main__":
    Gui().show()
