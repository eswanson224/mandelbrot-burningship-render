import numpy as np
from PIL import Image
from numba import jit, vectorize

np.warnings.filterwarnings('ignore')


@vectorize
def mandelbrot(c, n):
    z = 0
    for i in range(n):
        z = z ** 2 + c
        if abs(z) > 2:
            return i
    return n


@vectorize
def burning_ship(c, n):
    z = 0
    con = 0
    for i in range(n):
        z = (abs(z.real) + abs(z.imag) * 1j) ** 2 + c
        if abs(z) > 2:
            return i
    return n


def render_mandelbrot(xmin, ymin, xmax, ymax, width, height, iter):
    arrR, arrI = np.meshgrid(np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height), sparse=True)
    points = arrR + arrI * 1j

    matrix = mandelbrot(points, iter)
    matrix = matrix / iter * 255 % 255
    matrix = np.ndarray.astype(matrix, np.uint8)
    image = Image.fromarray(matrix, mode='L')
    return image
    

def render_burning_ship(xmin, ymin, xmax, ymax, width, height, iter):
    arrR, arrI = np.meshgrid(np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height), sparse=True)
    points = arrR + arrI * 1j

    matrix = burning_ship(points, iter)
    matrix = matrix / iter * 255 % 255
    matrix = np.ndarray.astype(matrix, np.uint8)
    image = Image.fromarray(matrix, mode='L')
    return image


if __name__ == "__main__":
    width = height = 800
    iter = 100
    xmin, xmax = -2, 0.5
    ymin, ymax = -1.25, 1.25
    
    render = ""
    while render != "mandelbrot" and render != "burning ship":
        render = input("Fractal (mandelbrot or burning ship): ").lower()

    if render == "mandelbrot":
        custom = input("Would you like to enter custom perameters? (y or n): ")
        if custom == 'y':
            width = int(input("Image Width (default 800): "))
            height = int(input("Image Height (default 800): "))
            iter = int(input("Iterations (default 100): "))
            xmin = float(input("xmin (default -2): "))
            ymin = float(input("ymin (default -1.25): "))
            xmax = float(input("xmax (default 0.5): "))
            ymax = float(input("ymax (default 1.25): "))
        img = render_mandelbrot(xmin, ymin, xmax, ymax, width, height, iter)
    else:
        xmin, xmax = -1.8, -1.7
        ymin, ymax = -.08, .01
        custom = input("Would you like to enter custom perameters? (y or n): ")
        if custom == 'y':
            width = int(input("Image Width (default 800): "))
            height = int(input("Image Height (default 800): "))
            iter = int(input("Iterations (default 100): "))
            xmin = float(input("xmin (default -1.8): "))
            ymin = float(input("ymin (default -0.08): "))
            xmax = float(input("xmax (default -1.7): "))
            ymax = float(input("ymax (default 0.01): "))
        img = render_burning_ship(xmin, ymin, xmax, ymax, width, height, iter)
    
    img.show()
    save = input("Would you like to save the image? (y or n): ")
    if save == 'y':
        name = input('File name ("input".png): ')
        img.save(f"{name}.png")