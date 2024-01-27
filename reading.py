"""Модуль представляет из себя описание логики всопроизведения последовательности кликов"""
from pynput.mouse import Button, Controller
from pynput import keyboard
from datetime import datetime
import time, json


def play_it(data, loop_status):
    mouse = Controller()
    previous_time = 0
    with open('mouse_button.txt') as g:
        mouse_button = g.read()

    with open('stop_button.txt') as f:
        stop_button = f.read()

    def on_release(key):
        if key.char == stop_button.lower():
            k_listener.stop()
            return False

    k_listener = keyboard.Listener(on_release=on_release)
    k_listener.start()

    if loop_status:
        while True:
            if k_listener.is_alive():
                for date, position in data.items():
                    if k_listener.is_alive():
                        date = datetime.strptime(date, "%m/%d/%Y, %H:%M:%S.%f")

                        if previous_time != 0 and previous_time < date:
                            time.sleep((date - previous_time).total_seconds())
                        mouse.position = position
                        mouse.press(Button[mouse_button])
                        mouse.release(Button[mouse_button])
                        previous_time = date
                    else:
                        break
            else:
                break
    else:
        for date, position in data.items():
            if k_listener.is_alive():
                date = datetime.strptime(date, "%m/%d/%Y, %H:%M:%S.%f")

                if previous_time != 0:
                    time.sleep((date - previous_time).total_seconds())
                mouse.position = position
                mouse.press(Button[mouse_button])
                mouse.release(Button[mouse_button])
                previous_time = date
            else:
                break




def opening(path, loop_status):
    with open(f'{path}', 'r') as f:
        data = json.load(f)
        play_it(data, loop_status)
