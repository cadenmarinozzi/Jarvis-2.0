import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")

def encode(text):
    return enc.encode(text);

def decode(text):
    return enc.decode(text);