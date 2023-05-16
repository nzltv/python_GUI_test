from pywinauto.application import Application
from time import sleep
import sys

try:
    app = Application().Start(cmd_line=u'"C:\\Program Files\\Notepad++\\notepad++.exe" ')
    notepad = app[u'Notepad++']
    notepad.Wait('ready')
    systabcontrol = notepad.Tab
    systabcontrol.Select(u'new 1')
    panel = notepad.Scintilla
    panel.set_focus()
    panel.type_keys('asd1222')
    sleep(3)
    notepad.set_focus()
    notepad.menu_select('File->SaveAs...')
    sleep(3)
    Sub = Application().Connect(title=u'Сохранение', class_name='#32770')
    #Sub.Dialog.print_control_identifiers()
    Sub.Dialog.Сохранить.click_input()
    sleep(10)
    app.Kill_()
except Exception as e:
    with open("error_code.log", 'w') as file:
        file.write(str(e))