import keyboard as key
import pyautogui as auto

start_key = input('Введите клавишу запуска: ')
stop_key = input('Введите клавишу остановки: ')
pause_key = input('Введите клавишу паузы: ')
always_key = input('Введите клавишу для постоянного клика: ')
button_name = input('Какая кнопка мыши будет кликать? (right / left): ')


def cps1():
    while True:
        if key.is_pressed(start_key):
            auto.tripleClick(button=button_name)
        if key.is_pressed(stop_key):
            break
        if key.is_pressed(always_key):
            always_click()


def always_click():
    while True:
        auto.tripleClick(button=button_name)
        if key.is_pressed(pause_key):
            cps1()
        if key.is_pressed(stop_key):
            break


cps1()
