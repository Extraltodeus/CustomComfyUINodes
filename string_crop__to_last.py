class string_crop_last_class:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_input": ("STRING", {"multiline": True, "forceInput": True}),
                "split_char": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "exec"
    CATEGORY = "utils"

    def exec(self, text_input, split_char):
        try:
            last_dot_index = text_input.rfind(split_char)
            output = text_input[:last_dot_index + 1]
        except:
            output = text_input
        return (output,)
            
NODE_CLASS_MAPPINGS = {
    "string_crop_last": string_crop_last_class,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "string crop to last": "string_crop_last_node",
}