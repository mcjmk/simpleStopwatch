#! python3
# SimpleStopwatch.py - a simple application to check how much time your activities take.
import tkinter as tk
import time


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.counter = 0
        self.time_counter = []

        self.activity_entry = tk.Entry()
        self.activity_entry.pack()

        self.contents = tk.StringVar()
        self.contents.set("Action")
        self.activity_entry["textvariable"] = self.contents
        self.activity_entry.bind('<Key-Return>', self.print_contents)

        self.labels_container = tk.Frame(self)
        self.labels_container.pack()

    def print_contents(self, event):
        current_time = time.time()
        activity_name = self.contents.get()
        self.time_counter.append(current_time)
        since_start = self.time_counter[-1] - self.time_counter[0]

        if len(self.time_counter) > 1:
            duration = self.time_counter[-1] - self.time_counter[-2]
        else:
            duration = 0

        activity_frame = tk.Frame(self.labels_container)
        activity_frame.pack(anchor='w')

        tk.Label(activity_frame, text=f"Czynność: {activity_name}").pack(side='left')
        tk.Label(activity_frame, text=f", Czas od startu: {since_start:.2f} s").pack(side='left')
        tk.Label(activity_frame, text=f", Czas trwania: {duration:.2f} s").pack(side='left')


root = tk.Tk()
myapp = App(root)
myapp.mainloop()
