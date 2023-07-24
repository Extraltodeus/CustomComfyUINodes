# class string_split_class:
#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                 "text_input": ("STRING", {"multiline": True, "forceInput": True}),
#                 "split_char": ("STRING", {"multiline": True}),
#                 "index":  ("INT", {"default": 0,"min": 0,"max": 50,"step": 1})
#             }
#         }

#     RETURN_TYPES = ("STRING",)
#     FUNCTION = "exec"
#     CATEGORY = "utils"

#     def exec(self, text_input, split_char, index):
#         try:
#             output = text_input.split(split_char)[index]
#         except:
#             output = text_input
#         return (output,)
            
# NODE_CLASS_MAPPINGS = {
#     "string_split": string_split_class,
# }

# NODE_DISPLAY_NAME_MAPPINGS = {
#     "string_split": "string_split_node",
# }

class string_split_class:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_input": ("STRING", {"multiline": True, "forceInput": True}),
                "split_char": ("STRING", {"multiline": True}),
                "index":  ("INT", {"default": 0,"min": 0,"max": 50,"step": 1})
            }
        }

    RETURN_TYPES = ("STRING","LIST",)
    FUNCTION = "exec"
    CATEGORY = "utils"

    def exec(self, text_input, split_char, index):
        try:
            string_list = text_input.split(split_char)
            output = string_list[index]
        except:
            string_list = []
            output = text_input
        return (output,string_list,)
            
NODE_CLASS_MAPPINGS = {
    "string_split": string_split_class,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "string_split": "string_split_node",
}