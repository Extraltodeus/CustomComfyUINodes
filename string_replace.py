class string_replace_class:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_input": ("STRING", {"multiline": True, "forceInput": True}),
                "replace_this": ("STRING", {"multiline": True}),
                "by_that": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "exec"
    CATEGORY = "utils"

    def exec(self, text_input, replace_this, by_that):
        return (text_input.replace(replace_this,by_that), )
            
NODE_CLASS_MAPPINGS = {
    "string_replace": string_replace_class,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "string_replace": "string_replace_node",
}