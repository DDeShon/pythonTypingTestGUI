import tkinter as tk
import time
import threading
import random

class TypeTestGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Test Application")
        self.root.geometry("800x600")

        self.text = open("text.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.text), font=("Georgia", 20), wraplength=700)
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input_entry = tk.Entry(self.frame, width=50, font=("Georgia", 16))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(self.frame, text="\nTyping Speed:  \n\n0.00 Words Per Second"
                                                     "\n0.00 Words Per Minute\n", font=("Georgia", 20))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, font=("Georgia", 20))
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()

        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"\nTyping Speed: \n\n{wps:.2f} Words Per Second\n{wpm:.2f} Words Per Minute\n")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="\nTyping Speed:  \n\n0.00 Words Per Second\n0.00 Words Per Minute\n")
        self.sample_label.config(text=random.choice(self.text))
        self.input_entry.delete(0, tk.END)

TypeTestGUI()
