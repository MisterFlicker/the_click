"""Модуль представляет из себя описание логики всопроизведения последовательности кликов"""
from pynput.mouse import Button, Controller
from pynput import keyboard
from datetime import datetime
import time, json


def play_it(data):
    mouse = Controller()
    previous_time = 0
    x = 0
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

    for date, position in data.items():
        if k_listener.is_alive():
            if x+1 == len(data):
                break
            date = datetime.strptime(date, "%m/%d/%Y, %H:%M:%S.%f")

            if previous_time != 0:
                time.sleep((date - previous_time).total_seconds())
            mouse.position = position
            mouse.press(Button[mouse_button])
            mouse.release(Button[mouse_button])
            previous_time = date
            x += 1
        else:
            break


def opening(path):
    with open(f'{path}', 'r') as f:
        data = json.load(f)
        play_it(data)
