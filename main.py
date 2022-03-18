from PIL import Image
from sty import Style, RgbFg, fg

import webcolors
import sys
import string
import random
import time

image = None
args = sys.argv
if len(args) > 1:
    image = args[1]
else:
    raise ValueError("Image not provided") 

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

try:
    log = sys.argv[2] == "log"
except:
    log = False

im = Image.open(image)
pixels = im.load()
size = im.size
width = size[0]
height = size[1]
im = im.resize((width//5, height//5), Image.LANCZOS)

start = time.time()

for h in range(height):
    for w in range(width):
        pix = pixels[w, h]

        if pix == (0,0,0,0) or pix == (0,0,0,255):
            print(" ", end="")
            continue

        if not log:
            # print(pix)
            print(
                fg(pix[0], pix[1], pix[2]) + random.choice(string.ascii_letters + string.digits) + fg.rs,
                end=""
            )
        
        if log: print(f"Pixel at ({w}, {h}):", pix)

    print("")

print("")
print("Time Elapsed: {} seconds".format(time.time() - start))
print("Press enter to exit...")

try:
    input("")
except KeyboardInterrupt:
    pass

sys.exit()
