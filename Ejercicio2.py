import pyttsx3
import speech_recognition as sr

def voz(mensajes):
    engine = pyttsx3.init()

  # Ajustar la velocidad y el tono para hacer la voz más dulce
    engine.setProperty('rate', 150)  # Puedes ajustar la velocidad según tus preferencias (100 es la velocidad predeterminada)
    engine.setProperty('pitch', 150) 

    [engine.say(mensaje) for mensaje in mensajes]
    engine.runAndWait()

def reconocer_voz():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Dime lo que quieras hacer:")
        
        audio = recognizer.listen(source)

    try:
        print("Reconociendo...")
        return recognizer.recognize_google(audio, language="es")
    except (sr.UnknownValueError, sr.RequestError) as e:
        print(f"Error: {e}")
        return None

# Mensajes de bienvenida
mensajes_iniciales = "Hola, ¿cómo estás? Te saluda quora de TRONIC.","Me podrías decir tu nombre por favor."

# Llamada a la función voz con mensajes iniciales
voz(mensajes_iniciales)

# Espera la respuesta del usuario
respuesta = reconocer_voz()

while True:
    
 if respuesta == "Sandro":
    mensaje_bienvenida = f"Bienvenido ingeniero {respuesta}, ¿en qué puedo ayudarte?"
    print(respuesta)
    voz([mensaje_bienvenida])
    respuesta = reconocer_voz()

    if respuesta =="cantidad de alumnos":
        cantidad_de_alumnos = 17
        mensaje_cantidad = f"Entiendo, usted cuenta con {cantidad_de_alumnos} alumnos inscritos."
        print(respuesta)
        voz([mensaje_cantidad])
        
        #El programa pregunta si esque el ususario desea preguntar algo mas
       
        mensaje_de_solicitud="¿Desea que lo asista en algo mas?"
        voz([mensaje_de_solicitud])
        respuesta=reconocer_voz()
        
        if respuesta=="Si":
            retornando="Okey,digame ingeniero que otra consulta tiene"
            voz([retornando])
          
            continue
        else:
            despidiendo="Muchas gracias por usar Quora ingeniero"
            voz([despidiendo])
        
            break
    else:
        #el programa no entendio la voz del usuario
        Disculpa="Disculpa no le entendi"
        voz([Disculpa])


else:
    mensaje_final = "No te entendi lo siento"
    voz([mensaje_final])
