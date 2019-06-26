import sys, ascii-generator
from PIL import Image

if __name__ == "__main__":
    file_path = os.path.abspath("jotaro.jpg")

    im = Image.open(file_path)

    im = resize(im, 40)

    pixels_matrix = convert_to_pixel(im)

    brightness_matrix = convert_to_grayscale(pixels_matrix)

    ascii_matrix = convert_to_ascii(brightness_matrix, ASCII_CHARS)

    print_matrix(ascii_matrix)
