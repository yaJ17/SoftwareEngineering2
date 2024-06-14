import os
import subprocess
from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0" ##CHANGE THIS ACCORDINGLY ##CHANGE THIS ACCORDINGLY

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1223x668")
window.configure(bg = "#1F1F1F")
window.title("REXIE")

canvas = Canvas(
    window,
    bg = "#1F1F1F",
    height = 668,
    width = 1223,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

canvas.create_rectangle(
    88.49998474121094,
    329.3177185058594,
    349.9427032470703,
    377.5416793823242,
    fill="#000000",
    outline=""
)

register_username_entry_image = PhotoImage(
    file=relative_to_assets("entry_1.png")
)
register_username_entry_bg = canvas.create_image(
    219.22394561767578,
    353.4296875,
    image=register_username_entry_image
)
register_username_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 16),
    insertwidth=10
)
register_username_entry.insert(0, "")
register_username_entry.place(
    x=88.0416488647461,
    y=328.859375,
    width=262.3645935058594,
    height=47.140625
)

canvas.create_rectangle(
    88.49998474121094,
    417.8854064941406,
    349.9427032470703,
    466.10936737060547,
    fill="#000000",
    outline=""
)

register_password_entry_image = PhotoImage(
    file=relative_to_assets("entry_2.png")
)
register_password_entry_bg = canvas.create_image(
    219.22394561767578,
    442.0000114440918,
    image=register_password_entry_image
)
register_password_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 16),
    insertwidth=10,
    show="•"
)
register_password_entry.insert(0, "")
register_password_entry.place(
    x=88.0416488647461,
    y=417.4270935058594,
    width=262.3645935058594,
    height=47.145835876464844
)

register_button_image = PhotoImage(
    file=relative_to_assets("button_1.png")
)
register_button = Button(
    image=register_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Register button clicked"),
    relief="flat"
)
register_button.place(
    x=85.0,
    y=489.0,
    width=109.0,
    height=55.0
)

background_image = PhotoImage(
    file=relative_to_assets("regbg.png")
)
background = canvas.create_image(
    944.8958129882812,
    365.6666564941406,
    image=background_image
)

canvas.create_text(
    79.0,
    77.0,
    anchor="nw",
    text="Rexie Marie Production ",
    fill="#FFFFFF",
    font=("Poppins Bold", 60 * -1)
)

canvas.create_text(
    79.0,
    141.0,
    anchor="nw",
    text="Management System",
    fill="#FFFFFF",
    font=("Poppins Bold", 60 * -1)
)

canvas.create_text(
    85.0,
    252.0,
    anchor="nw",
    text="Register",
    fill="#FFFFFF",
    font=("Poppins Bold", 24 * -1)
)

canvas.create_text(
    84.0,
    564.0,
    anchor="nw",
    text="Already have an existing account?",
    fill="#8E8E8E",
    font=("Poppins Regular", 16 * -1)
)

def signin_clicked(event):
    window.destroy()
    subprocess.Popen(["python",OUTPUT_PATH / "signin.py"])

signin_text = canvas.create_text(
    365.0,
    564.0,
    anchor="nw",
    text="Sign in",
    fill="#975BCE",
    font=("Poppins Regular", 16 * -1)
)

canvas.tag_bind(signin_text, "<Button-1>", signin_clicked)

canvas.create_text(
    88.0,
    304.0,
    anchor="nw",
    text="USERNAME",
    fill="#FFFFFF",
    font=("DMSans Regular", 15 * -1)
)

canvas.create_text(
    88.0,
    393.0,
    anchor="nw",
    text="PASSWORD",
    fill="#FFFFFF",
    font=("DMSans Regular", 15 * -1)
)

window.resizable(False, False)
window.mainloop()
