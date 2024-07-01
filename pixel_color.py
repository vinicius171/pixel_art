import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

def load_image(image_path):
    return cv2.imread(image_path)

def reduce_resolution(image, new_width, new_height):
    return cv2.resize(image, (new_width, new_height))

def extract_main_colors(image, num_colors):
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors)
    labels = kmeans.fit_predict(pixels)
    color_palette = kmeans.cluster_centers_.astype(np.uint8)
    return color_palette

def map_pixels_to_colors(image, color_palette):
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=color_palette.shape[0], init=color_palette, n_init=1)
    labels = kmeans.fit_predict(pixels)
    return kmeans.cluster_centers_[labels].reshape(image.shape).astype(np.uint8)

def create_pixel_art(original_image_path, output_folder, num_colors):
    original_image = load_image(original_image_path)
    reduced_image = reduce_resolution(original_image, 100, 100)
    color_palette = extract_main_colors(reduced_image, num_colors)
    colored_image = map_pixels_to_colors(reduced_image, color_palette)


    os.makedirs(output_folder, exist_ok=True)

  
    image_name = os.path.splitext(os.path.basename(original_image_path))[0]
    output_path = os.path.join(output_folder, f"{image_name}_pixel_art.png")

    cv2.imwrite(output_path, colored_image)
    print(f"Imagem Pixel Art salva em: {output_path}")

def posterize_image(image_path, output_folder, num_colors):
    original_image = Image.open(image_path)
    posterized_image = original_image.convert("P", palette=Image.ADAPTIVE, colors=num_colors)

    
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = os.path.join(output_folder, f"{image_name}_posterized.png")

    posterized_image.save(output_path)
    print(f"Imagem posterizada salva como '{output_path}' com {num_colors} cores.")


original_image_path = "img/deuses-da-india-os-principais-e-mais-conhecidos-9.jpg"
output_folder = "output_images"
num_colors = 10
create_pixel_art(original_image_path, output_folder, num_colors)
posterize_image(original_image_path, output_folder, num_colors)
