# Takes an input keyword and message and uses Vigenere's Cypher to encode the message

alphanum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
            'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
            'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

space_count = 0


def next_letter(key_char, src_char):
    global space_count
    if src_char == ' ':
        space_count += 1
        return src_char
    else:
        encode_index = alphanum[key_char.lower()] + alphanum[src_char.lower()]
        return letters[encode_index % 26]


if __name__ == '__main__':
    key = input('Enter keyword for encoding:')
    src = input('Enter message to be encoded:')
    output = ""
    for i in range(len(src)):
        output += next_letter(key[(i - space_count) % len(key)], src[i])
    print("key: %s\nsrc: %s\noutput: %s" % (key, src, output))
