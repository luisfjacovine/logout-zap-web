import pyautogui
import time
import ctypes

# Função para identificar Resolução do monitor principal
def get_monitor_resolution(monitor_number):
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    return screen_width, screen_height

# Função para identificar a largura, altura e posição da esquerda da janela do Whatsapp
def get_whatsapp_window_info():
    whatsapp_windows = pyautogui.getWindowsWithTitle('WhatsApp')
    if whatsapp_windows:
        whatsapp_window = whatsapp_windows[0]  # Obtém a primeira janela do WhatsApp
        width = whatsapp_window.width  # Largura da janela
        height = whatsapp_window.height  # Altura da janela
        left_position = whatsapp_window.left  # Posição da esquerda da janela
        top_position = whatsapp_window.top  # Posição do topo da janela
        return width, height, left_position, top_position
    else:
        return None

# Função para abrir o WhatsApp
def open_whatsapp():
    pyautogui.press('win')
    time.sleep(2)  # Aguardar 2 segundos para abrir o menu Iniciar
    pyautogui.write('WhatsApp')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)  # Aguardar 5 segundos para abrir o WhatsApp

# Função principal
def main():
    # Tentar obter as informações da janela do WhatsApp
    window_info = get_whatsapp_window_info()
    
    # Se o WhatsApp não estiver aberto, abrir o aplicativo
    if window_info is None:
        print("WhatsApp não está aberto. Abrindo WhatsApp...")
        open_whatsapp()
        window_info = get_whatsapp_window_info()
        if window_info is None:
            print("Falha ao abrir o WhatsApp. Certifique-se de que o WhatsApp está instalado e tente novamente.")
            return

    # Descompactar as informações da janela do WhatsApp
    width, height, left_position, top_position = window_info
    whatsapp_target_x = left_position + width / 2
    whatsapp_target_y = top_position + 10

    # Obter a resolução do monitor principal
    monitor_1_resolution = get_monitor_resolution(1)

    open_whatsapp()
    pyautogui.press('Esc')
    time.sleep(0.5)
    pyautogui.press('Esc')
    time.sleep(0.5)
    pyautogui.press('Esc')

    pyautogui.mouseDown(whatsapp_target_x, whatsapp_target_y)
    time.sleep(0.5)
    # Move o cursor para o meio da largura e altura do monitor primário
    monitor_width, monitor_height = pyautogui.size()  # Resolução do monitor primário
    target_x = monitor_width // 2  # Meio da largura do monitor primário
    target_y = 0  # Topo da altura do monitor primário
    pyautogui.moveTo(target_x, target_y)
    time.sleep(2)

    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.click(x=30, y=monitor_1_resolution[1] - int(monitor_1_resolution[1] * 0.13))  # Clicar em Configurações
    time.sleep(1)
    pyautogui.click(x=30, y=monitor_1_resolution[1] - int(monitor_1_resolution[1] * 0.09))  # Clicar em Perfil
    time.sleep(1)
    pyautogui.click(x=int(monitor_1_resolution[0] * 0.17), y=int(monitor_1_resolution[1] * 0.7))  # Clicar em Desconectar
    time.sleep(1)
    pyautogui.click(x=int(monitor_1_resolution[0] * 0.45), y=int(monitor_1_resolution[1] * 0.55))  # Clicar em OK

if __name__ == "__main__":
    main()
