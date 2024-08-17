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
        ("I'm falling in love",0.117),
        ("I'm in love for the first time to you\n",0.099),
        ("Hatiku...",0.15),
        ("tercipta hanya untuk dirimu",0.12),
        ("Walau cinta tak harus memiliki",0.12),
        ("Kutetap setia mencintaimu\n",0.12),
        ("Hatiku...",0.15),
        ("tercipta hanya untuk dirimu (diriku)",0.15),
        ("Kutanamkan harapan di hatiku",0.15),
        ("Kau matahari di dalam hidupku",0.12),
        ("Kau matahari...",0.1),
        ("di dalam hidupku...",0.15)
    ]
    detik = [01.3, 06.2, 11.7, 15, 20.5, 26.1, 34.3, 37.6, 43.2, 48.5, 57, 62.7]
    
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