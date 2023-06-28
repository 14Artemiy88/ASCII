from cv2 import transpose, cvtColor, imread, COLOR_BGR2GRAY

from ascii.Char import Char


class GrayImage:

    def __init__(self, path: str, char: Char, background: str) -> None:
        self.path = path
        self.char = char
        self.image = self.get_image()
        self.width, self.height = self.image.shape[0], self.image.shape[1]
        char.set_steps(self.width, self.height)

    def get_image(self):
        cv2_image = imread(self.path)
        transposed_image = transpose(cv2_image)

        return cvtColor(transposed_image, COLOR_BGR2GRAY)

    def draw(self) -> None:
        char_indices = self.image // int(self.char.ascii_coef)
        for y in range(0, self.height, self.char.vert_step):
            string = ""
            for x in range(0, self.width, self.char.gor_step):
                char_index = char_indices[x, y]
                string += self.char.get_char(color=char_index)
            print(string)
