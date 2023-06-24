from cv2 import transpose, cvtColor, COLOR_BGR2RGB, VideoCapture
from numba import njit

from Char import Char


@njit(fastmath=True)
def accelerate_conversion(image, width, height, gor_step, vert_step):
    strings = []
    for y in range(0, height, vert_step):
        string = ""
        for x in range(0, width, gor_step):
            r, g, b = image[x, y]
            string += f"\u001b[48;2;{r};{g};{b}m "
        strings.append(string)

    return strings


class PixelVideo:

    def __init__(self, path: str, char: Char, background: str) -> None:
        self.path = path
        self.char = char
        self.capture = VideoCapture(self.path)
        self.image = self.get_image()
        self.width, self.height = self.image.shape[0], self.image.shape[1]
        char.set_steps(self.width, self.height)

    def get_image(self):
        ret, cv2_image = self.capture.read()
        if not ret: exit()
        transposed_image = transpose(cv2_image)
        color_image = cvtColor(transposed_image, COLOR_BGR2RGB)

        return color_image

    def draw(self) -> None:
        while True:
            self.image = self.get_image()
            image = accelerate_conversion(
                self.image, self.width, self.height,
                self.char.gor_step, self.char.vert_step
            )

            print("\n".join(image))
            print(f"\u001b[0;0H")
