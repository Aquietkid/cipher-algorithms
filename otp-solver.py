def get_letter(char):
    if len(char) > 1:
        raise ValueError("Character must have length 1!")
    else:
        return ord(char.lower()) - ord('a')


def string_xor(str1, str2):
    """
    Performs XOR operation on two strings of equal length character by character
    and returns the result mapped to a-z range.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
    
    Returns:
        str: XOR result mapped to lowercase a-z range
    
    Raises:
        ValueError: If strings have different lengths
    """
    if len(str1) != len(str2):
        raise ValueError("Strings must have equal length")
    
    # Convert to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    result = ""
    
    for char1, char2 in zip(str1, str2):
        # Get ASCII values
        val1 = get_letter(char1)
        val2 = get_letter(char2)
        
        # Perform XOR
        xor_result = (val1 ^ val2)
        # print(xor_result)
        
        # Map to a-z range (0-25) using modulo 26
        mapped_char = chr((xor_result) + ord('a'))
        result += mapped_char
    
    return result

# Example usage
if __name__ == "__main__":
    # Test the function
    string1 = "aimebbekhdper"
    string2 = "cashnotneeded"
    
    result = string_xor(string1, string2)
    print(f"XOR of '{string1}' and '{string2}': {result}")
    print(f"XOR of '{string1}' and '{result}': {string_xor(string1, result)}")

