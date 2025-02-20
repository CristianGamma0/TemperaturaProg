import serial
from dearpygui import dearpygui as dpg
from datetime import datetime
import threading
import pytz  # Ensure proper timezone handling

# Set your local timezone (change "Europe/Rome" if needed)
local_timezone = pytz.timezone("Europe/Rome")

dataT_list = []  # Lista per la temperatura
dataU_list = []  # Lista per l'umidità
time_list = []  # Lista per i timestamp (asse x)


def funzione_thread():
    ser = serial.Serial("COM15")

    while True:
        data = ser.readline().decode("utf-8")
        datasplit = data.split(';')
        dataT = float(datasplit[0])
        dataU = float(datasplit[1])

        print(f"{dataT} °C")
        print(f"{dataU} %")

        dpg.set_value("Temp", f"{dataT} °C")
        dpg.set_value("Umi", f"{dataU} %")

        # Ottieni l'orario attuale come timestamp (secondi dall'epoch)
        current_time = datetime.now(local_timezone)
        # Add the offset (in seconds) to convert the UTC timestamp to local time
        timestamp = current_time.timestamp() + current_time.utcoffset().total_seconds()

        # Aggiorna le liste dei dati
        dataT_list.append(dataT)
        dataU_list.append(dataU)
        time_list.append(timestamp)

        # Mantieni solo gli ultimi 50 valori per evitare problemi di performance
        if len(time_list) > 50:
            dataT_list.pop(0)
            dataU_list.pop(0)
            time_list.pop(0)

        # Aggiorna il grafico: la serie ora usa time_list (numerico) che verrà formattato come orario
        dpg.set_value("temp_plot", [time_list, dataT_list])
        dpg.set_value("umi_plot", [time_list, dataU_list])


# Creazione ed esecuzione del thread in background
thread = threading.Thread(target=funzione_thread, daemon=True)
thread.start()

dpg.create_context()
dpg.create_viewport(title="Lettura sensore di temperatura", width=600, height=500)

with dpg.window(label="Dati in Tempo Reale", width=600, height=500):
    dpg.add_text(tag="Temp")
    dpg.add_text(tag="Umi")

    # Creazione del grafico
    with dpg.plot(label="Andamento Temperatura e Umidità", height=300, width=580):
        dpg.add_plot_legend()
        # Imposta l'asse x in modalità "tempo" in modo da formattare i timestamp in HH:MM:SS
        dpg.add_plot_axis(dpg.mvXAxis, label="Orario", tag="x_axis",auto_fit=True,time=True)
        dpg.add_plot_axis(dpg.mvYAxis, label="Valori", tag="y_axis")
        dpg.add_line_series([], [], label="Temperatura", parent="y_axis", tag="temp_plot")
        dpg.add_line_series([], [], label="Umidità", parent="y_axis", tag="umi_plot")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
