import pygetwindow as gw
import ctypes



def logout_monitor_1():
    # Abrir o aplicativo WhatsApp do Windows
    pyautogui.press('win')
    time.sleep(2)  # Aguardar 2 segundos para abrir o aplicativo WhatsApp
    pyautogui.write('WhatsApp')
    pyautogui.press('enter')
    time.sleep(3)  # Aguardar 5 segundos para abrir o WhatsApp
    
# Ajustar a altura da janela para quebrar a estrutura de tela dividida do Windows
    # Obter a janela ativa do WhatsApp
    whatsapp_window = gw.getWindowsWithTitle('WhatsApp')[0]

    # Obter o tamanho da tela
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    # Definir a altura da janela do WhatsApp para 100% da altura da tela
    whatsapp_window.resizeTo(whatsapp_window.width, screen_height)
    time.sleep(2)

    # Sequência de comandos no teclado para deixar Tela Inteira
    pyautogui.keyDown('win')
    pyautogui.press('left')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.keyUp('win')
    time.sleep(1)

    # Clicar em Configurações (assumindo que as coordenadas do botão de configurações sejam (x, y))
    pyautogui.click(x=29, y=992)  # Substitua (x, y) pelas coordenadas reais do botão de configurações
    #pyautogui.click(pyautogui.locateCenterOnScreen('config-dark.jpg'))  # returns center x and y
    time.sleep(2)
    
    # Clicar no botão Desconectar (assumindo que as coordenadas do botão Desconectar sejam (x, y))
    pyautogui.click(x=349, y=767)  # Substitua (x, y) pelas coordenadas reais do botão Desconectar
    
    print("Desconectado do WhatsApp Web.")

def logout_monitor_2():
    # Abrir o aplicativo WhatsApp do Windows
    pyautogui.press('win')
    time.sleep(2)  # Aguardar 2 segundos para abrir o aplicativo WhatsApp
    pyautogui.write('WhatsApp')
    pyautogui.press('enter')
    time.sleep(3)  # Aguardar 5 segundos para abrir o WhatsApp
    whatsapp_window = gw.getWindowsWithTitle('WhatsApp')[0]

    # Obter o tamanho da tela
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    # Definir a altura da janela do WhatsApp para 100% da altura da tela
    whatsapp_window.resizeTo(whatsapp_window.width, screen_height)
    time.sleep(2)

    # Sequência de comandos no teclado para deixar Tela Inteira
    pyautogui.keyDown('win')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.keyUp('win')
    time.sleep(1)

# Função para obter a resolução do monitor
def get_monitor_resolution(monitor_number):
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    return screen_width, screen_height

# Função para verificar em qual monitor a janela está aberta
def check_whatsapp_monitor():
    # Procura pela janela do WhatsApp
    whatsapp_window = gw.getWindowsWithTitle('WhatsApp')
    if whatsapp_window:
        # Obtém a posição da janela do WhatsApp
        window_position = whatsapp_window[0].left, whatsapp_window[0].top
        # Obtém a resolução do monitor
        monitor_1_resolution = get_monitor_resolution(1)
        monitor_2_resolution = get_monitor_resolution(2)
        # Verifica em qual monitor a janela está aberta
        if -7 <= window_position[0] < monitor_1_resolution[0]:
            return "A janela do WhatsApp está aberta no Monitor 1"
        elif monitor_1_resolution[0] >= window_position[0] > monitor_2_resolution[0]:
            return "A janela do WhatsApp está aberta no Monitor 2"
        else:
            return "A janela do WhatsApp está aberta em um monitor além do Monitor 1 e Monitor 2"
    else:
        return "A janela do WhatsApp não está aberta."

if __name__ == "__main__":
    result = check_whatsapp_monitor()
    print(result)