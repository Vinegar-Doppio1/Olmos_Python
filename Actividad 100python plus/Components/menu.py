import PySimpleGUI as sg
from Windows.menu import build
from Event_Handlers.menu import *


def loop(menu_window):
    """Controla los posibles eventos de la pantalla principal
    """
    while True:
        event, values = menu_window.read()
        if event == sg.WIN_CLOSED:
            break
        button1(event)
        button2(event)


def start():
    """Genera la pantalla y se la manda al loop
    """
    menu_window = build()
    loop(menu_window)

    menu_window.close()