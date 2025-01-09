from PIL import ImageGrab

from src.constants import SRC_ROOT_DIR

def takeScreenshot():
    screenshot = ImageGrab.grab(bbox=(0, 0, 1920, 1080/2))
    # Process the screenshot, then close
    # screenshot.save(SRC_ROOT_DIR + "/../assets/screenshot.png")
    screenshot.close()
