from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
notepadapp = Application(backend="uia").start("notepad.exe")
#notepadapp = Application(backend="uia").connect(path=r"C:\Windows\system32\notepad.exe")
notepad_window = notepadapp.window(title='Untitled - Notepad')
dialog = notepadapp.window(title='Untitled - Notepad')
#Menu item
fmenu = dialog.menu_select('Format->Font...')
fdlg = notepadapp.Font
ftype = fdlg.ComboBox
ftype.select('Trebuchet MS')
ftype = fdlg.ComboBox2
ftype.select('Bold Italic')
fsize = fdlg.ComboBox3
fsize.type_keys('28')
fdlg.OK.click() 
#Mouse
notepad_window["Close"].rectangle()
dialog.set_focus()
mouse.click(coords=(1608, 267, 1655, 297))
#keyboard
dialog.type_keys('Hello{SPACE}from{SPACE}PYWINAUTO')
dialog.type_keys('{ENTER}Lets test with keyboard')
dialog.type_keys('{ENTER}0123456789')
dialog.type_keys('{ENTER}ABCDEFGHIJKLMNOPQRSTUVWXYZ')
dialog.type_keys('{ENTER}abcdefghijklmnopqrstuvwxyz')
dialog.type_keys('{ENTER}`~!@#$%^&*()-_=+')
dialog.type_keys('{ENTER}[]{{}{}}\\|;:\'\",<.>/?')