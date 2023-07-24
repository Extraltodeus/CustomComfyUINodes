
class simple_math_float_out_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "float_input_1": ("FLOAT", {
                    "default": 1, 
                    "min": -1000000, #Minimum value
                    "max": 100000, #Maximum value
                    "step": 1 #Slider's step
                }),
                "float_input_2": ("FLOAT", {
                    "default": 1, 
                    "min": -1000000, #Minimum value
                    "max": 1000000, #Maximum value
                    "step": 1 #Slider's step
                }),
            "math_operation": (["add", "sub", "mult", "div"],)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT_out",)

    FUNCTION = "simple_math"

    CATEGORY = "Basic maths"

    def simple_math(self, float_input_1, float_input_2, math_operation):
        if math_operation == "add":
            result = float_input_1+float_input_2
        if math_operation == "sub":
            result = float_input_1-float_input_2
        if math_operation == "mult":
            result = float_input_1*float_input_2
        if math_operation == "div":
            result = float_input_1/float_input_2
        return (result,)
        
        
NODE_CLASS_MAPPINGS = {
    "Simple math FLOAT out 2x1": simple_math_float_out_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Simple math FLOAT": "Simple math FLOAT node"
}
