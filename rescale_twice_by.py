class rescale_twice_by_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "factor": ("FLOAT", {
                    "default": 2, 
                    "min": 0, #Minimum value
                    "max": 10, #Maximum value
                    "step": 0.5 #Slider's step
                }),
            }
        }

    RETURN_TYPES = ("FLOAT","FLOAT",)
    RETURN_NAMES = ("divided","multiplied",)

    FUNCTION = "simple_math"

    CATEGORY = "Basic maths"

    def simple_math(self, factor):
        return (1/factor,factor)
        
        
NODE_CLASS_MAPPINGS = {
    "Rescale twice by": rescale_twice_by_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Rescale twice by": "Rescale twice"
}
