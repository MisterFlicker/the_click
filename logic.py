"""Модуль представляет из себя описание логики записи последовательности кликов мышки и ее остановки по нажатию нужного символа с клавиатуры"""
from pynput import mouse, keyboard
from datetime import datetime
import json

sequence = {}
new_file = open(f'{datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}.txt', "w")
with open('stop_button.txt') as g:
    stop_button = g.read()


def on_release(key):
    if key.char == stop_button.lower():
        json.dump(sequence, new_file)
        new_file.close()
        m_listener.stop()
        return False


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    print(datetime.now())
    sequence[datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f")[:-3]] = (x, y)


with mouse.Listener(on_click=on_click) as m_listener, \
      keyboard.Listener(on_release=on_release) as k_listener:
    m_listener.join()
    k_listener.join()
