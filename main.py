from PIL import Image
from sty import fg, bg

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
                bg(pix[0], pix[1], pix[2]) + fg(pix[0], pix[1], pix[2]) + random.choice(string.ascii_letters + string.digits + "!@#$%^&*()|_-=+[]{}\|;:\"'<>/,.?") + fg.rs + bg.rs,
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
