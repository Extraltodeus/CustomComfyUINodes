from PIL import Image
import numpy as np
import torch

class upscale_antialias_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_image": ("IMAGE",),
                "upscale_by": ("FLOAT", {"default": 1.5, "min": 0.0, "max": 10.0, "step": 0.1})
            }
        }

    FUNCTION = "upscale_antialias"
    RETURN_TYPES = ("IMAGE",)
    CATEGORY = "image"

    def upscale_antialias(self, input_image, upscale_by):
        upscaled_images = []
        for x in range(len(input_image)):
            i = 255. * input_image[x].cpu().numpy()
            image = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            width, height = image.size
            image = image.resize((int(width*upscale_by), int(height*upscale_by)), Image.Resampling.LANCZOS)
            numpy_image = np.array(image)
            numpy_image = numpy_image / 255.0
            tensor_image = torch.from_numpy(numpy_image)

            tensor_image = tensor_image.unsqueeze(0)
            upscaled_images.append(tensor_image)
            
        upscaled_images_tensor = torch.cat(upscaled_images, 0)
        return (upscaled_images_tensor,)


        
NODE_CLASS_MAPPINGS = {
    "upscale_antialias": upscale_antialias_class
}
