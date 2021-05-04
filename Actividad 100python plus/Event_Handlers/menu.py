import PySimpleGUI
from Event_Handlers import analisys


def button1(event):
    """Se encarga de manejar el evento del botón 1
    """
    if event == "-BTN1-":
        analisys.start1()


def button2(event):
    """Se encanga de manejar el evento del botón 2
    """
    if event == "-BTN2-":
        analisys.start2()