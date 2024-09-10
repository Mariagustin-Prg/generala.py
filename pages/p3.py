import tkinter as tk

class P3:
    def __init__(self) -> None:
        
        self.app = tk.Tk()

        self.app.geometry("1000x420+200+100")
        self.app.title("Generala!")
        self.app.resizable(True, True)
        self.app.config(bg="dark olive green")

        space = tk.Frame(self.app, height=20, bg= "dark olive green")
        space.pack()

        frame = tk.Frame(self.app, bg="lightgreen", height=90, width=300, bd= 100)
        frame.pack()


        self.app.mainloop()

















if __name__ == '__main__':
    app = P3()