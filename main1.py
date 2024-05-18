import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def translator():


app = tk.Tk()

app.title("Translator Kitty")
app.geometry("600x300+100+100")

text_input = tk.Entry(width=50)
text_input.place(x=20, y=100)

source_language = ttk.Combobox( values=list(LANGUAGES.keys()))
source_language.place(x=20, y=80)
source_language.set("en")

target_language = ttk.Combobox( values=list(LANGUAGES.keys()))
target_language.place(x=20, y=130)
target_language.set("tr")

translate = tk.Button(text="Run Kitty!", font= "Verdana 18 bold", bg="pink", command= translator)
translate.place(x=330,y=80)

kitty = tk.Label(text="ฅ/ᐠ˶> ﻌ<˶ᐟ\ฅ", height=5)
kitty['font'] = "Verdana 12 bold"
kitty['fg'] = "#AA336A"
kitty.place(x=450, y=150)

text_output = tk.Text( height=5, width=50)
text_output.place(x=20,y=150)


label = tk.Label(text = "Translator Kitty", font = "Verdana 22 bold")
label.pack()

app.mainloop()