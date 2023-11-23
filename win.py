import win32api, win32gui, win32con, pywintypes
import time


# def get_windows():
#     hwndls = []
#     win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hwndls)
#     for i in hwndls:
#         print(win32gui.GetWindowText(i))


# win.py - interesting testing - Visual Studio Code
# get_windows()

# hwnd = win32gui.FindWindow(None, "Roblox")
# hwnd = win32gui.FindWindowEx(hwnd, None, None, None)
# win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x45, 0)
# time.sleep(0.15)
# win32gui.SendMessage(hwnd, win32con.WM_KEYUP, 0x45, 0)
# time.sleep(4)
# win32api.PostMessage(hwnd, win32con.WM_CHAR, 0x45, 0)