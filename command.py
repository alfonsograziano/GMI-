try:
    import win32api, win32con
    print("Windowsw libraries imported")
except ImportError:
    pass

try:
    import Xlib
    import Xlib.display
    print("Linux libraries imported")
except ImportError:
    pass

import platform

class Linux():
    def __init__(self):
        self.d = Xlib.display.Display()
        self.root = self.d.screen().root

    def moveCursor(self,x,y):
        desktop = self.root.get_geometry()
        if desktop.wight <= x and desktop.height <= y:
            self.root.warp_pointer(300, 300)
            self.displayd.sync()

    def getCursor(self):
        return [self.root.query_pointer()._data["root_x"],self.root.query_pointer()._data["root_x"]]


class Windows():
    def moveCursor(self,x,y):
        if x <= win32api.GetSystemMetrics(0) and y <= win32api.GetSystemMetrics(1):
            win32api.SetCursorPos((x, y))

    def getCursor(self):
        x, y = win32api.GetCursorPos()
        return [x,y]

class Osx():
    def moveCursor(self, x, y):
        pass

class Plattform():
    def __init__(self):
        os = platform.system()
        if os == "Linux":
            self.system = Linux()
            print("System recognized: " + os)
        elif os == "Windows":
            self.system = Windows()
            print("System recognized: " + os)
        elif os == "Osx":
            self.system = Osx()
            print("System recognized: "+ os)
        else:
            print("System not recognized")

    def getCursor(self):
        return self.system.getCursor()

    def moveCursor(self,x,y):
        self.system.moveCursor(x,y)