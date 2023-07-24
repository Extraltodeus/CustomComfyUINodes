from math import pi as π
class simple_math_π_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "π_divider": ("FLOAT", {
                    "default": 1, 
                    "min": -10, #Minimum value
                    "max": 10, #Maximum value
                    "step": 1 #Slider's step
                })
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("π",)

    FUNCTION = "simple_math"

    CATEGORY = "Basic maths"

    def simple_math(self, π_divider):
        result = π / π_divider
        return (result,)
        
        
NODE_CLASS_MAPPINGS = {
    "π": simple_math_π_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "π": "π"
}
