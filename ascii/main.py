from sys import exit
from argparse import ArgumentParser
from mimetypes import guess_type

from ascii import Char, ColorVideo, GrayVideo, ColorImage, GrayImage, PixelImage, PixelVideo, Utils


class ArtConverter:

    def __init__(self):
        path = 0
        background = ""
        args = self.set_args()
        is_colored = args.colored or args.bg
        if args.bg: background = Utils.Utils.bg_rgb(0, 0, 0)
        if args.path != '0': path = args.path
        if path == 0 or guess_type(path)[0].split('/')[0] == "video":
            if is_colored:
                draw_class = ColorVideo.ColorVideo
            elif args.pixelart:
                draw_class = PixelVideo.PixelVideo
            else:
                draw_class = GrayVideo.GrayVideo
        else:
            if is_colored:
                draw_class = ColorImage.ColorImage
            elif args.pixelart:
                draw_class = PixelImage.PixelImage
            else:
                draw_class = GrayImage.GrayImage

        char = Char.Char(scale=args.scale, chars=args.chars)
        self.drawClass = draw_class(path=path, char=char, background=background)

    def run(self):
        # system('tput civis')
        print("\u001b[2J")
        print(f"\u001b[0;0H")
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
