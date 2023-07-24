class int_to_fixed_lengthSTR_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "num": ("INT", {"default": 1, "min": 0,"max": 1000000,"step": 1}),
                "length":  ("INT", {"default": 5,"min": 1,"max": 16,"step": 1})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STR_out",)

    FUNCTION = "convert_to_fixed_width_string"

    CATEGORY = "Basic maths"

    def convert_to_fixed_width_string(self, num, length):
        str_num = str(num)
        if len(str_num) < length:
            str_num = str_num.zfill(length)
        elif len(str_num) > length:
            str_num = str_num[:length]
        return (str_num,)
     
NODE_CLASS_MAPPINGS = {
    "int_to_fixed_lengthSTR": int_to_fixed_lengthSTR_class
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "int_to_fixed_lengthSTR": "int_to_fixed_lengthSTR node"
}
