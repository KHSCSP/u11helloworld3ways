import tkinter as tk

def click_button1(name):
    root = tk.Tk()
    root.wm_geometry("600x600")
    root.title("My GUI")
    frame2 = tk.Frame(root)
    frame2.grid(row=0, column=0, sticky='news')
    label2 = tk.Label(frame2, text="hello " + name, font=('Arial', 20))
    label2.pack()
    frame2.tkraise()

def gui_hello():
    # setup main window
    root = tk.Tk()
    root.wm_geometry("200x200")
    root.title("My GUI")
    
    # create frame 1
    frame1 = tk.Frame(root)
    frame1.grid(row=0, column=0, sticky='news')
    label1 = tk.Label(frame1, text="what's your name?", font=('Arial', 20))
    label1.pack()
    # create text box
    tb = tk.Entry(frame1, bd=3, font=('Arial', 20))
    tb.pack(pady=5)
    btn1 = tk.Button(frame1, text='enter', font=('Arial', 20), command=lambda: click_button1(tb.get()))
    btn1.pack()

    frame2 = tk.Frame(root)
    frame2.grid(row=0, column=0, sticky='news')
    label2 = tk.Label(frame2, text="")
    label2.pack()

    frame1.tkraise()
    root.mainloop()
    