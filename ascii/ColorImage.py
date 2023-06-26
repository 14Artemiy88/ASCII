from ascii import Char, Utils
from cv2 import transpose, cvtColor, imread, COLOR_BGR2GRAY, COLOR_RGB2BGR


class ColorImage:

    def __init__(self, path: str, char: Char, background: str) -> None:
        self.path = path
        self.background = background
        self.char = char
        self.gray_image, self.color_image = self.get_image()
        self.width, self.height = self.color_image.shape[0], self.color_image.shape[1]
        char.set_steps(self.width, self.height)

    def get_image(self):
        cv2_image = imread(self.path)
        transposed_image = transpose(cv2_image)
        gray_image = cvtColor(transposed_image, COLOR_BGR2GRAY)
        color_image = cvtColor(transposed_image, COLOR_RGB2BGR)

        return gray_image, color_image

    def draw(self) -> None:
        char_indices = self.gray_image // int(self.char.ascii_coef)
        image = []
        for y in range(0, self.height, self.char.vert_step):
            string = ""
            for x in range(0, self.width, self.char.gor_step):
                char_index = char_indices[x, y]
                char = self.char.get_char(color=char_index)
                color = tuple(self.color_image[x, y])
                string += self.background + Utils.fg_rgb(int(color[0]), int(color[1]), int(color[2])) + char
            image.append(string)
        print("\n".join(image))
