from math import sin, cos, tan
class simple_math_trig_class:
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
                    "step": 0.1 #Slider's step
                }),
            "math_operation": (["sin", "cos", "tan"],)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT_out",)

    FUNCTION = "simple_math"

    CATEGORY = "Basic maths"

    def simple_math(self, float_input_1, math_operation):
        if math_operation == "sin":
            result = sin(float_input_1)
        elif math_operation == "cos":
            result = cos(float_input_1)
        elif math_operation == "tan":
            result = tan(float_input_1)
        return (result,)
        
        
NODE_CLASS_MAPPINGS = {
    "Simple_math_trig": simple_math_trig_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Simple_math_trigonometry": "Simple_math_trigonometry_node"
}
