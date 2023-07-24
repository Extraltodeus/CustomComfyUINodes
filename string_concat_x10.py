
class StringConcat_x10_class:
    @classmethod
    def INPUT_TYPES(s):
        dynamic_entries = {f"text_{x+1}": ("STRING", {"multiline": True}) for x in range(10)}
        return {
            "required": {
                "tidy_tags": (["yes", "no"], {"default": "no"}),
            },
            "optional": {
                **dynamic_entries
            }
        }


    RETURN_TYPES = ("STRING",)
    FUNCTION = "exec"
    CATEGORY = "utils"

    def exec(self, tidy_tags, text_1="", text_2="", text_3="", text_4="", text_5="", text_6="", text_7="", text_8="", text_9="", text_10=""):
        out = ""
        out = ("_" if tidy_tags == "yes" else "").join(filter(None, [text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9, text_10]))
        return (out, )
            
NODE_CLASS_MAPPINGS = {
    "StringConcat_x10": StringConcat_x10_class,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringConcat_x10": "String Concat X10",
}
