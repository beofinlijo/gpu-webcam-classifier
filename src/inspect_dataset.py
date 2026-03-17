import os
from pathlib import Path
import random
import matplotlib.pyplot as plt
from PIL import Image

DATA_DIR = Path("data/raw")

def count_images_per_class(data_dir: Path) -> None:
    print("Image count per class:\n")

    total = 0
    for class_dir in sorted(data_dir.iterdir()):
        if class_dir.is_dir():
            count = len([
                f for f in class_dir.iterdir()
                if f.suffix.lower() in [".jpg", ".jpeg", ".png"]
            ])
            total += count
            print(f"{class_dir.name}: {count}")

    print(f"\nTotal images: {total}")


def show_random_samples(data_dir: Path, samples_per_class: int = 5) -> None:
    class_dirs = [d for d in sorted(data_dir.iterdir()) if d.is_dir()]
    num_classes = len(class_dirs)

    fig, axes = plt.subplots(num_classes, samples_per_class, figsize=(15, 4 * num_classes))

    if num_classes == 1:
        axes = [axes]

    for row, class_dir in enumerate(class_dirs):
        image_files = [
            f for f in class_dir.iterdir()
            if f.suffix.lower() in [".jpg", ".jpeg", ".png"]
        ]

        chosen = random.sample(image_files, min(samples_per_class, len(image_files)))

        for col in range(samples_per_class):
            ax = axes[row][col] if num_classes > 1 else axes[col]

            if col < len(chosen):
                img = Image.open(chosen[col]).convert("RGB")
                ax.imshow(img)
                ax.set_title(f"{class_dir.name}")
            ax.axis("off")

    plt.tight_layout()
    plt.show()
def show_resized_samples(data_dir: Path, image_size=(128, 128), samples_per_class: int = 3) -> None:
    class_dirs = [d for d in sorted(data_dir.iterdir()) if d.is_dir()]
    num_classes = len(class_dirs)

    fig, axes = plt.subplots(num_classes, samples_per_class, figsize=(10, 4 * num_classes))

    if num_classes == 1:
        axes = [axes]

    for row, class_dir in enumerate(class_dirs):
        image_files = [
            f for f in class_dir.iterdir()
            if f.suffix.lower() in [".jpg", ".jpeg", ".png"]
        ]

        chosen = random.sample(image_files, min(samples_per_class, len(image_files)))

        for col in range(samples_per_class):
            ax = axes[row][col] if num_classes > 1 else axes[col]

            if col < len(chosen):
                img = Image.open(chosen[col]).convert("RGB")
                img = img.resize(image_size)
                ax.imshow(img)
                ax.set_title(f"{class_dir.name} - {image_size[0]}x{image_size[1]}")
            ax.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    count_images_per_class(DATA_DIR)
    show_random_samples(DATA_DIR, samples_per_class=5)
    show_resized_samples(DATA_DIR, image_size=(128, 128), samples_per_class=3)
