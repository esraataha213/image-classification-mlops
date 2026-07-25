import os
from PIL import Image


DATA_PATH = "data/raw/seg_train/seg_train"


bad_images = []

for root, dirs, files in os.walk(DATA_PATH):

    for file in files:

        file_path = os.path.join(root, file)

        try:
            img = Image.open(file_path)
            img.verify()

        except Exception:
            bad_images.append(file_path)


print("First bad images:")

for img in bad_images[:20]:
    print(img)

print("Total bad images:", len(bad_images))