start: #запустить программу
	python interface.py

install: #установить зависимости
	sudo apt update
	sudo apt install python3
	pip install pynput setuptools PySimpleGui tk
