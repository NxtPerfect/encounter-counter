from src.gui.window import Gui


def test_window_initializes():
    gui = Gui()
    try:
        assert gui != None
        assert gui.title != None
        assert gui.window_width != None
        assert gui.window_height != None
        assert gui.count != None
    except:
        print("Error: Gui failed to initialize correctly.")
        return
    print("==Passed==")

def run():
    test_window_initializes()

if __name__ == "__main__":
    run()
