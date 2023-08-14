from copy import deepcopy
import torch
import math

def sinc(x):
    if x == 0:
        return 1.0
    return torch.sin(math.pi * x) / (math.pi * x)

def lanczos(x, a=3):
    if abs(x) < 1e-5:
        return torch.tensor(1.0)
    if abs(x) > a:
        return torch.tensor(0.0)
    return sinc(x) * sinc(x/a)
    
def upscale_lanczos(tensor, scale_factor, a=3):
    # Input tensor: [C, H, W]
    C, H, W = tensor.shape
    
    new_H = int(math.ceil(H * scale_factor))
    new_W = int(math.ceil(W * scale_factor))
    
    # Generate the coordinates for the original and the upscaled images
    orig_coords_x = torch.linspace(0, W - 1, steps=W)
    orig_coords_y = torch.linspace(0, H - 1, steps=H)
    
    up_coords_x = torch.linspace(0, W - 1, steps=new_W)
    up_coords_y = torch.linspace(0, H - 1, steps=new_H)
    
    # Calculate the contributions of each pixel based on the lanczos kernel
    contributions_x = torch.stack([lanczos((up_x - orig_x) / scale_factor, a) for up_x in up_coords_x for orig_x in orig_coords_x])
    contributions_y = torch.stack([lanczos((up_y - orig_y) / scale_factor, a) for up_y in up_coords_y for orig_y in orig_coords_y])
    
    contributions_x = contributions_x.view(new_W, W)
    contributions_y = contributions_y.view(new_H, H)
    
    # Normalize contributions
    contributions_x /= contributions_x.sum(dim=1, keepdim=True)
    contributions_y /= contributions_y.sum(dim=1, keepdim=True)
    
    # Upscale width
    upscaled_tensor_w = torch.einsum('jw,chw->chj', contributions_x, tensor)
    
    # Upscale height
    upscaled_tensor_hw = torch.einsum('ih,chj->cij', contributions_y, upscaled_tensor_w)
    
    return upscaled_tensor_hw

class latent_lanczos_upscale_by:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "LATENT": ("LATENT", {"forceInput": True}),
                "upscale_by": ("FLOAT", {"default": 1, "min": 0,"max": 12,"step": 0.5}),
                "support": ("INT", {"default": 32, "min": 0,"max": 512,"step": 1})
            }
        }

    FUNCTION = "simple_output"
    RETURN_TYPES = ("LATENT",)
    CATEGORY = "latent"

    def simple_output(self, LATENT,upscale_by,support):
        if upscale_by == 1:
            return (LATENT,)
        new_latents = deepcopy(LATENT)
        samples = []
        for index in range(LATENT['samples'].shape[0]):
            bigger_latent = upscale_lanczos(new_latents['samples'][index],upscale_by,support)
            samples.append(bigger_latent)
        new_latents['samples'] = torch.stack(samples, dim=0)
        return (new_latents,)


NODE_CLASS_MAPPINGS = {
    "latent_lanczos_upscale_by": latent_lanczos_upscale_by,
}
