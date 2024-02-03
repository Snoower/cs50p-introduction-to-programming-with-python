import sys
from PIL import Image, ImageOps

def main():
    try:
        if len(sys.argv) <= 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif get_file_extension(sys.argv[2]) not in {"jpg","jpeg","png"}:
            sys.exit("Invalid output")
        elif get_file_extension(sys.argv[2]) != get_file_extension(sys.argv[1]):
            sys.exit("Input and output have different extensions")
        else:
            image = Image.open(sys.argv[1])
            shirt = Image.open('shirt.png')
            resized_image = ImageOps.fit(image, size=(600,600))
            resized_image.paste(shirt, shirt)
            resized_image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

def get_file_extension(filename):
    split = filename.split('.')
    if len(split) > 1:
        return split[-1].lower()
    else:
        return ""

if __name__ == "__main__":
    main()
