
PARAMS = {
    'max_new_tokens': 175,
    'temperature': 0.7,
    'top_p': 0.9,
    'typical_p': 1,
    'n': 1,
    'stop': None,
    # 'do_sample': True,
    'return_prompt': False,
    'return_metadata': False,
    'repetition_penalty': 1.17,
    'encoder_repetition_penalty': 1.0,
    'top_k': 20,
    'min_length': 0,
    'no_repeat_ngram_size': 0,
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

class llama_cpp_text_completion_class:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "llama_model": ("LLAMA", {"forceInput": True}),
                "prompt": ("STRING", {"multiline": True, "dynamicPrompts": False}),
            },
            "optional": {
                "max_new_tokens": ("INT", {"default": PARAMS['max_new_tokens']}),
                "temperature": ("FLOAT", {"default": PARAMS['temperature']}),
                "top_p": ("FLOAT", {"default": PARAMS['top_p']}),
                "repetition_penalty": ("FLOAT", {"default": PARAMS['repetition_penalty']}),
                "top_k": ("INT", {"default": PARAMS['top_k']}),
                "seed": ("INT", {"default": PARAMS['seed']})
            }
        }
        
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_text"
    CATEGORY = "Text/llama_cpp"
    
    def generate_text(self, llama_model, prompt, max_new_tokens, temperature, top_p, repetition_penalty, top_k, seed):
        self.prompt = prompt
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.repetition_penalty = repetition_penalty
        self.top_k = top_k
        self.seed = seed
        llama_model.seed = seed
        output = llama_model.create_completion(
            prompt=self.prompt,
            max_tokens=self.max_new_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            repeat_penalty=self.repetition_penalty,
            top_k=self.top_k
        )
        output_text = output['choices'][0]['text']
        return(output_text,)
    

NODE_CLASS_MAPPINGS = {
    "llamacppTextCompletionNode": llama_cpp_text_completion_class
}
