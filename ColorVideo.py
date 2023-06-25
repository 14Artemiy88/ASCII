from time import time, sleep

from cv2 import transpose, cvtColor, COLOR_BGR2GRAY, COLOR_BGR2RGB, VideoCapture
from numba import njit, typed

from Char import Char


@njit(fastmath=True)
def accelerate_conversion(image, gray_image, width, height, ascii_coef, gor_step, vert_step, ascii_chars, bg):
    strings = []
    ascii_chars_size = len(ascii_chars) - 1
    for y in range(0, height, vert_step):
        string = ""
        for x in range(0, width, gor_step):
            char_index = gray_image[x, y] // ascii_coef
            if char_index > ascii_chars_size: char_index = ascii_chars_size
            char = ascii_chars[char_index]
            r, g, b = image[x, y]
            string += bg + f"\u001b[38;2;{r};{g};{b}m{char}"
        strings.append(string)

    return strings


class ColorVideo:

    def __init__(self, path: str, char: Char, background: str) -> None:
        self.path = path
        self.background = background
        self.char = char
        self.ascii_chars = typed.List(self.char.ascii_chars)
        self.capture = VideoCapture(self.path)
        self.gray_image, self.color_image = self.get_image()
        self.width, self.height = self.gray_image.shape[0], self.gray_image.shape[1]
        char.set_steps(self.width, self.height)

    def get_image(self):
        ret, cv2_image = self.capture.read()
        if not ret: exit()
        transposed_image = transpose(cv2_image)
        gray_image = cvtColor(transposed_image, COLOR_BGR2GRAY)
        color_image = cvtColor(transposed_image, COLOR_BGR2RGB)

        return gray_image, color_image

    def draw(self) -> None:
        while True:
            self.gray_image, self.color_image = self.get_image()
            start = time()
            image = accelerate_conversion(
                self.color_image, self.gray_image, self.width, self.height,
                self.char.ascii_coef, self.char.gor_step, self.char.vert_step,
                self.ascii_chars, self.background
            )
            end = time() - start
            if end < .03: sleep(.03 - end)
            print("\n".join(image))
            print(f"\u001b[0;0H")
