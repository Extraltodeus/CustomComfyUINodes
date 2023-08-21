from colorama import Fore
import torch
class print_latent_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "LATENT_input": ("LATENT", {"forceInput": True}),
                "save_sample": (["enable", "disable"], {"default": "disable"}),
                "print_color": (["GREEN", "WHITE", "RED", "YELLOW", "BLUE", "MAGENTA", "CYAN"],)
            }
        }

    FUNCTION = "simple_print"
    RETURN_TYPES = ()
    CATEGORY = "latent"
    OUTPUT_NODE = True
    
    def simple_print(self, LATENT_input, save_sample, print_color):
        color_mapping = {
            "BLACK": Fore.BLACK,
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,
            "WHITE": Fore.WHITE,
            "RESET": Fore.RESET
        }
        for lat in LATENT_input['samples']:
            print("Print node :",f"{color_mapping[print_color]}{lat.size()}{Fore.RESET}")
            flattened = lat.flatten()
            min_val, max_val = torch.min(flattened), torch.max(flattened)
            print(min_val, max_val)
            num_bins = 64
            hist = torch.histc(flattened, bins=num_bins, min=min_val, max=max_val)
            bin_edges = torch.linspace(min_val, max_val, steps=num_bins+1)
            for i, count in enumerate(hist):
                # print(f"Interval {i + 1}: {count.item()} values")
                print(f"Interval {i + 1} ({round(bin_edges[i].item(),1)} to {round(bin_edges[i+1].item(),1)}): {hist[i].item()} values")
            for i, count in enumerate(hist):
                print("|"*int(count.item()/100),round((bin_edges[i].item()+bin_edges[i+1].item())/2,1))
                # print(f"Interval {i + 1} ({round(bin_edges[i].item(),1)} to {round(bin_edges[i+1].item(),1)}): {hist[i].item()} values")
        if save_sample=="enable":
            torch.save(LATENT_input['samples'],"./saved_samples.pt")
        return {}
    
class output_latent_size_class:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "LATENT_input": ("LATENT", {"forceInput": True}),
            }
        }

    FUNCTION = "simple_output"
    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("width","height",)
    CATEGORY = "latent"
    
    def simple_output(self, LATENT_input):
        for lat in LATENT_input['samples']:
            d, y, x = lat.size()
            break
        return (x*8,y*8,)

class output_latent_batch_amount:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "LATENT_input": ("LATENT", {"forceInput": True}),
            }
        }

    FUNCTION = "simple_output"
    RETURN_TYPES = ("INT",)
    CATEGORY = "latent"
    
    def simple_output(self, LATENT_input):
        return (len(LATENT_input['samples']),)
    
NODE_CLASS_MAPPINGS = {
    "print_latent": print_latent_class,
    "output_latent_size": output_latent_size_class,
    "output_latent_batch_amount": output_latent_batch_amount
}
