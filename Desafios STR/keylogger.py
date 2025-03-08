import pyautogui
import time
import threading

# Lista para armazenar as teclas pressionadas
teclas_pressionadas = []
parar_captura = threading.Event()

# Função para capturar as teclas pressionadas
def capturar_teclas():
    print("Iniciando captura de teclas. Pressione F8 para parar.")
    while not parar_captura.is_set():
        # Captura a tecla pressionada
        tecla = pyautogui.press()
        teclas_pressionadas.append(tecla)
        print(f"Tecla pressionada: {tecla}")

        # Verifica se a tecla F8 foi pressionada para parar a captura
        if tecla == 'f8':
            print("Captura de teclas finalizada.")
            parar_captura.set()

# Função para monitorar a tecla F8
def monitorar_f8():
    while not parar_captura.is_set():
        if pyautogui.press('f8'):
            parar_captura.set()

# Inicia a captura de teclas em uma thread separada
threading.Thread(target=capturar_teclas).start()
# Inicia a monitorização da tecla F8
monitorar_f8()

print(f"Teclas capturadas: {teclas_pressionadas}")
