import time
from threading import Thread, Lock
import sys
import os
from tkinter import *

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

def timing_lirik(lirik, delay, speed, label):
    time.sleep(delay)
    label.config(text=label.cget("text") + lirik)

def print_lirik():
    lirik_isi = [
        ("I'm falling in love\n",0.117),
        ("I'm in love for the first time to you\n\n",0.099),
        ("Hatiku...\n",0.15),
        ("tercipta hanya untuk dirimu\n",0.12),
        ("Walau cinta tak harus memiliki\n",0.12),
        ("Kutetap setia mencintaimu\n\n",0.12),
        ("Hatiku...\n",0.15),
        ("tercipta hanya untuk dirimu (diriku)\n",0.15),
        ("Kutanamkan harapan di hatiku\n",0.15),
        ("Kau matahari di dalam hidupku\n",0.12),
        ("Kau matahari...\n",0.1),
        ("di dalam hidupku...\n",0.15)
    ]
    detik = [01.3, 06.2, 11.7, 15, 20.5, 26.1, 34.3, 37.6, 43.2, 48.5, 57, 62.7]

    window = Tk()
    window.title("Agatha Chelsea - Sunset")
    window.geometry("700x500")
    window.resizable(False,False)

    label = Label(window, text="", font=("Courier",20))
    label.pack(pady=20)

    threads = []
    for i in range(len(lirik_isi)):
        lirik, speed = lirik_isi[i]
        t = Thread(target=timing_lirik, args=(lirik, detik[i], speed, label))
        threads.append(t)
        t.start()

    window.mainloop()

if __name__ == "__main__":
    clear()
    print_lirik()