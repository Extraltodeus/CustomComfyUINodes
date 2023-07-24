from clip_interrogator import Config, Interrogator

class CLIPinterrogatorLoaderNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "clip_model_name": (["ViT-L-14/openai", "ViT-H-14/laion2b_s32b_b79k"], {"default": "ViT-L-14/openai"}),
                    "caption_model_name": (["blip-base", "blip-large", "git-large-coco","blip2-2.7b"], {"default": "blip-large"})
                }}
    RETURN_TYPES = ("INTERROGATOR",)
    FUNCTION = "return_model"

    CATEGORY = "conditioning"

    def return_model(self, clip_model_name, caption_model_name):
        config = Config()
        config.clip_model_name = clip_model_name
        config.caption_model_name = caption_model_name
        ci = Interrogator(config)
        return (ci,)
    
NODE_CLASS_MAPPINGS = {
    "CLIPinterrogatorLoaderNode": CLIPinterrogatorLoaderNode
}

