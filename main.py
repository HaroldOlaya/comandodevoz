import requests
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import socket

def clima():
    # Definir la URL de la API y la clave de API
    url = 'https://api.tomorrow.io/v4/timelines'
    api_key = 'bSZp300M1YBDkZoVryBmlBo8Sq6gmZxI'

    # Latitud y longitud de Bogotá, Colombia
    latitud = '4.6097'
    longitud = '-74.0817'

    # Definir los parámetros de la solicitud
    params = {
        'location': f'{latitud},{longitud}',  # Latitud y longitud de Bogotá
        'fields': 'temperature',  # Solicitar solo la temperatura
        'timesteps': '1h',  # Paso de tiempo de 1 hora
        'units': 'metric',  # Unidades métricas (grados Celsius)
        'apikey': api_key
    }

    # Realizar la solicitud GET a la API
    respuesta = requests.get(url, params=params)

    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        datos_clima = respuesta.json()

        # Extraer la temperatura actual
        temperatura_actual = datos_clima['data']['timelines'][0]['intervals'][0]['values']['temperature']

        # Imprimir la temperatura actual
        climaBogota=(f'Temperatura actual en Bogotá: {temperatura_actual}°C')
        return climaBogota
    else:
        return ('Error al obtener la temperatura actual del clima en Bogotá')
def tiempo():
    pregunta = "Necesitas hora o fecha"
    # respuesta en voz alta
    text_to_speech.say(pregunta)
    text_to_speech.runAndWait()
    with sr.Microphone() as source:
        print("Hora o Fecha")
        audio = recognizer.listen(source)
    # Reconoce el discurso utilizando el motor de reconocimiento de voz
    text = recognizer.recognize_google(audio, language="es-ES")
    print(f"Texto reconocido: {text}")
    # URL para obtener la hora actual en Bogotá
    url = 'https://worldtimeapi.org/api/timezone/America/Bogota'

    # Realizar la solicitud GET a la API
    respuesta = requests.get(url)

    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        datos_hora = respuesta.json()

        # Extraer y mostrar la hora actual
        hora_actual = datos_hora['datetime']
        # Cadena de fecha y hora
        cadena_fecha_hora = hora_actual

        # Convertir la cadena a un objeto datetime
        fecha_hora_objeto = datetime.fromisoformat(cadena_fecha_hora)

        # Extraer la fecha y la hora por separado
        fecha = fecha_hora_objeto.date()
        hora = fecha_hora_objeto.time()
        if text=="hora" or text == "Hora":
            hora_str = str(hora)
            partes_hora = hora_str.split(':')
            return (f'Son las: {partes_hora[0]},con {partes_hora[1]} minutos y {partes_hora[2][:2]} segundos')
        elif text=="fecha" or text =="Fecha":
            return(f'Fecha: {fecha}')
    else:
        return('Error al obtener la hora actual en Bogotá')
def enviar(valor):
    client_socket.send((valor).encode())

esp32_ip = "192.168.1.44"
esp32_port = 80
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((esp32_ip, esp32_port))
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()
iniciar=True

while iniciar:
    try:
        # Captura audio del micrófono
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = recognizer.listen(source)
        # Reconoce el discurso utilizando el motor de reconocimiento de voz
        text = recognizer.recognize_google(audio, language="es-ES")
        print(f"Texto reconocido: {text}")
        if text[:7]== "Viernes" or text[:7]=="viernes":
            respuesta="Señor"
            #respuesta en voz alta
            text_to_speech.say(respuesta)
            text_to_speech.runAndWait()
            while True:
                with sr.Microphone() as source:
                    print("cuenteme...")
                    audio = recognizer.listen(source)
                    # Reconoce el discurso utilizando el motor de reconocimiento de voz
                    text = recognizer.recognize_google(audio, language="es-ES")
                    print(f"Texto reconocido: {text}")
                    if text == "salir":
                        respuesta = "Fue un placer señor stark"
                        # respuesta en voz alta
                        text_to_speech.say(respuesta)
                        text_to_speech.runAndWait()
                        break
                    elif text == "clima" or text=="Clima":
                        climaBogota=clima()
                        text_to_speech.say(climaBogota)
                        text_to_speech.runAndWait()
                    elif text== "Tiempo" or text=="tiempo":
                        tiempoActual = tiempo()
                        text_to_speech.say(tiempoActual)
                        text_to_speech.runAndWait()
                    elif text=="Encender luz":
                        despedir = "encendiendo luz"
                        text_to_speech.say(despedir)
                        text_to_speech.runAndWait()
                        for i in range(10):
                            enviar("a")
                        print("encendiendo luz")
                    elif text == "Apagar luz":
                        despedir = "apagando luz"
                        text_to_speech.say(despedir)
                        text_to_speech.runAndWait()
                        for i in range(10):
                            enviar("b")
                        print("Apagando luz")
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"Error en la solicitud: {e}")

