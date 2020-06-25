from PIL import Image
import os

files = []

print("Listing files . . .")
for r, d, f in os.walk('assets\\minecraft\\textures\\'):
    for file in f:
        if file.endswith(".png"):
            files.append(os.path.join(r, file))

max = len(files)
for f in files:
    print("Editing file - " + str(files.index(f)) + "/" + str(max) + " - " + f.split("\\")[-1])
    img = Image.open(f).convert('LA')
    img.save(f)
