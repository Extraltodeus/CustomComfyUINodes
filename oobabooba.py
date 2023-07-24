
import json
import requests


PARAMS = {
    'max_new_tokens': 200,
    'temperature': 0.5,
    'top_p': 0.9,
    'typical_p': 1,
    'n': 1,
    'stop': None,
    'do_sample': True,
    'return_prompt': False,
    'return_metadata': False,
    'typical_p': 0.95,
    'repetition_penalty': 1.05,
    'encoder_repetition_penalty': 1.0,
    'top_k': 0,
    'min_length': 0,
    'no_repeat_ngram_size': 2,
    'num_beams': 1,
    'penalty_alpha': 0,
    'length_penalty': 1.0,
    'pad_token_id': None,
    'eos_token_id': None,
    'use_cache': True,
    'num_return_sequences': 1,
    'bad_words_ids': None,
    'seed': -1,
}

class Oobabooba_class:

    do_sample = True
    early_stopping = False
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "dynamicPrompts": False}),
            },
            "optional": {
                "model_name": ("STRING", {"default": "Does not matter anyway"}),
                "max_new_tokens": ("INT", {"default": PARAMS['max_new_tokens']}),
                "temperature": ("FLOAT", {"default": PARAMS['temperature']}),
                "top_p": ("FLOAT", {"default": PARAMS['top_p']}),
                "typical_p": ("FLOAT", {"default": PARAMS['typical_p']}),
                "repetition_penalty": ("FLOAT", {"default": PARAMS['repetition_penalty']}),
                "encoder_repetition_penalty": ("FLOAT", {"default": PARAMS['encoder_repetition_penalty']}),
                "top_k": ("INT", {"default": PARAMS['top_k']}),
                "min_length": ("INT", {"default": PARAMS['min_length']}),
                "no_repeat_ngram_size": ("INT", {"default": PARAMS['no_repeat_ngram_size']}),
                "num_beams": ("INT", {"default": PARAMS['num_beams']}),
                "penalty_alpha": ("FLOAT", {"default": PARAMS['penalty_alpha']}),
                "length_penalty": ("FLOAT", {"default": PARAMS['length_penalty']}),
                "seed": ("INT", {"default": PARAMS['seed']})
            }
        }
        
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_text"
    CATEGORY = "Text"
    
    def generate_text(self, model_name, prompt, max_new_tokens, temperature, top_p, typical_p, repetition_penalty, encoder_repetition_penalty, top_k, min_length, no_repeat_ngram_size, num_beams, penalty_alpha, length_penalty, seed):
        self.model_name = model_name
        self.prompt = prompt
        self.max_new_tokens = max_new_tokens
        self.do_sample = True
        self.temperature = temperature
        self.top_p = top_p
        self.typical_p = typical_p
        self.repetition_penalty = repetition_penalty
        self.encoder_repetition_penalty = encoder_repetition_penalty
        self.top_k = top_k
        self.min_length = min_length
        self.no_repeat_ngram_size = no_repeat_ngram_size
        self.num_beams = num_beams
        self.penalty_alpha = penalty_alpha
        self.length_penalty = length_penalty
        self.early_stopping = False
        self.seed = seed
        
        # Make request to API to generate text
        url = f"http://127.0.0.1:5000/api/v1/generate"
        headers = {"Content-Type": "application/json"}
        params = {
            'prompt': self.prompt,
            'max_new_tokens': self.max_new_tokens,
            'do_sample': self.do_sample,
            'temperature': self.temperature,
            'top_p': self.top_p,
            'typical_p': self.typical_p,
            'repetition_penalty': self.repetition_penalty,
            'encoder_repetition_penalty': self.encoder_repetition_penalty,
            'top_k': self.top_k,
            'min_length': self.min_length,
            'no_repeat_ngram_size': self.no_repeat_ngram_size,
            'num_beams': self.num_beams,
            'penalty_alpha': self.penalty_alpha,
            'length_penalty': self.length_penalty,
            'early_stopping': self.early_stopping,
            'seed': self.seed,
        }
        response = requests.post(url, json=params)
        if response.status_code == 200:
            result = response.json()['results'][0]['text']
            return (result,)
    

NODE_CLASS_MAPPINGS = {
    "Oobabooba": Oobabooba_class
}
