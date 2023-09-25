
import tkinter as tk
from tkinter import Menu, Button
from tkinter.filedialog import askopenfilename, asksaveasfilename
from analizador import analizar, generar_reporte_errores  # Dummy import, please replace with actual import

# Redesigned ScrollText Class


class TextLineNumbers(tk.Canvas):
    def __init__(self, text_widget, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.text_widget = text_widget
        self.redraw()

    def redraw(self, *args):
        '''Redraw line numbers'''
        self.delete("all")

        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            line_num = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=line_num, fill="#000000")
            i = self.text_widget.index(f"{i}+1line")

# Modify the ScrollText class to include the line numbers widget
class ScrollText(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(self, undo=True, bg="#FFF")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.line_numbers = TextLineNumbers(self, width=30)
        
        self.vsb.pack(side="right", fill="y")
        self.line_numbers.pack(side="left", fill="y", padx=(5, 0))
        self.text.pack(side="right", fill="both", expand=True)
        
        self.text.bind("<Change>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        self.text.bind('<KeyRelease>', self._on_change)
        self.text.bind('<Button-1>', self._on_change)
        self.text.bind('<MouseWheel>', self._on_change)


    def _on_change(self, event):
        self.line_numbers.redraw()

class ScrollText(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, bg="#2C2C2C", **kwargs)
        self.text = tk.Text(
            self,
            bg="#2C2C2C",
            fg="#FFFFFF",
            insertbackground="#FFA500",
            selectbackground="#555555",
            wrap="none",
            undo=True,
            font=("Consolas", 12)
        )
        self.text.pack(side="left", fill="both", expand=True)

        self.scroll_y = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.scroll_y.pack(side="right", fill="y")
        self.text["yscrollcommand"] = self.scroll_y.set

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

# Redesigned Main Window Class
class RedesignedApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sophisticated Editor")
        self.geometry("800x600")
        self.configure(bg="#1E1E1E")

        # Menu Bar
        self.menu = Menu(self, bg="#333333", fg="#FFFFFF")
        self.config(menu=self.menu)
        file_menu = Menu(self.menu, tearoff=0, bg="#333333", fg="#FFFFFF")
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.clear_content)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Text Editor with Scrollbars
        self.scroll_text = ScrollText(self)
        self.scroll_text.pack(fill="both", expand=True)

        # Action Buttons
        self.analyze_button = Button(
            self,
            text="Analizar",
            command=self.analyze_text,
            bg="#5A9",
            fg="#FFF",
            font=("Arial", 12)
        )
        self.analyze_button.pack(side="left", padx=10, pady=10)
        # Reportes Button
        self.report_button = Button(
            self,
            text="Reportes",
            command=self.analyze_text,
            bg="#5A9",
            fg="#FFF",
            font=("Arial", 12)
        )
        self.report_button.pack(side="left", padx=10, pady=10)


        # Button to view errors
        self.errors_button = Button(
            self,
            text="Ver Errores",
            command=self.view_errors,
            bg="#5599FF",
            fg="#FFF",
            font=("Arial", 12)
        )
        self.errors_button.pack(side="left", padx=10, pady=10)

    def view_errors(self):
        generar_reporte_errores()
    def clear_content(self):
        self.scroll_text.text.delete("1.0", tk.END)



    
        

    def open_file(self):
        filepath = askopenfilename(filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
        if filepath:
            with open(filepath, "r") as file:
                self.scroll_text.text.delete(1.0, tk.END)
                self.scroll_text.text.insert(tk.END, file.read())

    def save_file(self):
        filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filepath:
            with open(filepath, "w") as file:
                file.write(self.scroll_text.text.get(1.0, tk.END))

    def analyze_text(self):
        text = self.scroll_text.get(1.0, tk.END)
        arbol = analizar(text)
        print(arbol.dot.source)
        arbol.dot.view()

# Run the app
if __name__ == "__main__":
    app = RedesignedApp()
    app.mainloop()
