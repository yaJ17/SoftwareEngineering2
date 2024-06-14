import subprocess
from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

# Set the path for assets folder
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0" ##CHANGE THIS ACCORDINGLY

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Create the main window
window = Tk()
window.geometry("1223x668")
window.configure(bg="#1F1F1F")
window.title("REXIE")

# Create a canvas
canvas = Canvas(
    window,
    bg="#1F1F1F",
    height=668,
    width=1223,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Draw rectangles and text
canvas.create_rectangle(
    88.49998474121094,
    329.3177185058594,
    349.9427032470703,
    377.5416793823242,
    fill="#000000",
    outline=""
)
canvas.create_rectangle(
    88.49998474121094,
    417.8854064941406,
    349.9427032470703,
    466.10936737060547,
    fill="#000000",
    outline=""
)
canvas.create_text(
    88.0,
    304.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("DMSans Regular", 15 * -1)
)
canvas.create_text(
    88.0,
    393.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("DMSans Regular", 15 * -1)
)

# Create Entry widgets for username and password
username_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 16),
    insertwidth=10
)
username_entry.insert(0, "")
username_entry.place(
    x=88.0416488647461,
    y=328.859375,
    width=262.3645935058594,
    height=47.140625
)

password_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 16),
    insertwidth=10,
    show="•"
)
password_entry.insert(0, "")
password_entry.place(
    x=88.0416488647461,
    y=417.4270935058594,
    width=262.3645935058594,
    height=47.145835876464844
)

# Create buttons and images
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    944.8958129882812,
    374.6666564941406,
    image=image_image_1
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
submit_signin = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("submit_signin clicked"),
    relief="flat"
)
submit_signin.place(
    x=85.0,
    y=489.0,
    width=109.0,
    height=55.0
)

# Create text labels
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
    text="Sign in",
    fill="#FFFFFF",
    font=("Poppins Bold", 24 * -1)
)

canvas.create_text(
    84.0,
    564.0,
    anchor="nw",
    text="Don’t have an existing account?",
    fill="#8E8E8E",
    font=("Poppins Regular", 16 * -1)
)

# Define function for the register button
def register_clicked(event):
    window.destroy()
    subprocess.Popen(["python", OUTPUT_PATH / "register.py"])

register_text = canvas.create_text(
    357.0,
    564.0,
    anchor="nw",
    text="Register",
    fill="#975BCE",
    font=("Poppins Regular", 16 * -1)
)

# Bind click event to register text
canvas.tag_bind(register_text, "<Button-1>", register_clicked)

canvas.create_text(
    85.0,
    591.0,
    anchor="nw",
    text="Forgot Password?",
    fill="#975BCE",
    font=("Poppins Regular", 16 * -1)
)

# Make the window non-resizable
window.resizable(False, False)

# Start the main event loop
window.mainloop()
