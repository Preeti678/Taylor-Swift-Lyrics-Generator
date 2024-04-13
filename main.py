from tkinter import *
import requests


def get_lyrics():
    response = requests.get("https://taylorswiftapi.onrender.com/get")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Lyrics Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Taylor's Lyrics Goes HERE", width=250, font=("Times New Roman", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

taylor_img = PhotoImage(file="taylorSwift.png")
taylor_button = Button(image=taylor_img, highlightthickness=0, command=get_lyrics)
taylor_button.grid(row=1, column=0)

window.mainloop()
