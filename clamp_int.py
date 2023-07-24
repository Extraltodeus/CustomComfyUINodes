class clamp_int_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_input": ("INT", {
                    "default": 1, 
                    "min": -1000000, #Minimum value
                    "max": 1000000, #Maximum value
                    "step": 1 #Slider's step
                }),
                "min_int": ("INT", {
                    "default": 1, 
                    "min": -1000000, #Minimum value
                    "max": 1000000, #Maximum value
                    "step": 1 #Slider's step
                }),
                "max_int": ("INT", {
                    "default": 1, 
                    "min": -1000000, #Minimum value
                    "max": 1000000, #Maximum value
                    "step": 1 #Slider's step
                }),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("INT_out",)

    FUNCTION = "clamp_int"

    CATEGORY = "Basic maths"

    def clamp_int(self, int_input, min_int, max_int):
        if int_input > max_int:
                int_input = max_int
        if int_input < min_int:
                int_input = min_int
        return (int_input,)
        
        
NODE_CLASS_MAPPINGS = {
    "clamp_int": clamp_int_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "clamp_int": "Simple clamp_int node"
}
