class simple_wildcards_class:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "wildcards": ("STRING", {"multiline": True, "default": "word1|word2|word3"}),
                "word_to_replace": ("STRING", {"multiline": True, "default": "keyword to replace"}),
                "text_input": ("STRING", {"multiline": True, "default": "original text here"}),
                "selection_index": ("INT", {"default": 0, "min": 0,"max": 1000,"step": 1}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "exec"
    CATEGORY = "utils"

    def exec(self, wildcards,text_input,word_to_replace,selection_index):
        wild_cards  = wildcards.split("|")
        idx_mod = selection_index % len(wild_cards)
        text_input  = text_input.replace(word_to_replace,wild_cards[idx_mod])
        return (text_input,)
            
NODE_CLASS_MAPPINGS = {
    "simple_wildcards": simple_wildcards_class,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "simple_wildcards(\"|\" separated)": "simple_wildcards_node",
}
