import PySimpleGUI as sg

WINDOW_FONT_SIZE = 20
WINDOW_FONT = "Montserrat Light"
BUTTON_SIZE = (17, 3)


def build():
    """Es la pantalla que va a mostrar los botones para procesar los datos
    """
    layout = [
        [
            sg.Text(f"Datos Procesables",
                    font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))
        ],
        [
            sg.Button('Los 10 paises con más gasto militar',
                      key="-BTN1-",
                      size=BUTTON_SIZE,
                      font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))
        ],
        [
            sg.Button('Los lugares de los 10 accidentes áreos más fatales',
                      key="-BTN2-",
                      size=BUTTON_SIZE,
                      font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))
        ],
    ]

    sg.theme()
    return sg.Window("Menu",
                     layout,
                     finalize="true",
                     element_justification='center',
                     margins=(10, 10))
