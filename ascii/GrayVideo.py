from time import sleep, time

from cv2 import transpose, cvtColor, COLOR_BGR2GRAY, VideoCapture
from numba import njit, typed

from ascii.Char import Char


@njit(fastmath=True)
def accelerate_conversion(gray_image, width, height, ascii_coef, gor_step, vert_step, ascii_chars, ascii_chars_size):
    strings = []
    for y in range(0, height, vert_step):
        chars = ""
        for x in range(0, width, gor_step):
            char_index = gray_image[x, y] // ascii_coef
            if char_index > ascii_chars_size:
                char_index = ascii_chars_size
            chars += ascii_chars[char_index]
        strings.append(chars)

    return strings


class GrayVideo:

    def __init__(self, path: str, char: Char, background: str) -> None:
        self.path = path
        self.char = char
        self.ascii_chars = typed.List(self.char.ascii_chars)
        self.capture = VideoCapture(self.path)
        self.image = self.get_image()
        self.width, self.height = self.image.shape[0], self.image.shape[1]
        char.set_steps(self.width, self.height)

    def get_image(self):
        ret, cv2_image = self.capture.read()
        if not ret: exit()
        transposed_image = transpose(cv2_image)

        return cvtColor(transposed_image, COLOR_BGR2GRAY)

    def draw(self) -> None:
        while True:
            self.image = self.get_image()
            start = time()
            strings = accelerate_conversion(
                self.image, self.width, self.height, self.char.ascii_coef,
                self.char.gor_step, self.char.vert_step, self.ascii_chars, self.char.ascii_chars_size
            )
            print("\n".join(strings))
            print(f"\u001b[0;0H")
            end = time() - start
            if end < .03: sleep(.03 - end)
