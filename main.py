import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import json
from datetime import datetime

root = tk.Tk()
root.title("Coin Flipping")

bg_image = Image.open("bg.png")
bg_image = bg_image.resize((270, 270), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=270, height=270)
canvas.pack()

canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

question_image = Image.open("question-mark.png")
head_image = Image.open("head.png")
tail_image = Image.open("tail.png")
sand_image = Image.open("sand-watch.png")

question_image = question_image.resize((270, 270), Image.Resampling.LANCZOS)
head_image = head_image.resize((270, 270), Image.Resampling.LANCZOS)
tail_image = tail_image.resize((270, 270), Image.Resampling.LANCZOS)
sand_image = sand_image.resize((270, 270), Image.Resampling.LANCZOS)

question_photo = ImageTk.PhotoImage(question_image)
head_photo = ImageTk.PhotoImage(head_image)
tail_photo = ImageTk.PhotoImage(tail_image)
sand_photo = ImageTk.PhotoImage(sand_image)

def flip_coin(event):
    canvas.itemconfig(coin_image, image=sand_photo)
    root.update()

    time.sleep(0.5)

    outcome = random.choice(["Head", "Tail"])
    if outcome == "Head":
        canvas.itemconfig(coin_image, image=head_photo)
    else:
        canvas.itemconfig(coin_image, image=tail_photo)
    
    current_time = datetime.now().strftime("%B %d, %Y %H:%M:%S")

    result = outcome

    data = {
        "date": current_time,
        "result": result
    }

    with open('history.json', 'a') as f:
        if f.tell() != 0:
            f.write("\n")
        json.dump(data, f, indent=4)

coin_image = canvas.create_image(0, 0, anchor=tk.NW, image=question_photo)

canvas.bind("<Button-1>", flip_coin)

root.mainloop()