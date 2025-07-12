# Cameron Mendez
# 07/10/2025
# Module 10.2 – To-Do App

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Window setup
        self.title("Mendez-ToDo")
        self.geometry("500x500")

        # Menu setup
        menu_bar = tk.Menu(self, bg="lightgoldenrod", fg="black")
        file_menu = tk.Menu(menu_bar, tearoff=0, bg="salmon", fg="black")
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

        # UI frames and scrollbar
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Instruction label
        todol = tk.Label(self.tasks_frame, text="Right-click a task to delete it", bg="lightgoldenrod", fg="black", pady=10)
        todol.bind("<Button-3>", self.remove_task)
        self.tasks.append(todol)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        # Event bindings
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # Alternating background color scheme
        self.colour_schemes = [
            {"bg": "lightgoldenrod", "fg": "black"},
            {"bg": "salmon", "fg": "black"}
        ]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", f"Delete '{task.cget('text')}'?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, style_index = divmod(position, 2)
        scheme = self.colour_schemes[style_index]
        task.configure(bg=scheme["bg"], fg=scheme["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
