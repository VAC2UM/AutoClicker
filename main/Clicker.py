import keyboard as key
import pyautogui as auto
import time

start_key = input('Введите клавишу запуска: ')
stop_key = input('Введите клавишу остановки: ')
pause_key = input('Введите клавишу паузы: ')
always_key = input('Введите клавишу для постоянного клика: ')
button_name = input('Какая кнопка мыши будет кликать? (right / left): ')
delay = float(input('Введите задержку между кликами в секундах (например, 0.01): '))


def cps():
    clicking = False
    while True:
        if key.is_pressed(start_key):
            clicking = True
        elif key.is_pressed(stop_key):
            break
        elif key.is_pressed(pause_key):
            clicking = False
        elif key.is_pressed(always_key):
            while not key.is_pressed(pause_key):
                auto.tripleClick(button=button_name)
                time.sleep(delay)
                if key.is_pressed(stop_key):
                    return

        if clicking:
            auto.tripleClick(button=button_name)
            time.sleep(delay)


cps()
