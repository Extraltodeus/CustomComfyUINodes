
class remap_range_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("FLOAT", {"default": 1, "min": -1000000,"max": 1000000,"step": 0.1}),
                "minIn": ("FLOAT", {"default": 0, "min": -1000000,"max": 1000000,"step": 0.1}),
                "MaxIn": ("FLOAT", {"default": 1, "min": -1000000,"max": 1000000,"step": 0.1}),
                "minOut": ("FLOAT", {"default": 0, "min": -1000000,"max": 1000000,"step": 0.1}),
                "maxOut": ("FLOAT", {"default": 1, "min": -1000000,"max": 1000000,"step": 0.1}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("val_out",)

    FUNCTION = "remap_range"
    CATEGORY = "Basic maths"

    def remap_range(self, value, minIn, MaxIn, minOut, maxOut):
                if value > MaxIn: value = MaxIn;
                if value < minIn: value = minIn;
                finalValue = ((value - minIn) / (MaxIn - minIn)) * (maxOut - minOut) + minOut;
                return (finalValue,)
        
NODE_CLASS_MAPPINGS = {
    "remap_range": remap_range_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Remap range": "Remap range node"
}
