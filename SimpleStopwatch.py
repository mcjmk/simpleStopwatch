#! python3
# SimpleStopwatch.py - a simple application to check how much time your activities take.
import tkinter as tk
from tkinter import ttk
import time


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.activities = []
        self.running = False
        self.start_time = 0

        self.activity_entry = tk.Entry(self)
        self.activity_entry.pack()

        self.contents = tk.StringVar()
        self.contents.set("Action")
        self.activity_entry["textvariable"] = self.contents
        self.activity_entry.bind('<Key-Return>', self.record_activity)

        self.tree = ttk.Treeview(self, columns=('Activity', 'Since Start', 'Duration'), show='headings')
        self.tree.heading('Activity', text='Activity')
        self.tree.heading('Since Start', text='Since Start (s)')
        self.tree.heading('Duration', text='Duration (s)')
        self.tree.pack()

        self.stopwatch_container = tk.Frame(self)
        self.stopwatch_container.pack(side='right', fill='y')

        self.time_label = tk.Label(self.stopwatch_container, text="0:00:000", font=("Helvetica", 24))
        self.time_label.pack()

        self.start_stopwatch_button = tk.Button(self.stopwatch_container, text="Start", command=self.toggle_stopwatch)
        self.start_stopwatch_button.pack()

    def toggle_stopwatch(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.start_stopwatch_button.config(text="Stop")
            self.update_clock()
        else:
            self.running = False
            self.start_stopwatch_button.config(text="Start")

    def update_clock(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.time_label.config(text=self.format_time(elapsed_time))
            self.after(50, self.update_clock)

    @staticmethod
    def format_time(elapsed):
        minutes = int(elapsed / 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed - int(elapsed)) * 1000)
        return f"{minutes}:{seconds:02}:{milliseconds:03}"

    def record_activity(self, event):
        current_time = time.time()
        activity_name = self.contents.get()

        if self.activities:
            since_start = current_time - self.start_time
            duration = current_time - self.activities[-1][1]
        else:
            since_start = 0
            duration = 0

        self.activities.append((activity_name, current_time))
        self.tree.insert('', 'end', values=(activity_name, f"{since_start:.2f}", f"{duration:.2f}"))


root = tk.Tk()
root.geometry("600x400")
myapp = App(root)
myapp.mainloop()
