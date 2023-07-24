import torch
import folder_paths
class sdxlEmbeddingLoadClass:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "conditioning_input_model": (folder_paths.get_filename_list("embeddings"), ),
                    "conditioning_input_refiner": (folder_paths.get_filename_list("embeddings"), )
                }}
    RETURN_TYPES = ("CONDITIONING","CONDITIONING",)
    RETURN_NAMES = ("conditioning_model","conditioning_refiner",)
    FUNCTION = "Load_embedding"
    CATEGORY = "conditioning"

    def Load_embedding(self, conditioning_input_model, conditioning_input_refiner):
        fm_path = folder_paths.get_full_path("embeddings", conditioning_input_model)
        rf_path = folder_paths.get_full_path("embeddings", conditioning_input_refiner)
        conditioning_input_model=torch.load(fm_path)
        conditioning_input_refiner=torch.load(rf_path)
        return(conditioning_input_model,conditioning_input_refiner,)
    
NODE_CLASS_MAPPINGS = {
    "sdxlEmbeddingLoad": sdxlEmbeddingLoadClass
}

