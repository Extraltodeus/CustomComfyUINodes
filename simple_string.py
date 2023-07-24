class simple_string_output_class:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_a": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "exec"
    CATEGORY = "utils"

    def exec(self, text_a):
        return (text_a, )
            
NODE_CLASS_MAPPINGS = {
    "simple_string_output": simple_string_output_class,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "simple_string_output": "simple_string_output_node",
}