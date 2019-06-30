from PIL import Image
import os
import argparse

ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']

def resize(img, new_width=200):
    (old_width, old_height) = img.size
    ratio = float(old_width/old_height)
    new_height = int(ratio * new_width)
    new_image = img.resize((new_width, new_height))
    return new_image

def convert_to_pixel(img):
    pixels = list(img.getdata())
    pixles_matrix = []
    for i in range(0, len(pixels), img.width):
        pixles_matrix.append(pixels[i:i+img.width])
    return pixles_matrix

def rgb_to_gray(r ,g ,b):
    # Calculating shade of grey from RGB value using luminosity formula
    return (r * 0.299) + (g * 0.587) + (b * 0.114)

def convert_to_grayscale(px_matrix):

    temp_matrix = px_matrix

    for x in range(0, len(temp_matrix)):
        for y in range(0, len(temp_matrix[x])):
            pixel = temp_matrix[x][y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            gray_scale = rgb_to_gray(red, green, blue)
            temp_matrix[x][y] = int(gray_scale)
    return temp_matrix

def convert_to_ascii(brightness_matrix, ascii_chars):
    ascii_matrix = []
    for row in brightness_matrix:
        ascii_row = []
        for px in row:
            # Divide greyshade with max pixel value and multiply to get the correct shade of grey
            ascii_row.append(ascii_chars[int((px / 255) * (len(ascii_chars) - 1))])
        ascii_matrix.append(ascii_row)

    return ascii_matrix

def print_matrix(input_matrix):
    for row in input_matrix:
        line = [px*5 for px in row]
        print("".join(line))

def parse_handler():
    parser = argparse.ArgumentParser(prog="Image to ASCII art")
    parser.add_argument("inputFile", type=str, help="the name of the image file")
    parser.add_argument('-o', "--output", type=str, default="output.txt", help="output file path to print out ascii art")
    parser.add_argument("--size", type=int, help="size of the output ascii art")
    args = parser.parse_args()
    return args

def main(command):
    file_path = os.path.abspath(command.inputFile)
    
    img = Image.open(file_path)

    img = resize(img, command.size)

    pixles_matrix = convert_to_pixel(img)
    gs_matrix = convert_to_grayscale(pixles_matrix)

    ascii_matrix = convert_to_ascii(gs_matrix, ASCII_CHARS)
    print_matrix(ascii_matrix)

if __name__ == "__main__":
    command = parse_handler()
    main(command)



