from math import pi, cos
class simple_math_cosine_loop_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "n_loop": ("FLOAT", {"default": 1,"min": 0,"max": 100,"step": 0.1}),
                "value" : ("FLOAT", {"default": 1, "min": 0,"max": 1,"step": 0.1}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("loop_value",)

    FUNCTION = "simple_math"
    CATEGORY = "Basic maths"

    def simple_math(self, n_loop, value):
        z = cos(2 * pi * n_loop * value)
        z = (1 - z) / 2
        return (z,)
        
        
NODE_CLASS_MAPPINGS = {
    "cosine_loop": simple_math_cosine_loop_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "cosine_loop": "cosine_loop_node"
}
