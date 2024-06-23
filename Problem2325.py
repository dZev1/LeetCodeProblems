def decodeMessage(key: str, message: str) -> str:
    code_dict: dict[str, str] = {}
    curr_letra: str = 'a'
    decoded_message: str = ""
    
    for i in key:
        if i not in code_dict.keys() and i != ' ':
            code_dict[i] = curr_letra
            curr_letra = chr(ord(curr_letra) + 1)
    
    for letra in message:
        if letra in code_dict.keys():
            decoded_message += code_dict[letra]
        else:
            decoded_message += letra
        
    return decoded_message
    

if __name__ == "__main__":
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    print(decodeMessage(key, message))
    # "this is a secret"