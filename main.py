import tkinter as tk
import time
import threading
import random

class TypeTestGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Test Application")
        self.root.geometry("800x600")

        self.texts = open("texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Georgia", 20))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Georgia", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyDown>", self.start)

        self.speed_label = tk.Label(self.frame, text="Typing Speed:  \n0.00 WPS\n0.00 WPM", font=("Georgia", 20))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self):
        pass

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1

    def reset(self):
        pass


