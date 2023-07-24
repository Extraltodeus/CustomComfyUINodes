# class string_list_append_class:
#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                 "string_list_input": ("STRING", {"forceInput": True}),
#                 "string_input": ("STRING", {"multiline": True}),
#                 "splitjoin_char": ("STRING", {"multiline": True}),
#                 "max_len":  ("INT", {"default": 10,"min": 0,"max": 1000,"step": 1})
#             }
#         }

#     RETURN_TYPES = ("STRING",)
#     FUNCTION = "exec"
#     CATEGORY = "utils"

#     def exec(self, string_list_input, string_input, splitjoin_char, max_len):
#         string_list_input = string_list_input.split(splitjoin_char)
#         string_list_input.append(string_input)
#         string_list_input=string_list_input[-max_len:]
#         string_list_input=splitjoin_char.join(string_list_input)
#         return (string_list_input,)
            
# NODE_CLASS_MAPPINGS = {
#     "string_list_append": string_list_append_class,
# }

# NODE_DISPLAY_NAME_MAPPINGS = {
#     "string_list_append": "string_list_append_node",
# }

class string_list_append_class:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "max_len":  ("INT", {"default": 10,"min": 0,"max": 1000,"step": 1})
            },
            "optional": {
                "string_list_input": ("LIST", {"forceInput": True}),
                "string_input": ("STRING", {"multiline": True, "forceInput": True})
            }
        }

    RETURN_TYPES = ("LIST",)
    FUNCTION = "exec"
    CATEGORY = "utils"

    def exec(self, max_len, string_list_input=[], string_input=""):
        string_list_input.append(string_input)
        string_list_input=string_list_input[-max_len:]
        return (string_list_input,)
            
NODE_CLASS_MAPPINGS = {
    "string_list_append": string_list_append_class,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "string_list_append": "string_list_append_node",
}