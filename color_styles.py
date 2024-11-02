from colorama import Fore, Style

def apply_color(text, color):
    colors = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'blue': Fore.BLUE,
        'yellow': Fore.YELLOW,
        'cyan': Fore.CYAN,
        'magenta': Fore.MAGENTA,
        'white': Fore.WHITE
    }
    color_code = colors.get(color.lower(), Fore.WHITE)
    return f"{color_code}{text}{Style.RESET_ALL}"

def list_colors():
    return ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white']
