from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file = open(askopenfilename(), 'r')
print(file.read())