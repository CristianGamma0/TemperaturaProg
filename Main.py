import serial
from dearpygui import dearpygui as dpg
import threading


def funzione_thread():
    ser = serial.Serial("COM14")

    while True:
        data = ser.readline().decode("utf-8")
        datasplit = data.split(';')
        dataT = float(datasplit[0])
        dataU = float(datasplit[1])

        print(dataT, '°C')
        print(dataU, '%')
        dpg.set_value("Temp", dataT)
        dpg.set_value("Umi", dataU)


# Creazione del thread
thread = threading.Thread(target=funzione_thread)

# Avvio del thread
thread.start()

dpg.create_context()

dpg.create_viewport(title="Bomboclat", width=400, height=300)
with dpg.window(label="Temperatura"):
    with dpg.group(horizontal=True):
        dpg.add_text(tag="Temp")
        dpg.add_text('°C')
    with dpg.group(horizontal=True):
        dpg.add_text(tag="Umi")
        dpg.add_text('%')

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()
