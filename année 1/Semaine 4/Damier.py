from PIL import Image
img = Image.new("RGB", (15,15), "white") # create a new 15x15 image
pixels = img.load() # create the pixel map
black_2 = []
for i in range(img.size[0]):
    if i % 2 == 0:
        black_2.append(i)
black_1 = [i-1 for i in black_2 if i > 0]
if img.size[0] % 2 == 0: # 'that' if statement
    black_1.append(img.size[0]-1)

img.show()