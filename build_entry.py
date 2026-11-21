"""Draw a vintage travel poster for Faroluna, the island the moon visits first."""
import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
CREAM = (243, 234, 211)
SKY_TOP, SKY_BOT = (16, 42, 67), (38, 84, 110)
SEA = (24, 68, 92)
MOON = (246, 231, 183)
CORAL = (224, 110, 74)
DARK = (13, 30, 48)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def F(p, s):
    return ImageFont.truetype(p, s)

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img, "RGBA")
# inner scene
X0, Y0, X1, Y1 = 46, 46, W - 46, H - 46
for y in range(Y0, Y1):
    t = (y - Y0) / (Y1 - Y0)
    d.line([(X0, y), (X1, y)], fill=tuple(int(SKY_TOP[i] + (SKY_BOT[i] - SKY_TOP[i]) * t) for i in range(3)))
# stars
random.seed(7)
for _ in range(120):
    sx, sy = random.randint(X0 + 8, X1 - 8), random.randint(Y0 + 8, Y0 + 430)
    r = random.choice([1, 1, 2])
    d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(255, 246, 214, random.randint(90, 200)))
# moon + halo
mx, my, mr = 512, 300, 128
for hr in range(190, 130, -12):
    d.ellipse([mx - hr, my - hr, mx + hr, my + hr], outline=(246, 231, 183, 14), width=6)
d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=MOON)
d.ellipse([mx - 58, my - 40, mx - 26, my - 8], fill=(232, 214, 160))
d.ellipse([mx + 30, my + 28, mx + 66, my + 64], fill=(232, 214, 160))
d.ellipse([mx + 2, my - 84, mx + 26, my - 60], fill=(232, 214, 160))
# sea
sea_y = 668
d.rectangle([X0, sea_y, X1, Y1], fill=SEA)
for i in range(9):
    yy = sea_y + 26 + i * 34
    off = (i % 2) * 46
    for x in range(X0 + 20 + off, X1 - 60, 118):
        d.arc([x, yy, x + 64, yy + 20], 180, 360, fill=(168, 216, 214, 130), width=3)
# moonlight path
for i in range(12):
    yy = sea_y + 18 + i * 26
    wdt = 30 + i * 16
    d.line([(mx - wdt, yy), (mx + wdt, yy)], fill=(246, 231, 183, max(30, 120 - i * 9)), width=4)
# island
d.polygon([(300, sea_y + 6), (724, sea_y + 6), (660, sea_y - 58), (364, sea_y - 58)], fill=(30, 44, 58))
d.polygon([(364, sea_y - 58), (660, sea_y - 58), (620, sea_y - 84), (404, sea_y - 84)], fill=(40, 58, 74))
# lighthouse
lx, base = 512, sea_y - 84
d.polygon([(lx - 34, base), (lx + 34, base), (lx + 22, base - 168), (lx - 22, base - 168)], fill=CREAM)
for i, yy in enumerate(range(base - 150, base - 20, 34)):
    if i % 2 == 0:
        d.polygon([(lx - 30 + (base - yy) * 0.07, yy), (lx + 30 - (base - yy) * 0.07, yy),
                   (lx + 28 - (base - yy - 30) * 0.07, yy + 30), (lx - 28 + (base - yy - 30) * 0.07, yy + 30)], fill=CORAL)
d.rectangle([lx - 26, base - 196, lx + 26, base - 168], fill=DARK)
d.ellipse([lx - 11, base - 190, lx + 11, base - 168], fill=(255, 214, 120))
d.polygon([(lx - 34, base - 196), (lx + 34, base - 196), (lx, base - 226)], fill=CORAL)
# beams
d.polygon([(lx - 20, base - 182), (X0 + 30, base - 262), (X0 + 30, base - 128)], fill=(255, 224, 140, 44))
d.polygon([(lx + 20, base - 182), (X1 - 30, base - 262), (X1 - 30, base - 128)], fill=(255, 224, 140, 44))
# birds
for bx, by, s in ((238, 208, 15), (292, 168, 11), (742, 190, 13)):
    d.arc([bx - s, by - s // 2, bx, by + s // 2], 200, 330, fill=(230, 238, 240), width=3)
    d.arc([bx, by - s // 2, bx + s, by + s // 2], 210, 340, fill=(230, 238, 240), width=3)
# frame
d.rectangle([X0, Y0, X1, Y1], outline=CREAM, width=3)
d.rectangle([22, 22, W - 22, H - 22], outline=(176, 60, 44), width=3)
# typography
def centered(text, y, font, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)
centered("F A R O L U N A", 66, F(SERIF, 64), CREAM)
centered("THE ISLAND THE MOON VISITS FIRST", 148, F(SANS, 21), (196, 224, 220))
centered("VISIT BY FERRY · NIGHTLY DEPARTURES · EST. NEVER", 934, F(SANSB, 19), (240, 200, 150))
img.save("entry.png", optimize=True)
print("saved", img.size)
