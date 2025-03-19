# TemperaturaProg
# Termostato con Arduino

Il progetto **Termostato con Arduino** è un sistema di monitoraggio ambientale che utilizza una scheda Arduino per rilevare temperatura e umidità tramite un sensore DHT11. I dati vengono trasmessi in tempo reale a un’applicazione desktop sviluppata in Python con **Dear PyGui**, che li visualizza graficamente e li salva in un file JSON per analisi future. Inoltre, il sistema gestisce l'accensione di un LED (indicatore) se la temperatura supera una soglia predefinita.

## Caratteristiche

- **Monitoraggio Ambientale:** Lettura in tempo reale di temperatura e umidità.
- **Visualizzazione Dati:** Interfaccia grafica che mostra i valori correnti e un grafico dell'andamento nel tempo.
- **Gestione LED:** Accensione del LED se la temperatura supera la soglia impostata.
- **Storico Dati:** Salvataggio periodico dei dati in un file JSON per ulteriori analisi.

## Requisiti

### Hardware
- **Arduino:** (es. Arduino Uno)
- **Sensore di Temperatura/Umidità:** DHT11
- **LED:** LED rosso (per indicare la temperatura oltre soglia)
- **Componenti Accessori:** Breadboard, cavi, resistenze

### Software
- **Arduino IDE:** Per scrivere e caricare lo sketch sulla scheda Arduino.
- **Python 3.x:** Per eseguire l'applicazione desktop.
- **Librerie Python:**
  - `pyserial`
  - `dearpygui`
  - `pytz`
  - `json` (inclusa nella libreria standard)

## Installazione e Setup

1. **Configurazione di Arduino:**
   - Segui lo schema hardware descritto nel file [Hardware.md](./Hardware) della documentazione.
   - Apri l'**Arduino IDE** e carica lo sketch Arduino contenuto nel file [Codice.md](./Codice) (sezione Codice Arduino). Questo codice:
     - Legge i dati dal sensore DHT11.
     - Invia i dati in formato "temperatura;umidità" via seriale.
     - Controlla il LED in base alla soglia di temperatura.

2. **Configurazione dell'Applicazione Python:**
   - Installa le librerie necessarie eseguendo:
     ```bash
     pip install pyserial dearpygui pytz
     ```
   - Verifica che la porta seriale configurata (es. "COM7") corrisponda a quella utilizzata dal tuo Arduino.
   - Avvia lo script Python per visualizzare la GUI, che mostrerà i dati in tempo reale e aggiornerà il grafico mentre il file `Dati.json` viene aggiornato.

## Struttura del Progetto

Il repository include:
- **Sketch Arduino:** Codice per la lettura dei dati dal sensore e la gestione del LED.
- **Script Python:** Codice per la ricezione dei dati dalla porta seriale, aggiornamento della GUI e salvataggio dello storico in JSON.
- **Documentazione Wiki:** Divisa in più pagine per una consultazione dettagliata (Overview, Hardware, Software, Installazione, Codice, Project Management, FAQ).

Per ulteriori dettagli, consulta la [Wiki del progetto](./Wiki).

## Contributi

I contributi sono benvenuti! Consulta la pagina [Gestione del Progetto e Contributi](./ProjectManagement) per linee guida dettagliate.  
Per segnalare bug o proporre miglioramenti, utilizza le **Issue** del repository GitHub.

## Licenza

Questo progetto è distribuito sotto la [Licenza MIT](LICENSE).

## Contatti

Per ulteriori informazioni o domande, apri una **Issue** nel repository o contatta gli sviluppatori.

---

*Documentazione completa disponibile nella Wiki del progetto.*
