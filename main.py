from PIL import Image, ImageDraw
import random


if __name__ == "__main__":
    icon = Image.new(mode="RGB", size=(100, 100), color=(255, 255, 255))
    icon_half = Image.new(mode="RGB", size=(int(icon.width/2), icon.height), color=(255, 255, 255))
    draw = ImageDraw.Draw(icon_half)
    dominant_colors = []
    for color in range(3):
        dominant_colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    for x in range(0, icon_half.width):
        for y in range(0, icon_half.height):
            draw.point((x, y), random.choice(dominant_colors)) # (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    icon.paste(icon_half)
    icon_half = icon_half.transpose(Image.FLIP_LEFT_RIGHT)
    icon.paste(icon_half, (int(icon.width/2), 0))
    icon = icon.resize((500, 500), resample=0)
    icon.save(f"yes{random.random()}.png")
