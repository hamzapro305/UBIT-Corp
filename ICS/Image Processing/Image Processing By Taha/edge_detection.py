import struct
from math import floor


def printMatrix(array):
    for i in array:
        print(i)


def Keepinrange(value):
    if value < 0:
        return 0
    elif value > 255:
        return 255
    else:
        return value


img = open(f"C:\\Users\\Hp\\Downloads\\python_images\\forest1.BMP", "r+b")
img.seek(18, 0)
width = struct.unpack("i", img.read(4))[0]
height = struct.unpack("i", img.read(4))[0]
img.seek(10, 0)
offset = struct.unpack("i", img.read(4))[0]
blue = []
green = []
red = []
img.seek(offset, 0)
for i in range(height):
    bluetemp = []
    greentemp = []
    redtemp = []
    for j in range(width):
        bluetemp.append(int.from_bytes(img.read(1), "little"))
        greentemp.append(int.from_bytes(img.read(1), "little"))
        redtemp.append(int.from_bytes(img.read(1), "little"))
    blue.append(bluetemp)
    green.append(greentemp)
    red.append(redtemp)
kernel = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
img.seek(offset, 0)
for r in range(height):
    for c in range(width):
        if (r == 0 or r == height - 1) or (c == 0 or c == width - 1):
            b = int(blue[r][c]).to_bytes(1, "little")
            g = int(green[r][c]).to_bytes(1, "little")
            r_ed = int(red[r][c]).to_bytes(1, "little")
            img.write(b)
            img.write(g)
            img.write(r_ed)
        else:
            blueconv = (
                (kernel[0][0] * blue[r - 1][c - 1])
                + (kernel[0][1] * blue[r - 1][c])
                + (kernel[0][2] * blue[r - 1][c + 1])
                + (kernel[1][0] * blue[r][c - 1])
                + (kernel[1][1] * blue[r][c])
                + (kernel[1][2] * blue[r][c + 1])
                + (kernel[2][0] * blue[r + 1][c - 1])
                + (kernel[2][1] * blue[r + 1][c])
                + (kernel[0][0] * blue[r + 1][c + 1])
            )
            greenconv = (
                (kernel[0][0] * green[r - 1][c - 1])
                + (kernel[0][1] * green[r - 1][c])
                + (kernel[0][2] * green[r - 1][c + 1])
                + (kernel[1][0] * green[r][c - 1])
                + (kernel[1][1] * green[r][c])
                + (kernel[1][2] * green[r][c + 1])
                + (kernel[2][0] * green[r + 1][c - 1])
                + (kernel[2][1] * green[r + 1][c])
                + (kernel[0][0] * green[r + 1][c + 1])
            )
            redconv = (
                (kernel[0][0] * red[r - 1][c - 1])
                + (kernel[0][1] * red[r - 1][c])
                + (kernel[0][2] * red[r - 1][c + 1])
                + (kernel[1][0] * red[r][c - 1])
                + (kernel[1][1] * red[r][c])
                + (kernel[1][2] * red[r][c + 1])
                + (kernel[2][0] * red[r + 1][c - 1])
                + (kernel[2][1] * red[r + 1][c])
                + (kernel[0][0] * red[r + 1][c + 1])
            )

            b = int(Keepinrange(floor(blueconv))).to_bytes(1, "little")
            g = int(Keepinrange(floor(greenconv))).to_bytes(1, "little")
            r_ed = int(Keepinrange(floor(redconv))).to_bytes(1, "little")
            img.write(b)
            img.write(g)
            img.write(r_ed)
