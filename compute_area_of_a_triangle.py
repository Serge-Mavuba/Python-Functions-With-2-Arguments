import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#TO COMPUTE THE AREA WE NEED TO ARGUMENTS THE BASE (b) AND THE HEIGHT (h)
def triangle_area(b,h):
    """Returns the value of a triangle with base b and height h."""
    return 0.5 * b * h
    
triangle_area(3,6)
print(Fore.GREEN + Style.BRIGHT + str(triangle_area(3,6)))
