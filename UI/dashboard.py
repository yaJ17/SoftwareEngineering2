from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0" ##CHANGE THIS ACCORDINGLY


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x704")
window.configure(bg = "#1E1E1E")
window.title("REXIE")

canvas = Canvas(
    window,
    bg = "#1E1E1E",
    height = 704,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("settings.png"))
image_1 = canvas.create_image(
    42.208316802978516,
    626.4948120117188,
    image=image_image_1
)

canvas.create_rectangle(
    34.40623092651367,
    96.83332824707031,
    251.46354293823242,
    97.83332824707034,
    fill="#3B3B3B",
    outline="")

canvas.create_rectangle(
    29.786439895629883,
    524.9323120117188,
    246.848970413208,
    525.9323120117188,
    fill="#3B3B3B",
    outline="")

canvas.create_rectangle(
    250.46353149414062,
    74.78645324707031,
    1280.0000305175781,
    75.7864532470708,
    fill="#3B3B3B",
    outline="")

canvas.create_rectangle(
    250.96353149414062,
    36.0000114440918,
    251.96353149414062,
    837.0000114440918,
    fill="#3B3B3B",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    42.963523864746094,
    589.5051879882812,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1215.578125,
    38.89582443237305,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    52.260398864746094,
    41.197906494140625,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    42.239566802978516,
    552.6145629882812,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    292.875,
    248.39584350585938,
    image=image_image_6
)

canvas.create_rectangle(
    868.5208129882812,
    74.79165649414062,
    869.5208129882812,
    763.0052185058594,
    fill="#3B3B3B",
    outline="")

Dashboard_button_image_1 = PhotoImage(
    file=relative_to_assets("DB_button.png"))
Dashboard_button = Button(
    image=Dashboard_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Dashboard_button clicked"),
    relief="flat"
)
Dashboard_button.place(
    x=16.828105926513672,
    y=121.88540649414062,
    width=182.17189025878906,
    height=43.44791793823242
)

PMS_button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
PMS_button = Button(
    image=PMS_button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("PMS_button clicked"),
    relief="flat"
)
PMS_button.place(
    x=17.0,
    y=192.0,
    width=182.0,
    height=43.0
)

Sched_button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
Sched_button = Button(
    image=Sched_button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Sched_button clicked"),
    relief="flat"
)
Sched_button.place(
    x=17.0,
    y=313.0,
    width=182.0,
    height=43.0
)

IM_button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
IM_button = Button(
    image=IM_button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("IM_button clicked"),
    relief="flat"
)
IM_button.place(
    x=17.0,
    y=254.0,
    width=182.0,
    height=43.0
)

Report_button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
Report_button = Button(
    image=Report_button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Report_button clicked"),
    relief="flat"
)
Report_button.place(
    x=17.0,
    y=375.0,
    width=182.0,
    height=43.0
)

Transac_button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
Transac_button = Button(
    image=Transac_button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Transac_button clicked"),
    relief="flat"
)
Transac_button.place(
    x=17.0,
    y=435.0,
    width=182.0,
    height=43.0
)

logout_button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
Logout_button = Button(
    image=logout_button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Logout_button clicked"),
    relief="flat"
)
Logout_button.place(
    x=31.0,
    y=647.0,
    width=86.0,
    height=37.34375
)

canvas.create_rectangle(
    317.3697814941406,
    296.265625,
    328.3697814941406,
    306.4270839691162,
    fill="#000000",
    outline="")

image_image_7 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_7 = canvas.create_image(
    322.3697814941406,
    301.265625,
    image=image_image_7
)

canvas.create_rectangle(
    317.3697814941406,
    311.8385314941406,
    328.3697814941406,
    322.00519847869873,
    fill="#000000",
    outline="")

image_image_8 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_8 = canvas.create_image(

    322.3697814941406,
    316.8385314941406,
    image=image_image_8
)

canvas.create_rectangle(
    317.3697814941406,
    327.4166564941406,
    328.3697814941406,
    337.58332347869873,
    fill="#000000",
    outline="")

image_image_9 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_9 = canvas.create_image(
    322.3697814941406,
    332.4166564941406,
    image=image_image_9
)

canvas.create_rectangle(
    317.3697814941406,
    342.9895935058594,
    328.3697814941406,
    353.1562604904175,
    fill="#000000",
    outline="")

