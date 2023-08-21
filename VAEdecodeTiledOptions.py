

class VAEDecodeTiledOptions:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "samples": ("LATENT", ), "vae": ("VAE", ),
            "tiles_size": ("INT", {"default": 128, "min": 32,"max": 256,"step": 8}),
            "overlap": ("INT", {"default": 8, "min": 2,"max": 64,"step": 2}),
            "enabled": ("INT", {"default": 1, "min": 0,"max": 1,"step": 1})
            }}
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "decode"

    CATEGORY = "latent"

    def decode(self, vae, samples, tiles_size, overlap,enabled):
        if enabled != 1:
            return (samples,)
        for lat in samples['samples']:
            d, y, x = lat.size()
            break
        if x*8 * y*8 > 2097152:
            return (vae.decode_tiled(samples["samples"], tiles_size, tiles_size, overlap), )
        else:
            return (vae.decode(samples["samples"]), )

NODE_CLASS_MAPPINGS = {
    "VAEDecodeTiled with options": VAEDecodeTiledOptions
}
