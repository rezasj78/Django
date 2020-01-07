import socket
from tkinter import Tk
from tkinter.filedialog import askopenfilename

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("localhost", 10000))
# socket.send("hello".encode("utf-8"))
Tk().withdraw()
path = askopenfilename()
file = open(path, 'r')
l = file.read(10)
while (l):
    print("sending", l)
    socket.send(l.encode("utf-8"))
    l = file.read(10)
file.close()
print("done sending!")
socket.close()
