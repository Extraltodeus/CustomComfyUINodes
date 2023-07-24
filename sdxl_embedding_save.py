import torch
import os
import folder_paths
class sdxlEmbeddingSaveClass:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "conditioning_input_model": ("CONDITIONING", {"forceInput": True}),
                    "conditioning_input_refiner": ("CONDITIONING", {"forceInput": True}),
                    "output_dir": ("STRING", {"default": folder_paths.get_folder_paths("embeddings")}),
                    "filename": ("STRING", {"default": "sdxl_embedding"})
                }}
    RETURN_TYPES = ("CONDITIONING","CONDITIONING",)
    RETURN_NAMES = ("conditioning_model","conditioning_refiner",)
    FUNCTION = "save_embedding"
    CATEGORY = "conditioning"

    def save_embedding(self, conditioning_input_model, conditioning_input_refiner, output_dir, filename):
        fm_path = os.path.join(output_dir,filename+"_for_model.pt")
        rf_path = os.path.join(output_dir,filename+"_for_refiner.pt")
        torch.save(conditioning_input_model,fm_path)
        torch.save(conditioning_input_refiner,rf_path)
        print("Model saved at:",fm_path)
        print("Refiner saved at:",rf_path)
        return(conditioning_input_model,conditioning_input_refiner,)
    
NODE_CLASS_MAPPINGS = {
    "sdxlEmbeddingSave": sdxlEmbeddingSaveClass
}