image_image_10 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_10 = canvas.create_image(
    322.3697814941406,
    346.9947814941406,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    504.6770935058594,
    301.265625,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_12 = canvas.create_image(
    685.0,
    301.265625,
    image=image_image_12
)

canvas.create_rectangle(
    499.6770935058594,
    311.8385314941406,
    510.6666774749756,
    322.00519847869873,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    680.0,
    311.8385314941406,
    690.9895839691162,
    322.00519847869873,
    fill="#000000",
    outline="")

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    504.6770935058594,
    316.8385314941406,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_14 = canvas.create_image(
    685.0,
    316.8385314941406,
    image=image_image_14
)

canvas.create_rectangle(
    499.6770935058594,
    327.4166564941406,
    510.6666774749756,
    337.58332347869873,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    680.0,
    327.4166564941406,
    690.9895839691162,
    337.58332347869873,
    fill="#000000",
    outline="")

image_image_15 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_15 = canvas.create_image(
    504.6770935058594,
    332.4166564941406,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_16 = canvas.create_image(
    685.0,
    332.4166564941406,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_17 = canvas.create_image(
    504.6770935058594,
    346.9270935058594,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_18 = canvas.create_image(
    685.0,
    346.9270935058594,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_19 = canvas.create_image(
    292.875,
    386.3645935058594,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    566.8801879882812,
    465.7552185058594,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    520.9322814941406,
    436.40625,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    406.92706298828125,
    472.796875,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_23 = canvas.create_image(
    406.92706298828125,
    622.796875,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_24 = canvas.create_image(
    433.6822814941406,
    472.0625,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_25 = canvas.create_image(
    567.7916564941406,
    615.9948120117188,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_26 = canvas.create_image(
    505.3020935058594,
    586.6458129882812,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_29.png"))
image_27 = canvas.create_image(
    378.33331298828125,
    203.22915649414062,
    image=image_image_27
)

image_image_28 = PhotoImage(
    file=relative_to_assets("image_30.png"))
image_28 = canvas.create_image(
    310.671875,
    203.35415649414062,
    image=image_image_28
)

image_image_29 = PhotoImage(
    file=relative_to_assets("image_29.png"))
image_29 = canvas.create_image(
    577.65625,
    204.75,
    image=image_image_29
)

image_image_30 = PhotoImage(
    file=relative_to_assets("image_30.png"))
image_30 = canvas.create_image(
    509.9895935058594,
    204.875,
    image=image_image_30
)

canvas.create_text(
    69.0,
    538.0,
    anchor="nw",
    text="Help",
    fill="#FFFFFF",
    font=("Poppins Light", 19 * -1)
)

canvas.create_text(
    31.0,
    495.0,
    anchor="nw",
    text="Support",
    fill="#8E8E8E",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    756.0,
    679.0,
    anchor="nw",
    text="See Details",
    fill="#7A69E9",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    756.0,
    529.0,
    anchor="nw",
    text="See Details",
    fill="#7A69E9",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    304.0,
    377.0,
    anchor="nw",
    text="Upcoming Deadlines",
    fill="#8E8E8E",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    304.0,
    240.0,
    anchor="nw",
    text="This week’s tasks",
    fill="#8E8E8E",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    905.0,
    116.0,
    anchor="nw",
    text="Recent Transaction History",
    fill="#8E8E8E",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    914.0,
    150.0,
    anchor="nw",
    text="Rexie Added new raw material",
    fill="#FFFFFF",
    font=("Poppins Light", 13 * -1)
)

canvas.create_text(
    914.0,
    186.0,
    anchor="nw",
    text="Rexie Added new raw material",
    fill="#FFFFFF",
    font=("Poppins Light", 13 * -1)
)

canvas.create_text(
    914.0,
    222.0,
    anchor="nw",
    text="Rexie Added new raw material",
    fill="#FFFFFF",
    font=("Poppins Light", 13 * -1)
)

canvas.create_text(
    1148.0,
    152.0,
    anchor="nw",
    text="Nov 29 2023",
    fill="#8E8E8E",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    1148.0,
    188.0,
    anchor="nw",
    text="Nov 29 2023",
    fill="#8E8E8E",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    1148.0,
    224.0,
    anchor="nw",
    text="Nov 29 2023",
    fill="#8E8E8E",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    35.0,
    67.0,
    anchor="nw",
    text="Menu",
    fill="#8E8E8E",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    86.0,
    45.0,
    anchor="nw",
    text="Bag Manufacturer",
    fill="#8E8E8E",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    1073.0,
    38.0,
    anchor="nw",
    text="Administrator",
    fill="#8E8E8E",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    1033.0,
    14.0,
    anchor="nw",
    text="Maris Pascual",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 21 * -1)
)

canvas.create_text(
    86.0,
    22.0,
    anchor="nw",
    text="Rexie Marie",
    fill="#FFFAFA",
    font=("Poppins BlackItalic", 20 * -1)
)

canvas.create_text(
    331.0,
    295.0,
    anchor="nw",
    text="Sew Zipper",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    330.0,
    194.0,
    anchor="nw",
    text="Raw Materials",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 13 * -1)
)

canvas.create_text(
    529.0,
    194.0,
    anchor="nw",
    text="Bag Products",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 13 * -1)
)

canvas.create_text(
    513.0,
    295.0,
    anchor="nw",
    text="Sew Zipper",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    693.3228759765625,
    295.0,
    anchor="nw",
    text="Sew Zipper",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    331.0,
    311.0,
    anchor="nw",
    text="Send over client ABCD products",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    513.0,
    311.0,
    anchor="nw",
    text="Send over client ABCD products",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    693.3228759765625,
    311.0,
    anchor="nw",
    text="Send over client ABCD products",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    331.0,
    326.0,
    anchor="nw",
    text="Talk to client Z",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    513.0,
    326.0,
    anchor="nw",
    text="Talk to client Z",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    693.3228759765625,
    326.0,
    anchor="nw",
    text="Talk to client Z",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    331.0,
    342.0,
    anchor="nw",
    text="Contact fabric supplier",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    513.0,
    342.0,
    anchor="nw",
    text="Contact fabric supplier",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    693.3228759765625,
    342.0,
    anchor="nw",
    text="Contact fabric supplier",
    fill="#FFFFFF",
    font=("Poppins ExtraLight", 8 * -1)
)

canvas.create_text(
    394.0,
    490.0,
    anchor="nw",
    text="Nov 29, 2023",
    fill="#FFFFFF",
    font=("Poppins Light", 16 * -1)
)

canvas.create_text(
    309.0,
    267.0,
    anchor="nw",
    text="Nov 29, 2023",
    fill="#FFFFFF",
    font=("Poppins Light", 16 * -1)
)

canvas.create_text(
    290.0,
    151.0,
    anchor="nw",
    text="Quick Add",
    fill="#FFFFFF",
    font=("Poppins Regular", 19 * -1)
)

canvas.create_text(
    320.0,
    21.0,
    anchor="nw",
    text="Dashboard",
    fill="#FFFFFF",
    font=("Poppins Medium", 24 * -1)
)

canvas.create_text(
    287.0,
    96.0,
    anchor="nw",
    text="Welcome, Maris Pasqual !",
    fill="#FFFFFF",
    font=("Poppins ExtraBold", 27 * -1)
)

canvas.create_text(
    491.0,
    267.0,
    anchor="nw",
    text="Nov 30, 2023",
    fill="#FFFFFF",
    font=("Poppins Light", 16 * -1)
)

canvas.create_text(
    673.0,
    267.0,
    anchor="nw",
    text="Dec 01, 2023",
    fill="#FFFFFF",
    font=("Poppins Light", 16 * -1)
)

canvas.create_text(
    311.0,
    418.0,
    anchor="nw",
    text="Straightforward",
    fill="#FFFFFF",
    font=("Poppins Regular", 24 * -1)
)

canvas.create_text(
    311.0,
    569.0,
    anchor="nw",
    text="ManyBags Co.",
    fill="#FFFFFF",
    font=("Poppins Regular", 24 * -1)
)

canvas.create_text(
    394.0,
    640.0,
    anchor="nw",
    text="Dec 23, 2023",
    fill="#FFFFFF",
    font=("Poppins Light", 16 * -1)
)

canvas.create_text(
    405.0,
    467.0,
    anchor="nw",
    text="A",
    fill="#FFFFFF",
    font=("Poppins Light", 8 * -1)
)

canvas.create_text(
    405.0,
    617.0,
    anchor="nw",
    text="A",
    fill="#FFFFFF",
    font=("Poppins Light", 8 * -1)
)

canvas.create_text(
    432.0,
    467.0,
    anchor="nw",
    text="B",
    fill="#FFFFFF",
    font=("Poppins Light", 8 * -1)
)

canvas.create_text(
    312.0,
    490.0,
    anchor="nw",
    text="Deadline",
    fill="#FFFFFF",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    312.0,
    640.0,
    anchor="nw",
    text="Deadline",
    fill="#FFFFFF",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    312.0,
    460.0,
    anchor="nw",
    text="Bag Type",
    fill="#FFFFFF",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    312.0,
    610.0,
    anchor="nw",
    text="Bag Type",
    fill="#FFFFFF",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    69.0,
    576.0,
    anchor="nw",
    text="About",
    fill="#FFFFFF",
    font=("Poppins Light", 19 * -1)
)

canvas.create_text(
    69.0,
    611.0,
    anchor="nw",
    text="Maintenance",
    fill="#FFFFFF",
    font=("Poppins Light", 19 * -1)
)

canvas.create_text(
    693.0,
    422.0,
    anchor="nw",
    text="50%",
    fill="#FFFFFF",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    714.0,
    569.0,
    anchor="nw",
    text="13%",
    fill="#FFFFFF",
    font=("Poppins Bold", 64 * -1)
)
window.resizable(False, False)
window.mainloop()
