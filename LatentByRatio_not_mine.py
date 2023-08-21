import torch

class LatentByRatio:
    def __init__(self, device="cpu"):
        self.device = device
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                        "model": (["SDXL 1024","SD1.5 512","SD2.1 768"],),
                        "ratio": ([
                                   "1:1",
                                   "2:3",
                                   "3:2",
                                   "3:4",
                                   "4:3",
                                   "16:9", 
                                   "9:16", 
                                   "21:9",
                                   "9:21",
                                   "2:1",
                                   "1:2",
                                   "4:1",
                                   "1:4"
                                   ],),
                        "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})
                    }
                }
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "generate"

    CATEGORY = "latent"

    def generate(self,model,ratio,batch_size):
        base = 512
        if model == "SD2.1 768":
            base = 768
        elif model == "SDXL 1024":
            base = 1024

        widthRatio,heightRatio = ratio.split(":")
        widthRatio = int(widthRatio)
        heightRatio = int(heightRatio)
        # print(f"widthRatio: {widthRatio},heightRatio: {heightRatio}")
        maxRatio = max(widthRatio,heightRatio)
        minRatio = min(widthRatio,heightRatio)
        # print(f"minRatio: {minRatio}")
        baseUnit = 64
        width = base/minRatio * widthRatio
        height = base/minRatio * heightRatio

        maxLimit = base * 2

        # use base unit to calculate width and height
        if maxRatio > 10:
            width = baseUnit * widthRatio
            height = baseUnit * heightRatio
        # limit max width less than 2 times of base
        if width > maxLimit or height > maxLimit:
            width = width / 2
            height = height / 2
        width = int(width)
        height = int(height)
        # print(f"width: {width},height: {height}")

        latent = torch.zeros([batch_size, 4, height // 8, width // 8])

        return ({"samples":latent},)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "LatentByRatio": LatentByRatio
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "JNode": "LatentByRatio"
}