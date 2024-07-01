import pyautogui
import time
import win32api
import win32gui
import win32con
import ctypes
import pygetwindow as gw

def funcao_abre_whatsapp():
    # Abrir o aplicativo WhatsApp do Windows
    pyautogui.press('win')
    time.sleep(2)  # Aguardar 2 segundos para abrir o aplicativo WhatsApp
    pyautogui.write('WhatsApp')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)  # Aguardar 5 segundos para abrir o WhatsApp
    
    # Maximizar o aplicativo WhatsApp na tela
    whatsapp_window_list = gw.getWindowsWithTitle('WhatsApp')
    if whatsapp_window_list:
        whatsapp_window = whatsapp_window_list[0]  # Acessa o primeiro elemento da lista
        whatsapp_window.maximize()

def funcao_monitor2():
    # Sequência de comandos no teclado para deixar Tela Inteira
    #pyautogui.keyDown('win')
    #pyautogui.press('right')
    #pyautogui.press('right')
    #pyautogui.press('up')
    #pyautogui.press('up')
    #pyautogui.keyUp('win')
    #time.sleep(1)

    # Encontra o identificador de janela (handle) da janela do WhatsApp
    hwnd = win32gui.FindWindow(None, 'WhatsApp')

    # Obtém as coordenadas do retângulo da janela
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)

    # Calcula a posição do meio
    meio_x = (left + right) / 2
    meio_y = (top + bottom)*0.022

    return meio_x, meio_y

    # Testa a função funcao_monitor2()
    meio_x, meio_y = funcao_monitor2()
    print("Posição do meio X:", meio_x)
    print("Posição do meio Y:", meio_y)
    time.sleep(5)
    print("aguarde o clique")
    pyautogui.click(x=meio_x, y=meio_y)
    print("Clicado no meio com sucesso")
    time.sleep(5)

def funcao_tela_cheia():
    whatsapp_window_list = gw.getWindowsWithTitle('WhatsApp')
    if whatsapp_window_list:
        whatsapp_window = whatsapp_window_list[0]  # Acessa o primeiro elemento da lista
        # Obter o tamanho da tela
        screen_width = win32api.GetSystemMetrics(0)
        screen_height = win32api.GetSystemMetrics(1)

        # Definir a altura da janela do WhatsApp para 100% da altura da tela
        whatsapp_window.resizeTo(whatsapp_window.width, screen_height)
        time.sleep(2)
        whatsapp_window.maximize()

def funcao_logout():
    pyautogui.press('Esc')
    time.sleep(1)
    pyautogui.press('Esc')
    time.sleep(0.5)
    pyautogui.press('Esc')
    pyautogui.click(x=30, y=monitor_1_resolution[1] - monitor_1_resolution[1]*0.13) # Clicar em Configurações
    time.sleep(1)
    pyautogui.click(x=30, y=monitor_1_resolution[1] - monitor_1_resolution[1]*0.09) # Clicar em Perfil
    time.sleep(1)
    pyautogui.click(x=monitor_1_resolution[0]*0.17, y=monitor_1_resolution[1]*0.7) # Clicar em Desconectar
    print("Desconectado do WhatsApp Web.")

# Função para obter a resolução do monitor
def get_monitor_resolution(monitor_number):
    # Obtém a área de trabalho do monitor especificado
    monitor_info = win32api.GetMonitorInfo(monitor_number)
    monitor_rect = monitor_info['Monitor']
    width = monitor_rect[2] - monitor_rect[0]  # Calcula a largura
    height = monitor_rect[3] - monitor_rect[1]  # Calcula a altura
    return width, height


whatsapp_window_list = gw.getWindowsWithTitle('WhatsApp')

if whatsapp_window_list:
    whatsapp_window = whatsapp_window_list[0]  # Acessa o primeiro elemento da lista

    # Calcula a posição do meio da janela
    meio_x = whatsapp_window.left + 200
    meio_y = whatsapp_window.top + 20

    # Obtém a posição da janela do WhatsApp
    window_position = whatsapp_window.left, whatsapp_window.top
    print(f'Window_Position: {window_position}')

    # Obtém a resolução do monitor
    monitor_1_resolution = get_monitor_resolution(1)
    monitor_2_resolution = get_monitor_resolution(2)

    print("Resolução do Monitor 1:", monitor_1_resolution)
    print("Resolução do Monitor 2:", monitor_2_resolution)

    # Imprime as coordenadas do meio
    print(f'Posição do meio X: {meio_x}')
    print(f'Posição do meio Y: {meio_y}')

    # Verificação Condicional
    while True:
        if -10 <= window_position[0] <= 1530: #-7 <= window_position[0] < monitor_1_resolution[0]:
            print("Monitor 1")
            funcao_abre_whatsapp()
            #funcao_tela_cheia()
            funcao_logout()
            break
        elif monitor_2_resolution[0]*-1 <= window_position[0] < -10: #monitor_1_resolution[0] <= window_position[0] < monitor_2_resolution[0]:
            print("Monitor 2")
            funcao_monitor2()
            #funcao_tela_cheia()
            funcao_logout()
            break
        else:
            print("Abrindo Whatsapp")
            funcao_abre_whatsapp()


#print(get_monitor_resolution(1))
print(f'Window_Position: {window_position}')

