import time

from PIL import Image, ImageDraw
import random


def icon_1():
    icon = Image.new(mode="RGB", size=(100, 100), color=(255, 255, 255))
    icon_half = Image.new(mode="RGB", size=(int(icon.width / 2), icon.height), color=(255, 255, 255))
    draw = ImageDraw.Draw(icon_half)
    dominant_colors = []
    # for color in range(3):
    #     dominant_colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    dominant_colors = [(0, 255, 0), (255, 255, 255), (0, 100, 0)]
    for x in range(0, icon_half.width):
        for y in range(0, icon_half.height):
            draw.point((x, y), random.choice(
                dominant_colors))  # (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    icon.paste(icon_half)
    icon_half = icon_half.transpose(Image.FLIP_LEFT_RIGHT)
    icon.paste(icon_half, (int(icon.width / 2), 0))
    icon = icon.resize((500, 500), resample=0)
    icon.save(f"icon0_{random.random()}.png")
    icon.show()


def icon_2(symetrie: bool = False, grid: bool = True):
    icon = Image.new(mode="RGB", size=(2049, 2049), color=(255, 255, 255))
    if symetrie:
        f = 5
    else:
        f = round(icon.width / 2)
    icon_half = Image.new(mode="RGB", size=(f, icon.height), color=(255, 255, 255))
    draw = ImageDraw.Draw(icon_half)
    dominant_colors = []
    # for color in range(3):
    #     dominant_colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    dominant_colors = [(0, 255, 0), (0, 100, 0), (255, 255, 255)]
    for x in range(0, icon_half.width):
        for y in range(0, icon_half.height):
            draw.point((x, y), random.choice(dominant_colors))  # (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    if symetrie:
        for x in range(round(icon.width / f)):
            print(x)
            icon.paste(icon_half, (x * f, 0))
            if x * f >= icon.width / 2:
                icon.paste(icon_half.transpose(Image.FLIP_LEFT_RIGHT), (x * f, 0))
    else:
        icon.paste(icon_half)
        icon_half = icon_half.transpose(Image.FLIP_LEFT_RIGHT)
        icon.paste(icon_half, (int(icon.width / 2), 0))
    if grid:
        grid_color = (255, 255, 255)
        draw = ImageDraw.Draw(icon)
        for x in range(icon.width+1):
            if x % 2 == 0:
                draw.line(((x, icon.height), (0, x)),  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 1)
        for y in range(icon.width+1):
            if y % 2 == 0:
                draw.line(((icon.width, y), (y, 0)),  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 1)

    icon = icon.resize(icon.size, resample=0)
    icon.save(f"icon1_{time.time()}.png")
    icon.show()


if __name__ == "__main__":
    icon_2()
