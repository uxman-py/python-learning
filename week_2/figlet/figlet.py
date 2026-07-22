import sys
import pyfiglet
import random

all_fonts = pyfiglet.FigletFont.getFonts()

def main():
    

    if len(sys.argv) > 3: 
        print ("give 2 arguements for random font and 3 for a specific font")
        sys.exit()

    elif len(sys.argv) < 2:
        user = str(input("Input: "))
        font_name = random.choice(all_fonts)
        font = pyfiglet.Figlet(font = font_name)

        print(font.renderText(user))
    
    elif len(sys.argv) == 3:
        user = str(input("Input: "))
        font = pyfiglet.Figlet(font = sys.argv[2])

        print(font.renderText(user))
    
    
    


    
    
    

    
main()