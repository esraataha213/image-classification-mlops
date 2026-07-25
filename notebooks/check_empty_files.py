import os

DATASET = "data/raw/seg_train/seg_train"

empty_files = []

for root, dirs, files in os.walk(DATASET):

    for file in files:

        path = os.path.join(root, file)

        if os.path.getsize(path) == 0:
            empty_files.append(path)

print(f"Empty files: {len(empty_files)}")

for file in empty_files[:20]:
    print(file)