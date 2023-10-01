import requests
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import pyautogui


def responder(frase):
    text_to_speech.say(frase)
    text_to_speech.runAndWait()
def oir(opcion):
    with sr.Microphone() as source:
        print(opcion)
        audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language="es-ES")
    text = convertirMayus(text)
    textOido(text)
    return text
def musica():
    responder("Que desea hacer señor")
    parametro=oir("Que desea hacer señor: ")
    if parametro == "REPRODUCIR":
        responder("Nombre de la cancion")
        nombre=oir("Nombre de la cancion: ")
        responder("Nombre del compositor")
        cantante=oir("Nombre del compositor: ")
        busqueda_url = f'https://www.youtube.com/results?search_query={nombre+cantante}'
        webbrowser.open(busqueda_url)
        responder("Ya la tiene en pantalla señor")
    elif parametro == "CERRAR PESTAÑA":
        responder("cerrando pestaña")
        pyautogui.hotkey('ctrl', 'w')


def textOido(text):
    print(f"Texto reconocido: {text}")

def convertirMayus(texto):
    texto=texto.upper()
    return texto
def clima():
    url = 'https://api.tomorrow.io/v4/timelines'
    api_key = 'bSZp300M1YBDkZoVryBmlBo8Sq6gmZxI'
    latitud = '4.6097'
    longitud = '-74.0817'
    params = {
        'location': f'{latitud},{longitud}',  # Latitud y longitud de Bogotá
        'fields': 'temperature',  # Solicitar solo la temperatura
        'timesteps': '1h',  # Paso de tiempo de 1 hora
        'units': 'metric',  # Unidades métricas (grados Celsius)
        'apikey': api_key
    }
    respuesta = requests.get(url, params=params)
    if respuesta.status_code == 200:
        datos_clima = respuesta.json()
        temperatura_actual = datos_clima['data']['timelines'][0]['intervals'][0]['values']['temperature']
        climaBogota = (f'Temperatura actual en Bogotá: {temperatura_actual}°C')
        return climaBogota
    else:
        return ('Error al obtener la temperatura actual del clima en Bogotá')


def tiempo():
    responder('Necesitas hora o fecha')
    text=oir("Hora o Fecha")
    url = 'https://worldtimeapi.org/api/timezone/America/Bogota'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_hora = respuesta.json()
        hora_actual = datos_hora['datetime']
        cadena_fecha_hora = hora_actual
        fecha_hora_objeto = datetime.fromisoformat(cadena_fecha_hora)
        fecha = fecha_hora_objeto.date()
        hora = fecha_hora_objeto.time()
        if text == "HORA":
            hora_str = str(hora)
            partes_hora = hora_str.split(':')
            return (f'Son las: {partes_hora[0]}, con {partes_hora[1]} minutos y {partes_hora[2][:2]} segundos')
        elif text == "FECHA":
            return (f'Fecha: {fecha}')
    else:
        return ('Error al obtener la hora actual en Bogotá')

recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()
iniciar = True

while iniciar:
    try:
        text = oir("ESCUCHANDO")
        if text[:7] == "VIERNES":
            responder("Señor")
            while True:
                with sr.Microphone() as source:
                    text=oir("CUENTEME")
                    if text == "SALIR":
                        responder("Fue un placer ingeniero")
                        iniciar=False
                        break
                    elif text == "CLIMA":
                        climaBogota = clima()
                        responder(climaBogota)
                    elif text == "TIEMPO":
                        tiempoActual = tiempo()
                        responder(tiempoActual)
                    elif text =="SALUDA":
                        responder("HOLA SOY VIERNES TU AYUDANTE VIRTUAL")
                    elif text == "MÚSICA":
                        musica()

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"Error en la solicitud: {e}")
