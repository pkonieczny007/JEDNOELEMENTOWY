from PIL import Image
import os

def convert_tiff_to_jpg(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".tif") or filename.endswith(".tiff"):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            output_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.jpg')
            img.convert('RGB').save(output_path, "JPEG")

# Pobierz ścieżkę folderu, w którym znajduje się skrypt
current_folder = os.path.dirname(os.path.abspath(__file__))
convert_tiff_to_jpg(current_folder)
