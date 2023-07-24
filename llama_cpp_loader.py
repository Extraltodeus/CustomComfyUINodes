from llama_cpp import Llama

class llama_cpp_loader_class:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "model_path": ("STRING", {"multiline": True, "default": r"path"}),
                    "n_gpu_layers":  ("INT", {"default": 64,"min": 1,"max": 256,"step": 1}),
                    "n_ctx":  ("INT", {"default": 4096,"min": 512,"max": 16384,"step": 1})
                }}
    
    RETURN_TYPES = ("LLAMA",)
    FUNCTION = "return_model"
    CATEGORY = "Text/llama_cpp"

    def return_model(self, model_path, n_gpu_layers, n_ctx):
        llm = Llama(model_path=model_path,n_gpu_layers=n_gpu_layers, n_ctx=n_ctx)
        return (llm,)
    
NODE_CLASS_MAPPINGS = {
    "llamacppLoaderNode": llama_cpp_loader_class
}

