
from PIL import Image
x=0
for i in range(12):
    for j in range(12):
        img = Image.open("Gogeta.png").convert("RGBA")
        print img.mode
        img = img.crop((j*32,i*32,j*32+32,i*32+32))
        img.save("Images/vegeta"+str(x)+".png")
        x+=1
