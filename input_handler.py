import os, argparse
import ascii_generator as ascii
from PIL import Image

if __name__ == "__main__":
    # file_path = os.path.abspath("jotaro.jpg")

    # im = Image.open(file_path)

    # im = ascii.resize(im, 40)

    # pixels_matrix = ascii.convert_to_pixel(im)

    # brightness_matrix = ascii.convert_to_grayscale(pixels_matrix)

    # ascii_matrix = ascii.convert_to_ascii(brightness_matrix, ascii.ASCII_CHARS)

    # ascii.print_matrix(ascii_matrix)

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="inputfile.jpg", help="Input file path to image")
    parser.add_argument("--output", type=str, default="output.txt", help="Output file path to print out ascii art")
    parser.add_argument("-size", type=int, default=50, help="size of the output ascii art")
    args = parser.parse_args()
    print(args)