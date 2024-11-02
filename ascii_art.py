import pyfiglet
from art import text2art

def generate_ascii_art(text, font='slant', symbol=None, width=80):
    try:
        if symbol:
            ascii_art = text2art(text, chr_ignore=True)
            ascii_art = ascii_art.replace('*', symbol)
        else:
            figlet = pyfiglet.Figlet(font=font, width=width)
            ascii_art = figlet.renderText(text)
        return ascii_art
    except pyfiglet.FontNotFound:
        return f"Font '{font}' not found. Please select another font."

def get_available_fonts():
    return pyfiglet.FigletFont.getFonts()

def save_ascii_art(ascii_art, filename="output/saved_art.txt"):
    with open(filename, 'w') as file:
        file.write(ascii_art)
    print(f"ASCII art saved to file: {filename}")
