from src.gui.window import Gui

def test_backend():
    assert test_increment_encounter()
    assert test_increment_then_decrement_encounter()
    assert test_decrement_encounter_past_zero()
    assert test_increment_by_five()
    assert test_decrement_by_five()

def test_increment_encounter() -> bool:
    gui = Gui()
    try:
        assert gui != None
        assert gui.title != None
        assert gui.windowWidth != None
        assert gui.windowHeight != None
        assert gui.count != None
        assert gui.countVar.get() != None
        countBefore = gui.countVar.get()
        gui.incrementEncounters()
        countAfter = gui.countVar.get()
        assert countBefore < countAfter
    except:
        print("Error: Incrementing by 1 failed.")
        return False
    print("==Passed==")
    return True

def test_increment_then_decrement_encounter() -> bool:
    gui = Gui()
    try:
        assert gui != None
        assert gui.title != None
        assert gui.windowWidth != None
        assert gui.windowHeight != None
        assert gui.count != None
        assert gui.countVar.get() != None
        countBefore = gui.countVar.get()
        gui.incrementEncounters()
        countAfter = gui.countVar.get()
        assert countBefore < countAfter
        assert countBefore == 0
        assert countAfter == 1
        countBefore = gui.countVar.get()
        gui.decrementEncounters()
        countAfter = gui.countVar.get()
        assert countBefore > countAfter
        assert countBefore == 1
        assert countAfter == 0
    except Exception as e:
        print("Error: Decrementing by 1 after incrementing by 1 failed.")
        return False
    print("==Passed==")
    return True

def test_decrement_encounter_past_zero():
    gui = Gui()
    try:
        assert gui != None
        assert gui.title != None
        assert gui.windowWidth != None
        assert gui.windowHeight != None
        assert gui.count != None
        assert gui.countVar.get() != None
        countBefore = gui.countVar.get()
        gui.decrementEncounters()
        countAfter = gui.countVar.get()
        assert countBefore == countAfter
        assert countBefore == 0
        assert countAfter == 0
    except Exception as e:
        print("Error: Decrementing by 1 past zero failed.")
        return False
    print("==Passed==")
    return True

def test_increment_by_five():
    gui = Gui()
    try:
        assert gui != None
        assert gui.title != None
        assert gui.windowWidth != None
        assert gui.windowHeight != None
        assert gui.count != None
        assert gui.countVar.get() != None
        countBefore = gui.countVar.get()
        gui.incrementEncounters(5)
        countAfter = gui.countVar.get()
        assert countBefore < countAfter
        assert countBefore == 0 
        assert countAfter == 5
    except Exception as e:
        print("Error: Incrementing by 5 failed.")
        return False
    print("==Passed==")
    return True

def test_decrement_by_five():
    gui = Gui()
    try:
        assert gui != None
        assert gui.title != None
        assert gui.windowWidth != None
        assert gui.windowHeight != None
        assert gui.count != None
        assert gui.countVar.get() != None
        gui.incrementEncounters(5)
        assert gui.countVar.get() == 5
        countBefore = gui.countVar.get()
        gui.decrementEncounters(5)
        countAfter = gui.countVar.get()
        assert countBefore > countAfter
        assert countBefore == 5
        assert countAfter == 0
    except Exception as e:
        print("Error: Decrementing by 5 after incrementing by 5 failed.")
        return False
    print("==Passed==")
    return True

def test_preprocess():
    pass

if __name__ == "__main__":
    print("--Testing backend--")
    test_backend()
