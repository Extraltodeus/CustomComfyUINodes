class int_modulo_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_input": ("INT", {"default": 1, "min": 0,"max": 1000000,"step": 1}),
                "int_modulo": ("INT", {"default": 24, "min": 1,"max": 1000000,"step": 1}),
                "if_equal_return_equal": ("INT", {"default": 1, "min": 0,"max": 1,"step": 1}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("INT_out",)

    FUNCTION = "simple_modulo"

    CATEGORY = "Basic maths"

    def simple_modulo(self, int_input, int_modulo, if_equal_return_equal):
        if if_equal_return_equal == 1 and int_input == int_modulo:
            return (int_input,)
        return (int_input%int_modulo,)
        
        
NODE_CLASS_MAPPINGS = {
    "int_modulo": int_modulo_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "int_modulo": "int_modulo node"
}
