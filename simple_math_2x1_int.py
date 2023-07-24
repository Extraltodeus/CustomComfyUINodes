from math import ceil, floor
class simple_math_int_out_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_input_1": ("INT", {
                    "default": 1, 
                    "min": -1000000, #Minimum value
                    "max": 1000000, #Maximum value
                    "step": 1 #Slider's step
                }),
                "int_input_2": ("INT", {
                    "default": 1, 
                    "min": -1000000, #Minimum value
                    "max": 1000000, #Maximum value
                    "step": 1 #Slider's step
                }),
            "math_operation": (["add", "sub", "mult", "div"],),
            "round_to": (["near", "floor", "ceil"],),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("INT_out",)

    FUNCTION = "simple_math"

    CATEGORY = "Basic maths"

    def simple_math(self, int_input_1, int_input_2, math_operation, round_to):
        if math_operation == "add":
            result = int_input_1+int_input_2
        if math_operation == "sub":
            result = int_input_1-int_input_2
        if math_operation == "mult":
            result = int_input_1*int_input_2
        if math_operation == "div":
            result = int_input_1/int_input_2
        if round_to == "near":
            result = round(result,0)
        if round_to == "floor":
            result = floor(result)
        if round_to == "ceil":
            result = ceil(result)
        return (int(result),)
        
        
NODE_CLASS_MAPPINGS = {
    "Simple math INT 2x1": simple_math_int_out_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Simple math INT": "Simple INT math node"
}
