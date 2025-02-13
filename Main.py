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


# Creazione del thread
thread = threading.Thread(target=funzione_thread)

# Avvio del thread
thread.start()


dpg.create_context()

with dpg.window(label="Temperatura"):
    dpg.add_text("sium")

dpg.create_viewport(title="Bomboclat", width=400, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()
