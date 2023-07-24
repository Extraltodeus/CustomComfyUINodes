from PIL import Image
import numpy as np

class CLIPinterrogatorNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "interrogator": ("INTERROGATOR", {"forceInput": True}),
                    "image": ("IMAGE",),
                    "mode": (["best", "classic", "fast", "negative"], {"default": "best"})
                }}
    RETURN_TYPES = ("STRING",)
    FUNCTION = "image_to_prompt"
    CATEGORY = "conditioning"

    def image_to_prompt(self, interrogator, image, mode):
        ci = interrogator
        ci.config.chunk_size = 2048 if ci.config.clip_model_name == "ViT-L-14/openai" else 1024
        ci.config.flavor_intermediate_count = 2048 if ci.config.clip_model_name == "ViT-L-14/openai" else 1024

        i = 255. * image[0].cpu().numpy()
        image = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

        if mode == 'best':
            output = ci.interrogate(image)
        elif mode == 'classic':
            output = ci.interrogate_classic(image)
        elif mode == 'fast':
            output = ci.interrogate_fast(image)
        elif mode == 'negative':
            output = ci.interrogate_negative(image)
        return (output,)
    
NODE_CLASS_MAPPINGS = {
    "CLIPinterrogatorNode": CLIPinterrogatorNode
}