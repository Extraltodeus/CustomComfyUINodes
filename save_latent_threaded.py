import folder_paths
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import os
import json
import threading
import numpy as np
import comfy.utils
import torch

class SaveLatentThreaded_class:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""

    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    {
                     "samples": ("LATENT", ),
                     "filename_prefix": ("STRING", {"default": "ComfyUI"}),
                     "output_dir": ("STRING", {"default": """D:\StableDiffusion\workingwebui\comfyui\input"""})
                     },
                "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
                }

    RETURN_TYPES = ()
    FUNCTION = "save_latents"

    OUTPUT_NODE = True

    CATEGORY = "latent"


    def save_latents(self, *args, **kwargs):
        thread = threading.Thread(target=self.save_latents_threaded, args=args, kwargs=kwargs)
        thread.start()
        return ()

    def save_latents_threaded(self, samples, filename_prefix="ComfyUI", output_dir="input", prompt=None, extra_pnginfo=None):
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, output_dir)

        # support save metadata for latent sharing
        prompt_info = ""
        if prompt is not None:
            prompt_info = json.dumps(prompt)

        metadata = {"prompt": prompt_info}
        if extra_pnginfo is not None:
            for x in extra_pnginfo:
                metadata[x] = json.dumps(extra_pnginfo[x])

        file = f"{filename}_{counter:05}_.latent"
        file = os.path.join(full_output_folder, file)

        output = {}
        output["latent_tensor"] = samples["samples"]
        output["latent_format_version_0"] = torch.tensor([])

        comfy.utils.save_torch_file(output, file, metadata=metadata)
        return {}
    
NODE_CLASS_MAPPINGS = {
    "SaveLatentThreaded": SaveLatentThreaded_class,
}
