from os import system
from sys import exit
from argparse import ArgumentParser
from mimetypes import guess_type

from ascii.Char import Char
from ascii.ColorVideo import ColorVideo
from ascii.GrayVideo import GrayVideo
from ascii.ColorImage import ColorImage
from ascii.GrayImage import GrayImage
from ascii.PixelImage import PixelImage
from ascii.PixelVideo import PixelVideo


class ArtConverter:

    def __init__(self):
        args = self.set_args()
        is_colored = args.colored or args.bg
        background = "" if not args.bg else Char.bg_rgb(0, 0, 0)
        path = 0 if args.path == '0' else args.path
        if path == 0 or guess_type(path)[0].split('/')[0] == "video":
            if is_colored:
                draw_class = ColorVideo
            elif args.pixelart:
                draw_class = PixelVideo
            else:
                draw_class = GrayVideo
        else:
            if is_colored:
                draw_class = ColorImage
            elif args.pixelart:
                draw_class = PixelImage
            else:
                draw_class = GrayImage

        char = Char(scale=args.scale, chars=args.chars)
        self.drawClass = draw_class(path=path, char=char, background=background)

    def run(self):
        # system('tput civis')
        system("clear")
        print(f"\u001b[1;1H")
        self.drawClass.draw()
        # system('tput cnorm')

    @staticmethod
    def set_args():
        parser = ArgumentParser()

        parser.add_argument('path', help="Path to file, 0 for webcam video")
        parser.add_argument('-s', "--scale", help="Scale, default 70", default=70, type=float)
        parser.add_argument('-ch', "--chars", help="Chars")

        group = parser.add_mutually_exclusive_group()
        group.add_argument('-c', "--colored", help="Colored, default false", action="store_true", default=False)
        group.add_argument('-b', "--bg", help="Black background with colored image, default false",
                           action="store_true", default=False)
        group.add_argument('-p', "--pixelart", help="Pixelart style, default false", action="store_true", default=False)

        return parser.parse_args()


def main():
    app = ArtConverter()
    app.run()


if __name__ == "__main__":
    exit(main())
