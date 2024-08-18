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
           # isi lirik. ("lirik",speed). ex: ("nananana",0.1)
    ]
    detik = [] # waktu dimunculkan lirik, gunakan detik jangan menit. ex: 2 menit -> 120 detik
    
    window = Tk()    # inisiasi
    window.title("Judulnya")    # title/nama di atas kiri
    window.geometry("700x500")    # ukuran display
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
