def encode(message: str, shift: int, alphabet_length: int) -> str:
    result = ""
    for letter in message:
        result += chr((ord(letter) - ord('a') + shift) % alphabet_length + ord('a'))
        
    return result
    
def decode(message: str, shift: int, alphabet_length: int) -> str:
    result = ""
    for letter in message:
        result += chr((ord(letter) - ord('a') - shift) % alphabet_length + ord('a'))
        
    return result
 

print(f"'{encode("abc", 3, 26)}'")
print(f"'{decode("abc", 3, 26)}'")

