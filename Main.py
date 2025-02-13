import serial
from dearpygui import dearpygui as dpg
import threading

dataT_list = []  # Lista per la temperatura
dataU_list = []  # Lista per l'umidità
time_list = []  # Lista per il tempo (numero di letture)
count = 0  # Contatore per le letture


def funzione_thread():
    global count
    ser = serial.Serial("COM14")

    while True:
        data = ser.readline().decode("utf-8")
        datasplit = data.split(';')
        dataT = float(datasplit[0])
        dataU = float(datasplit[1])

        print(dataT, '°C')
        print(dataU, '%')

        dpg.set_value("Temp", f"{dataT} °C")
        dpg.set_value("Umi", f"{dataU} %")

        # Aggiorna i dati della lista
        dataT_list.append(dataT)
        dataU_list.append(dataU)
        time_list.append(count)
        count += 1

        # Mantieni solo gli ultimi 50 valori per evitare problemi di performance
        if len(time_list) > 50:
            dataT_list.pop(0)
            dataU_list.pop(0)
            time_list.pop(0)

        # Aggiorna il grafico
        dpg.set_value("temp_plot", [time_list, dataT_list])
        dpg.set_value("umi_plot", [time_list, dataU_list])


# Creazione del thread.
thread = threading.Thread(target=funzione_thread, daemon=True)
thread.start()

dpg.create_context()

dpg.create_viewport(title="Bomboclat", width=600, height=500)
with dpg.window(label="Dati in Tempo Reale", width=600, height=500):
    dpg.add_text(tag="Temp")
    dpg.add_text(tag="Umi")

    # Creazione del grafico
    with dpg.plot(label="Andamento Temperatura e Umidità", height=300, width=580):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="Letture", tag="x_axis")
        dpg.add_plot_axis(dpg.mvYAxis, label="Valori", tag="y_axis")
        dpg.add_line_series([], [], label="Temperatura", parent="y_axis", tag="temp_plot")
        dpg.add_line_series([], [], label="Umidità", parent="y_axis", tag="umi_plot")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
