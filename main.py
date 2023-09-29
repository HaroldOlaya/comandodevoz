import speech_recognition as sr
import pyttsx3
import socket

# Función para enviar datos al ESP32
def enviar(valor):
    client_socket.send((valor).encode())

esp32_ip = "192.168.1.44"
esp32_port = 80

# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al ESP32
client_socket.connect((esp32_ip, esp32_port))
# Inicializar el reconocimiento de voz y el motor de texto a voz
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
                    print("Cuenteme...")
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio, language="es-ES")
                    print(f"Texto reconocido: {text}")
                    if text=="Salir" or text == "salir":
                        despedir="Fue un placer señor STARk"
                        text_to_speech.say(despedir)
                        text_to_speech.runAndWait()
                        iniciar=False
                        break
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









