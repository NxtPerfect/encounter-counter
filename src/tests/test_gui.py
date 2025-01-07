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

def test_gui():
    tests = [test_window_initializes]
    passed: int = 0
    for test in tests:
        try:
            test()
        except:
            continue
        else:
            passed += 1
    print(f"Passed {passed} out of {len(tests)}")
    test_window_initializes()

if __name__ == "__main__":
    print("Testing gui")
    test_gui()
