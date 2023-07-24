import folder_paths
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import os
import json
import threading
import numpy as np
class SaveImageThreaded_class:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""

    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    {"images": ("IMAGE", ),
                     "filename_prefix": ("STRING", {"default": "ComfyUI"}),
                     "save_bool": ("INT", {"default": 1, "min": 0,"max": 1,"step": 1})
                     },
                     
                "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
                }

    RETURN_TYPES = ()
    FUNCTION = "save_images"

    OUTPUT_NODE = True

    CATEGORY = "image"


    def save_images(self, *args, **kwargs):
        thread = threading.Thread(target=self.save_images_threaded, args=args, kwargs=kwargs)
        thread.start()
        return ()

    def save_images_threaded(self, images, filename_prefix="ComfyUI", save_bool=1, prompt=None, extra_pnginfo=None):
        if save_bool != 1: return ()
        filename_prefix += self.prefix_append
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir, images[0].shape[1], images[0].shape[0])
        results = list()
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = PngInfo()
            if prompt is not None:
                metadata.add_text("prompt", json.dumps(prompt))
            if extra_pnginfo is not None:
                for x in extra_pnginfo:
                    metadata.add_text(x, json.dumps(extra_pnginfo[x]))

            file = f"{filename}_{counter:05}_.png"
            img.save(os.path.join(full_output_folder, file), pnginfo=metadata, compress_level=4)
            results.append({
                "filename": file,
                "subfolder": subfolder,
                "type": self.type
            })
            counter += 1

        return { "ui": { "images": results } }
    
NODE_CLASS_MAPPINGS = {
    "SaveImageThreaded": SaveImageThreaded_class,
}