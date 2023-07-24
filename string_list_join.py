# class string_list_join_class:
#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                 "string_list_input": ("STRING", {"forceInput": True}),
#                 "split_char": ("STRING", {"multiline": True}),
#                 "join_char": ("STRING", {"multiline": True})
#             }
#         }

#     RETURN_TYPES = ("STRING",)
#     FUNCTION = "exec"
#     CATEGORY = "utils"

#     def exec(self, string_list_input, split_char, join_char):
#         string_list_input = string_list_input.split(split_char)
#         return (join_char.join(string_list_input),)
            
# NODE_CLASS_MAPPINGS = {
#     "string_list_join": string_list_join_class,
# }

# NODE_DISPLAY_NAME_MAPPINGS = {
#     "string_list_join": "string_list_join_node",
# }


class string_list_join_class:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string_list_input": ("LIST", {"forceInput": True}),
                "join_char": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "exec"
    CATEGORY = "utils"

    def exec(self, string_list_input, join_char):
        return (join_char.join(string_list_input),)
            
NODE_CLASS_MAPPINGS = {
    "string_list_join": string_list_join_class,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "string_list_join": "string_list_join_node",
}