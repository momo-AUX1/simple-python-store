import tkinter as tk 
import wget 
import os.path
from os.path import exists

app = tk.Tk()
app.title("installer")
app.config(height=300,width=480, background="gray")



def C1():
    if exists("notepad.py"):
        L.config(text="file already exists!", background="red")
    else: 
        wget.download("https://8000-cs-ddc4f778-0ad0-4648-a49e-e5912a9a2449.cs-europe-west1-xedi.cloudshell.dev/files/notepad.py","notepad.py")
        L.config(text="downloaded py notepad",background="green")

def C2():
    if exists("notepad.exe"):
        L.config(text="file already exists!", background="red")
    else: 
        wget.download("https://8000-cs-ddc4f778-0ad0-4648-a49e-e5912a9a2449.cs-europe-west1-xedi.cloudshell.dev/files/notepad.exe","notepad.exe")
        L.config(text="downloaded exe notepad",background="green")


def C3():
    if exists("YTDL.py"):
        L.config(text="file already exists!", background="red")
    else: 
        wget.download("https://8000-cs-ddc4f778-0ad0-4648-a49e-e5912a9a2449.cs-europe-west1-xedi.cloudshell.dev/files/YTDL.py","YTDL.py")
        L.config(text="downloaded py YTDL",background="green")

def C4():
    if exists("YTDL.exe"):
        L.config(text="file already exists!", background="red")
    else: 
        wget.download("https://8000-cs-ddc4f778-0ad0-4648-a49e-e5912a9a2449.cs-europe-west1-xedi.cloudshell.dev/files/YTDL.exe","YTDL.exe")
        L.config(text="downloaded exe YTDL",background="green")


def C5():
    if exists("url.py"):
        L.config(text="file already exists!", background="red")
    else: 
        wget.download("https://8000-cs-ddc4f778-0ad0-4648-a49e-e5912a9a2449.cs-europe-west1-xedi.cloudshell.dev/files/url.py","url.py")
        L.config(text="downloaded py url",background="green")

L = tk.Label(
    app,
    text="installer ver 0.1",
    background="yellow",
    font="roboto"
)


B1 = tk.Button(
    app,
    text="download python notepad",
    command= C1
)

B2 = tk.Button(
    app,
    text="download exe notepad",
    command= C2
)

B3 = tk.Button(
    app,
    text="download python youtube downloader",
    command= C3
)

B4 = tk.Button(
    app,
    text="download exe youtube downloader",
    command= C4
)


B5 = tk.Button(
    app,
    text="download python url shortener",
    command= C5
)


B5.place(x=130,y=200)
B4.place(x=240,y=150)
B3.place(x=240, y=100)
B2.place(x=40,y=150)
B1.place(x=40,y=100)
L.place(x=170,y=60)
app.mainloop()