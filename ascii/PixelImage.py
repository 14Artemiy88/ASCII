from ascii import Char
from ascii import Utils
from cv2 import transpose, cvtColor, imread, COLOR_RGB2BGR


class PixelImage:

    def __init__(self, path: str, char: Char, background: str) -> None:
        self.path = path
        self.char = char
        self.image = self.get_image()
        self.width, self.height = self.image.shape[0], self.image.shape[1]
        char.set_steps(self.width, self.height)

    def get_image(self):
        cv2_image = imread(self.path)
        transposed_image = transpose(cv2_image)

        return cvtColor(transposed_image, COLOR_RGB2BGR)

    def draw(self) -> None:
        image = []
        for y in range(0, self.height, self.char.vert_step):
            string = ""
            for x in range(0, self.width, self.char.gor_step):
                color = tuple(self.image[x, y])
                string += Utils.Utils.bg_rgb(int(color[0]), int(color[1]), int(color[2])) + " "
            image.append(string)
        print("\n".join(image))
