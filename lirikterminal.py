import time
from threading import Thread, Lock
import sys
import os

lock = Lock()

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def animasi_teks(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def timing_lirik(lirik, delay, speed):
    time.sleep(delay)
    animasi_teks(lirik, speed)

def print_lirik():
    lirik_isi = [
           # isi lirik. ("lirik",speed). ex: ("nananana",0.1)
    ]
    detik = [] # waktu dimunculkan lirik, gunakan detik jangan menit. ex: 2 menit -> 120 detik
    
    threads = []
    for i in range(len(lirik_isi)):
        lirik, speed = lirik_isi[i]
        t = Thread(target=timing_lirik, args=(lirik, detik[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    clear()
    print_lirik()
    # clear()
