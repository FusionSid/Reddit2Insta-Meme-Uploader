# from sidspackage

colors = {
    # Colors
    "red": "\033[91m",
    "yellow": "\033[93m",
    "green": "\033[92m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
    "magenta": "\u001b[35m",
    "purple": "\033[95m",
    "black": "\u001b[30m",
    # Effects
    "reset": "\u001b[0m",
    "bold": "\033[1m",
    "underline": "\033[4m",
}


class ColorPrint:
    class colorNotFound(Exception):
        def __init__(
            self,
            color,
            message=f"Color not found. You can choose from the following list of colors -\n{', '.join([key.capitalize() for key in colors.keys()])}\nOr you can do ColorPrint().help for more information and an example of usage.",
        ):
            self.color = color
            self.message = message
            super().__init__(self.message)

        def __str__(self):
            return f"{self.color} -> {self.message}"

    def print(self, text, color=None):
        if color is None:
            print(text)
            return
        color = color.lower()
        try:
            color = colors[color]
            reset = colors["reset"]
            print(f"{color}{text}{reset}")
        except KeyError:
            raise self.colorNotFound(color)

    @property
    def help(self):
        reset = colors["reset"]
        print(
            f"---- List of Colors ----\n{', '.join(f'{color}{name.capitalize()}{reset}' for name, color in colors.items())}\n\n---- Usage ----\n>>> c = ColorPrint()\n>>> c.print('text', color=Optional[str])\n>>> c.print('Hello World', color='green')\n{colors['green']}Hello World{colors['reset']}"
        )
