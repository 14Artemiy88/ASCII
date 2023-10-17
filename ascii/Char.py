class Char:
    # ascii_chars = [' ', '.', ':', '!', '/', 'r', '(', 'l', '1', 'Z', '4', 'H', '9', 'W', '8', '$', '@']
    ascii_chars ="   ...',;:clodxkO0KXNWM"

    def __init__(self, scale: float, chars: str | None) -> None:
        if chars: self.ascii_chars = chars
        self.scale = scale
        self.ascii_chars_size = len(self.ascii_chars) - 1
        self.ascii_coef = 255 // (len(self.ascii_chars))

    def set_steps(self, width: int, height: int) -> None:
        if width >= height:
            coaff = width // height * .6
        else:
            coaff = height // width * .6
        vert = width
        gor = coaff * width
        self.vert_step = max(1, int(vert // self.scale * 2))
        self.gor_step = max(1, int(gor // self.scale * 2))

    def get_char(self, color: int) -> str:
        if color > self.ascii_chars_size:
            color = self.ascii_chars_size

        return self.ascii_chars[color]

    @staticmethod
    def bg_rgb(r, g, b): return f"\u001b[48;2;{r};{g};{b}m"

    @staticmethod
    def fg_rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"
