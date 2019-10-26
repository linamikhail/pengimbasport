# Imbasan Port Berbilang Jaluran
# Mikhail Game Tech
# Nama Kod: PengimnasPort.py
# Python3 (Python Tiga)
#  __  __   _   _      _               _   _      ____                                _____                 _     
# |  \/  | (_) | | __ | |__     __ _  (_) | |    / ___|   __ _   _ __ ___     ___    |_   _|   ___    ___  | |__  
# | |\/| | | | | |/ / | '_ \   / _` | | | | |   | |  _   / _` | | '_ ` _ \   / _ \     | |    / _ \  / __| | '_ \ 
# | |  | | | | |   <  | | | | | (_| | | | | |   | |_| | | (_| | | | | | | | |  __/     | |   |  __/ | (__  | | | |
# |_|  |_| |_| |_|\_\ |_| |_|  \__,_| |_| |_|    \____|  \__,_| |_| |_| |_|  \___|     |_|    \___|  \___| |_| |_|
                                                                                                                 
from queue import Queue
import socket
import threading

print ("Selamat menggunakan skrip Pengimbas Port Berbilang Jaluran kami.")
target = input("[+] Masukkan alamat IP sasaran: ")

queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Masukkan PORTs anda (diselangi dengan ruang kosong):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} adalah TERBUKA!".format(port))
            open_ports.append(port)

def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Senarai Ports TERBUKA: Port No: ", open_ports)

    print("Terima kasih kerana menggunakan pengimbas port berbilang jaluran ini")

run_scanner(100, 1)
