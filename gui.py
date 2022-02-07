import tkinter as tk

top = tk.Tk()
#top.geometry("200x290")
top.title("Test")
top.attributes("-fullscreen", True)
filename = tk.PhotoImage(file = "~/gui/image.png")

background_label = tk.Label(top,image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
b1 = tk.Button(top, text="B1")
b1.place(x = 55, y = 65)

b2 = tk.Button(top, text="B2")
b2.place(x = 600, y = 65)
b3 = tk.Button(top, text="B3")
b3.place(x = 40, y = 200)

b4 = tk.Button(top,text = "b4")
b4.place(x = 650, y = 200)


top.mainloop()
