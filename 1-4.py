import string

def xor_bytearrays(in1, in2):
    return bytearray(a ^ b for (a, b) in zip(in1, in2))

def decode_hex_string(hex_string):
    return bytearray.fromhex(hex_string)

def score_char(string, char):
    if not char.isupper():
        char = char.upper()

    expected = get_expected_occurrences(bytes(char, 'utf-8'), len(string))
    actual = string.count(bytes(char, 'utf-8'))
    actual += string.count(bytes(char.lower(), 'utf-8'))

    return abs(expected - actual)

def score_string(text):
    scores = []
    for char in string.ascii_uppercase:
        scores.append(score_char(text, char))
    return sum(scores)

def get_expected_occurrences(byte, length):
    english_avg = {
        b'A': 8.4966,
        b'B': 2.0720,
        b'C': 4.5388,
        b'D': 3.3844,
        b'E': 11.1607,
        b'F': 1.8121,
        b'G': 2.4705,
        b'H': 3.0034,
        b'I': 7.5448,
        b'J': 0.1965,
        b'K': 1.1016,
        b'L': 5.4893,
        b'M': 3.0129,
        b'N': 6.6544,
        b'O': 7.1635,
        b'P': 3.1671,
        b'Q': 0.1962,
        b'R': 7.5809,
        b'S': 5.7351,
        b'T': 6.9509,
        b'U': 3.6308,
        b'V': 1.0074,
        b'W': 1.2899,
        b'X': 0.2902,
        b'Y': 1.7779,
        b'Z': 0.2722
    }

    return english_avg[byte] / 100.0 * length

def decrypt(ciphertext, key):
    stream = bytearray([key] * len(ciphertext))
    return xor_bytearrays(ciphertext, stream)


if __name__ == '__main__':
    in_text = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    ciphertext = decode_hex_string(in_text)

    scores = []
    for i in range(256):
        plaintext = decrypt(ciphertext, i)
        scores.append(score_string(plaintext))

    min_idx = scores.index(min(scores))

    result = decrypt(ciphertext, min_idx)
    print(result)
    print("key: %s" % (hex(min_idx)))

