def decode_hex_string(hex_string):
    return int(hex_string, 16)


if __name__ == '__main__':
    in1 = '1c0111001f010100061a024b53535009181c'
    in2 = '686974207468652062756c6c277320657965'

    num1 = decode_hex_string(in1)
    num2 = decode_hex_string(in2)

    result = num1 ^ num2

    print(hex(result))

