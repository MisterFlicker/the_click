"""Модуль представляет из себя описание интерфейса приложения"""
import PySimpleGUI as sg
from tkinter import filedialog
from reading import opening
from util import change_stop_button, change_m_button, valid
import os

os.environ["DISPLAY"] = ":0"

choices = ('left', 'middle', 'right')

with open('stop_button.txt') as f:
    stop_button = f.read()

with open('mouse_button.txt') as h:
    mouse_button = h.read()

menu_def = [['Settings'],
            ['Help', ['Version', 'About']]]

sg.theme('Light Blue 2')

layout = [[sg.Menu(menu_def, )],
          [sg.Button('Record clicks')],
          [sg.Menu(menu_def, )],
          [sg.Text('Press'), sg.Text(stop_button.upper(), key='-STOP-'), sg.Text('to stop record or play back of clicks')],
          [sg.Text('')],
          [sg.Button('Play recorded clicks')],
          [sg.Text('')],
          [sg.Button('Change "STOP" Button')],
          [sg.Text('')],
          [sg.Text(f'Current mouse button: {mouse_button}', key='-MOUSE-')],
          [sg.Text('Choose mouse button to play recorded clicks:')],
          [sg.Listbox(choices, size=(10, len(choices)), key='-BUTTON-', enable_events=True)],
          [sg.Checkbox('Loop the playing sequnece', key='-INF-')]]


window = sg.Window('The Click', layout, auto_size_text=True, auto_size_buttons=True)

while True:

    event, values = window.read()

    if event == 'Version':
        sg.popup_scrolled(sg.get_versions())

    if event == 'About':
        sg.popup('About "The Click"', 'Version 1.0', 'Author: Mister_Flicker')

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Record clicks':
        with open('logic.py') as f:
            exec(f.read())

    if event == 'Play recorded clicks':
        filepath = filedialog.askopenfilename()
        if filepath:
            opening(filepath, values['-INF-'])
        else:
            continue

    if event == 'Change "STOP" Button':
        layout2 = [[sg.Input(window['-STOP-'].get(), key='-IN-')],
                   [sg.Text('', key='-INFO-')],
                   [sg.Button('Ok')]]
        window2 = sg.Window('Choose new button', layout2)

        while True:
            event2, values2 = window2.read()
            print(event2, values2)

            if event2 == sg.WIN_CLOSED:
                break

            if event2 == 'Ok':
                if valid(values2['-IN-']):
                    window['-STOP-'].update(values2['-IN-'].upper())
                    window2['-IN-'].update(values2['-IN-'].upper())
                    change_stop_button(values2['-IN-'])
                    break

                else:
                    window2['-INFO-'].update("Please don't enter special symbols or more than 1 symbol.\nYou can enter only common symbols or figures.")
        window2.close()

    if values['-BUTTON-']:
        change_m_button(values['-BUTTON-'][0])
        window['-MOUSE-'].update(f'Current mouse button: {(values["-BUTTON-"][0])}')

window.close()