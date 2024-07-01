import pygetwindow as gw
import ctypes

class MONITORINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_uint),
        ("rcMonitor", ctypes.wintypes.RECT),
        ("rcWork", ctypes.wintypes.RECT),
        ("dwFlags", ctypes.c_uint)
    ]

def get_monitor_resolution(monitor_number):
    user32 = ctypes.windll.user32
    monitor_info = MONITORINFO()
    monitor_info.cbSize = ctypes.sizeof(MONITORINFO)
    user32.GetMonitorInfoW(user32.MonitorFromWindow(0, 1), ctypes.byref(monitor_info))
    monitor = monitor_info.rcMonitor
    width = monitor.right - monitor.left
    height = monitor.bottom - monitor.top
    return width, height

# Obtendo a resolução do primeiro monitor
monitor_resolution_1 = get_monitor_resolution(0)

# Obtendo a resolução do segundo monitor
monitor_resolution_2 = get_monitor_resolution(1)
monitor_resolution_3 = get_monitor_resolution(2)

# Exibindo as resoluções dos monitores
print("Resolução do primeiro monitor:", monitor_resolution_1)
print("Resolução do segundo monitor:", monitor_resolution_2)
print("Resolução do terceiro monitor:", monitor_resolution_3)
