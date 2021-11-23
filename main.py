import tkinter as tk
import time
import threading
import random

class TypeTestGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Test Application")
        self.root.geometry("800x600")

        self.sample_label = tk.Label(self.root, text="Sample Text")