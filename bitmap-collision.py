import math
from PIL import Image

def get_collision(filename):
    im = Image.open(filename).convert('RGB')
    pix = im.load()
    width, height = im.size
    content = []
    line = " "
    count = 0
    for y in range(height):
        for chunk in range(int(math.ceil(width / 8.0))):
            for x in range(8):
                if not chunk * 8 + x >= width:
                    if (pix[chunk * 8 + x, y][0] < 127):
                        line += (str(chunk * 8 + x) + ", " + str(y) + ", ")
                        count += 2

    line += ("count = " + str(count))
    content.append(line)
    with open(filename + '_collision.txt', 'w+') as f:
        for item in content:
            f.write("%s\n" % item)


if __name__ == "__main__":
    # txt_to_png("testcase.txt")
    get_collision("ground_floor.png")
