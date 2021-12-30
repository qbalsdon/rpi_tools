#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD, Font

import platform

from common.networking import fetch_ip_address

def Close(main_window):
    main_window.destroy()

def create_main_window():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Control UI")

    # place a label on the root window
    bold25 = Font(root, size=25, weight=BOLD)
    message = tk.Label(root, text=f"{fetch_ip_address()} [{platform.platform()}]", font=bold25)
    message.pack()


    exit_button = tk.Button(root, text="Exit", command=lambda: Close(root))
    exit_button.pack(pady=20)
    # keep the window displaying
    root.mainloop()

if __name__ == "__main__":
    create_main_window()
