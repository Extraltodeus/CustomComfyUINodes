
class vae_decode_condition_class:
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                        "samples": ("LATENT", ), "vae": ("VAE", ),
                        "save_bool": ("INT", {"default": 1, "min": 0,"max": 1,"step": 1})
                        }
                }
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "decode"

    CATEGORY = "latent"

    def decode(self, vae, samples, save_bool):
        if save_bool != 1: return (("",))
        return (vae.decode(samples["samples"]), )

NODE_CLASS_MAPPINGS = {
    "vae_decode_condition": vae_decode_condition_class,
}

