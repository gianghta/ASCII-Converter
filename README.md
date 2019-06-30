# ASCII-Converter
[![Python Version](https://img.shields.io/pypi/pyversions/slcp.svg)](https://www.python.org/downloads/release/python-370/)

Convert images into text based art(ASCII) to be either printed on terminal or exported to .txt file

## Example
![original image](https://github.com/gianghta/ASCII-Converter/blob/master/jotaro.jpg)
![example](https://github.com/gianghta/ASCII-Converter/blob/master/ascii-project.PNG)

## Usage

Clone repo and put the picture to convert in the same folder of the script
<pre>
Image to ASCII art [-h] [-o OUTPUT] [--size SIZE] inputFile

positional arguments:
inputFile                   the name of the image file

optional arguments:
-h, --help                  show this help message and exit
-o OUTPUT, --output OUTPUT  output file path to print out ascii art
--size SIZE                 size of the output ascii art
</pre>

## Requirements
* **>=python 3.7**
* **PIL**

## To Do
- [ ] Invert brightness
- [x] CLI Commands
- [ ] Support gif/animated
