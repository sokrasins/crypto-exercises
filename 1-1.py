import base64

def convert_hex_to_base64(string):
    string_bytes = string.decode("hex")
    return base64.b64encode(string_bytes)

if __name__ == '__main__':
    start_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

    ans = convert_hex_to_base64(start_string)
    print(ans)
