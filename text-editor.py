import Tkinter as tk
import tkFileDialog
import tkMessageBox
from ScrolledText import *

root = tk.Tk()
textpad = ScrolledText(root, width=100, height=80)


class MainApplication(tk.Frame):
    def __init__(self, parent, textpad, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.textpad = textpad
        self.CreateMenu()

    def OpenCommand(self):
        self.files = tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file')
        if self.files != None:
            self.contents = self.files.read()
            self.textpad.insert('1.0', self.contents)
            self.files.close()

    def SaveCommand(self):
        self.files = tkFileDialog.asksaveasfile(mode='w')
        if self.files != None:
            self.data = self.textpad.get('1.0', tk.END+'-1c')
            self.files.write(self.data)
            self.files.close()

    def ExitCommand(self):
        if tkMessageBox.askokcancel("Quit", "Sure you want to quit?!"):
            root.destroy()

    def AboutCommand(self):
        self.label = tkMessageBox.showinfo("About", "It's a textpad")

    def CreateMenu(self):
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open", command=self.OpenCommand)
        self.filemenu.add_command(label="Save", command=self.SaveCommand)

        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.ExitCommand)

        self.helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.AboutCommand)


if __name__ == "__main__":
    textpad.pack()
    MainApplication(root, textpad).pack(side="top", fill="both", expand=True)
    root.mainloop()
