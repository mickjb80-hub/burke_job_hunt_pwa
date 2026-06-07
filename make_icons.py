#!/usr/bin/env python3
"""Generate CareerConsole app icons: clean CC monogram + subtle gear accent.
No spanner-C, no snake. Bold, high-contrast, readable at iPhone size."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os

OUT = os.path.dirname(os.path.abspath(__file__))
SIZES = [180, 192, 512]

BG_TOP = (24, 30, 38)      # near-black slate, slight blue
BG_BOT = (11, 13, 16)
BLUE   = (10, 132, 255)    # iOS blue
BLUE_HI= (90, 170, 255)
WHITE  = (233, 237, 242)

def rounded_mask(size, radius):
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, size-1, size-1], radius=radius, fill=255)
    return m

def vgrad(size, top, bot):
    g = Image.new("RGB", (1, size))
    for y in range(size):
        t = y / (size-1)
        g.putpixel((0, y), tuple(int(top[i]+(bot[i]-top[i])*t) for i in range(3)))
    return g.resize((size, size))

def load_font(px):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, px)
    return ImageFont.load_default()

def gear(draw, cx, cy, r, teeth, color, tooth=0.22, width=None):
    pts = []
    for i in range(teeth*2):
        ang = math.pi * i / teeth
        rad = r if i % 2 == 0 else r*(1-tooth)
        pts.append((cx + rad*math.cos(ang), cy + rad*math.sin(ang)))
    if width:
        draw.line(pts+[pts[0]], fill=color, width=width, joint="curve")
    else:
        draw.polygon(pts, fill=color)

def build(size):
    S = size * 4  # supersample
    img = Image.new("RGB", (S, S), BG_BOT)
    img.paste(vgrad(S, BG_TOP, BG_BOT), (0, 0))
    d = ImageDraw.Draw(img, "RGBA")

    # subtle gear accent, lower-right, low opacity (engineering hint, not literal)
    gear(d, int(S*0.78), int(S*0.80), int(S*0.20), 9, (10,132,255,60), tooth=0.30)
    d.ellipse([S*0.78-S*0.07, S*0.80-S*0.07, S*0.78+S*0.07, S*0.80+S*0.07], fill=BG_BOT)

    # CC monogram — two bold letters, blue + white, clearly separated
    f = load_font(int(S*0.40))
    def draw_C(x, y, color):
        bbox = d.textbbox((0,0), "C", font=f)
        w = bbox[2]-bbox[0]; h = bbox[3]-bbox[1]
        d.text((x - w/2 - bbox[0], y - h/2 - bbox[1]), "C", font=f, fill=color)
    draw_C(int(S*0.36), int(S*0.44), BLUE)
    draw_C(int(S*0.62), int(S*0.44), WHITE)

    # round corners
    radius = int(S*0.225)
    mask = rounded_mask(S, radius)
    out = Image.new("RGBA", (S, S), (0,0,0,0))
    out.paste(img, (0,0), mask)

    out = out.resize((size, size), Image.LANCZOS)
    return out

for s in SIZES:
    icon = build(s)
    icon.save(os.path.join(OUT, "icons", f"icon-{s}.png"))
    print("wrote icon-%d.png" % s)
