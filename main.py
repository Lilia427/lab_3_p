import os
from font_styles import list_fonts, is_valid_font
from color_styles import apply_color, list_colors
from ascii_art import generate_ascii_art, save_ascii_art
from preview import preview_ascii_art
import config

def main():
    print("Welcome to the ASCII Art Generator!")
    
    text = input("Enter the text you want to convert to ASCII Art: ")

    print("\nAvailable fonts:")
    fonts = list_fonts()
    print(", ".join(fonts))
    font = input("Choose a font from the list above (or press Enter for default): ")
    if not font or not is_valid_font(font):
        font = config.DEFAULT_FONT
        print(f"Using default font: {font}")

    print("\nAvailable colors:")
    colors = list_colors()
    print(", ".join(colors))
    color = input("Choose a color from the list above (or press Enter for default): ")
    if color.lower() not in colors:
        color = config.DEFAULT_COLOR
        print(f"Using default color: {color}")

    symbol = input("Enter a symbol to use in ASCII Art (optional, press Enter to skip): ")
    if not symbol:
        symbol = config.DEFAULT_SYMBOL

    width = input(f"Enter the width for ASCII Art (default is {config.DEFAULT_WIDTH}): ")
    if not width.isdigit():
        width = config.DEFAULT_WIDTH
    else:
        width = int(width)

    ascii_art = generate_ascii_art(text, font=font, symbol=symbol, width=width)
    colored_ascii_art = apply_color(ascii_art, color)
    
    preview_ascii_art(colored_ascii_art)

    save = input("Do you want to save this ASCII Art? (y/n): ")
    if save.lower() == 'y':
        filename = input(f"Enter filename (default is {config.DEFAULT_OUTPUT_FILE}): ")
        if not filename:
            filename = config.DEFAULT_OUTPUT_FILE
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        save_ascii_art(colored_ascii_art, filename)
        print(f"ASCII Art saved to {filename}")
    else:
        print("ASCII Art was not saved.")

if __name__ == "__main__":
    main()
