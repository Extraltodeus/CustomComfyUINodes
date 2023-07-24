class TypeConverter:
    @classmethod
    def INPUT_TYPES(cls):
        if cls.INPUT_TYPE[0] == cls.INPUT_TYPE[1] and (cls.INPUT_TYPE[0] == "INT" or cls.INPUT_TYPE[0] == "FLOAT"):
            properties = {"input": (cls.INPUT_TYPE[0], {"default":1,"min":-1000000,"max":1000000,"step":0.1 if cls.INPUT_TYPE[0] == "FLOAT" else 1})}
        else:
            properties = {"input": (cls.INPUT_TYPE[0], {"forceInput": True})}
        return {"required": properties}

    FUNCTION = "run"
    CATEGORY = "var_conversion"

    def run(self, input):
        if self.__class__.TYPE_OUT == "INT":
            return (int(input),)
        elif self.__class__.TYPE_OUT == "FLOAT":
            return (float(input),)
        elif self.__class__.TYPE_OUT == "STRING":
            return (str(input),)
        else:
            return (input,)

NODE_CLASS_MAPPINGS = {}

def addConverterType(t_in, t_out):
    NODE_CLASS_MAPPINGS[t_in+"_to_"+t_out] = type("TypeConverter_" + t_in + "_to_" + t_out, 
                                                 (TypeConverter,), 
                                                 { "INPUT_TYPE": [t_in,t_out], "TYPE_OUT": t_out, "RETURN_TYPES": (t_out,), "RETURN_NAMES": (t_out,) })
# Now you can create a converter from one type to another
nodes_to_create = ["INT","FLOAT","STRING","PROMPT","CONDITIONING"]
for n in nodes_to_create:
    for c in nodes_to_create:
        addConverterType(n,c)
