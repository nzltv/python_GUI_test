from pywinauto.application import Application
from time import sleep
import sys
import pyautogui
import os

try:
    app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\Notepad++\\notepad++.exe" ')
    print('step_1')
    notepad = app[u'Notepad++']
    notepad.wait('ready')
    print('step_2')
    systabcontrol = notepad.Tab
    #systabcontrol.select(u'new 1')
    panel = notepad.Scintilla
    panel.set_focus()
    print('step_3')
    panel.type_keys('asd1222')
    sleep(3)
    notepad.set_focus()
    notepad.menu_select('File->SaveAs...')
    print('step_4')
    sleep(3)
    Sub = Application().Connect(title=u'Сохранение', class_name='#32770')
    #Sub.Dialog.print_control_identifiers()
    Sub.Dialog.Сохранить.click_input()
    print('step_5')
    user = os.getlogin()
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'C:\Jenkins\screenshots\{user}.png')
    sleep(10)
    app.Kill_()
except Exception as e:
    with open("error_code.log", 'w') as file:
        file.write(str(e))
