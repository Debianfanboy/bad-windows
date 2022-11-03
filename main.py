from PIL import Image
from time import sleep
from os import system

frames = []
for i in range(1,3286):
    filename = f"new{i}.png"
    with Image.open(filename) as image:
        # 255 = @
        # 200 = &
        # 150 = #
        # 100 = $
        # 50 = +
        # 30 = -
        # 20 = .
        # <20 = " "
        frame = ""
        for pix in image.getdata(0):
            if pix == 255:
                frame += "@"
            elif pix >= 200:
                frame += "&"
            elif pix >= 150:
                frame += "#"
            elif pix >= 100:
                frame += "$"
            elif pix >= 50:
                frame += "+"
            elif pix >= 30:
                frame += "-"
            elif pix >= 20:
                frame += "."
            else:
                frame += " "
        frames.append(frame)
    if i % 5 == 0:
        print(f"{i}/3286")
print("playing")
for frame in frames:
    print(frame)
    sleep(0.06272)
    system("cls")
