
from PIL import Image

for i in range(6):
    img = Image.open("Images/kiblast.png")
    img.convert("RGBA")
    img = img.crop((i*20,0,i*20+20,20))
    img.save("Images/ki"+str(i)+".png")
