from PIL import Image

path = input("Input path to photo: ")

image = Image.open(path)
px = image.load()
width, height = image.size
grey_image = [[] for _ in range(height)]
symbols = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^'. "

for y in range(height):
    for x in range(width):
        grayscale_value = int(
            (0.3 * px[x, y][0] + 0.59 * px[x, y][1] + 0.11 * px[x, y][2])
        )
        symbol_index = int(grayscale_value / 256 * len(symbols))
        grey_image[y].append(symbols[symbol_index])

for row in grey_image:
    print("".join(row))

with open("ascii_art.txt", "w") as file:
    for row in grey_image:
        file.write("".join(row) + "\n")