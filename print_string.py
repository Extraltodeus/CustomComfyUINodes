from colorama import Fore, Style

class print_string_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string_input": ("STRING", {"multiline": True, "dynamicPrompts": False, "forceInput": True}),
                "print_color": (["GREEN", "WHITE", "RED", "YELLOW", "BLUE", "MAGENTA", "CYAN"],)
            }
        }

    FUNCTION = "simple_print"
    RETURN_TYPES = ("STRING",)
    CATEGORY = "utils"

    def simple_print(self, string_input, print_color):
        color_mapping = {
            "BLACK": Fore.BLACK,
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,
            "WHITE": Fore.WHITE,
            "RESET": Fore.RESET
        }
        print("Print node :",f"{color_mapping[print_color]}{string_input}{Fore.RESET}")
        return (string_input,)
        
NODE_CLASS_MAPPINGS = {
    "print_string": print_string_class
}
