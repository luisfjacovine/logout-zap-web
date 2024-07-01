import pyautogui
import time
import ctypes

# Função para identificar Resolução do monitor principal
def get_monitor_resolution(monitor_number):
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    return screen_width, screen_height

def get_whatsapp_window_info():
    whatsapp_window = pyautogui.getWindowsWithTitle('WhatsApp')[0]  # Obtém a janela do Whatsapp
    width = whatsapp_window.width  # Largura da janela
    height = whatsapp_window.height  # Altura da janela
    left_position = whatsapp_window.left  # Posição da esquerda da janela
    top_position = whatsapp_window.top  # Posição do topo da janela
    return width, height, left_position, top_position



# Função principal
def main():
    # Identifica a largura, altura, posição da esquerda e posição do topo da janela do Whatsapp
    width, height, left_position, top_position = get_whatsapp_window_info()
    whatsapp_target_x = left_position + width / 2
    whatsapp_target_y = top_position + 10

    print(f"Largura da janela do WhatsApp: {width}")
    print(f"Altura da janela do WhatsApp: {height}")
    print(f"Posição da esquerda da janela do WhatsApp: {left_position}")
    print(f"Posição do topo da janela do WhatsApp: {top_position}")
    print(f"Posição X alvo no WhatsApp: {whatsapp_target_x}")
    print(f"Posição Y alvo no WhatsApp: {whatsapp_target_y}")

    monitor_1_width, monitor_1_height = get_monitor_resolution(1)
    print(f"Resolução do monitor 1: {monitor_1_width}x{monitor_1_height}")

if __name__ == "__main__":
    main()
