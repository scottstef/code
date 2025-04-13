##### heic_converter.py
#  This is a little script i wrote to convert images from my iphone camera that
#  were in HEIC format to PNG format.  I can't say the code is all mine, i did 
# query claude to find out what library would be best to use for the conversion
# after i got tired of searching thru apps to find a quick and easy converter
# online

## This program requires one argument (input_folder) and will accept an 
# optional second argument (output_folder).  The script will then search 
# the input folder and convert any .HEIC or .HEIF images into a jeg file
# with the same name, but a JPG extension since it has been converted to a
# jpeg

import os
import pyheif
from PIL import Image   
import sys

def convert_heic_to_jpg(input_folder, output_folder):
    if output_folder is None:
        output_folder = input_folder
        
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.heic', '.heif')):  # Corrected - needs parentheses
            heic_path = os.path.join(input_folder, filename)
            jpg_filename = os.path.splitext(filename)[0] + '.jpg'
            jpg_path = os.path.join(output_folder, jpg_filename)

            try:
                heif_file = pyheif.read(heic_path)
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )
                image.save(jpg_path, "JPEG")
                print(f"Converted {filename} to {jpg_path}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")
                continue

def main():
    if len(sys.argv) < 1:
        print("Usage: python script.py input_folder [output_folder]")
        return 1
        
    input_folder = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_heic_to_jpg(input_folder, output_folder)
    return 0

if __name__ == '__main__':  
    sys.exit(main())