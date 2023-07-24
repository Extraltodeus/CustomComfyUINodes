import os
import safetensors.torch

class load_latent_from_str_class:
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "filename": ("STRING", {"default": "ComfyUI"}),
                    "output_dir": ("STRING", {"default": """D:\StableDiffusion\workingwebui\comfyui\input"""})
                    }
                }

    CATEGORY = "latent"
    RETURN_TYPES = ("LATENT", )
    FUNCTION = "load"

    def load(self, filename, output_dir):
        latent_path = os.path.join(output_dir,filename)
        latent = safetensors.torch.load_file(latent_path, device="cpu")
        multiplier = 1.0
        if "latent_format_version_0" not in latent:
            multiplier = 1.0 / 0.18215
        samples = {"samples": latent["latent_tensor"].float() * multiplier}
        return (samples, )
    
NODE_CLASS_MAPPINGS = {
    "load_latent_from_str": load_latent_from_str_class,
}