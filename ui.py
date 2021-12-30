#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

from common.networking import fetch_ip_address

def create_main_window():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Control UI")

    # place a label on the root window
    message = tk.Label(root, text=f"{fetch_ip_address()}")
    message.pack()

    # keep the window displaying
    root.mainloop()

if __name__ == "__main__":
    create_main_window()
