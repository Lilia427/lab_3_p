import pyfiglet

def list_fonts():
    return pyfiglet.FigletFont.getFonts()

def is_valid_font(font_name):
    return font_name in list_fonts()
