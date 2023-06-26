class Utils:
    @staticmethod
    def dd(*param):
        print(param)
        exit()

    @staticmethod
    def bg_rgb(r, g, b): return f"\u001b[48;2;{r};{g};{b}m"

    @staticmethod
    def fg_rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"
