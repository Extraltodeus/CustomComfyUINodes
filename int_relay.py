class simple_math_int_relay_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_input_1": ("INT", {
                    "default": 1, 
                    "min": 0, #Minimum value
                    "max": 1000000, #Maximum value
                    "step": 1 #Slider's step
                }),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("INT_out",)

    FUNCTION = "simple_math"

    CATEGORY = "Basic maths"

    def simple_math(self, int_input_1):
        return (int_input_1,)
        
        
NODE_CLASS_MAPPINGS = {
    "Simple INT relay": simple_math_int_relay_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Simple INT relay": "Simple INT relay node"
}
