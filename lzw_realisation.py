from struct import *

def encoding(data, name):
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}
    string = ""
    compressed_data = list()
    for symbol in data:
        string_plus_symbol = string + symbol
        if string_plus_symbol in dictionary:
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            dictionary[string_plus_symbol] = dictionary_size
            dictionary_size += 1
            string = symbol

    if string in dictionary:
        compressed_data.append(dictionary[string])

    output_file = open(name + ".lzw", "wb")
    for data in compressed_data:
        output_file.write(pack('>H', int(data)))

    output_file.close()

def decoding(name):
    # taking the compressed file input and the number of bits from command line
    # defining the maximum table size
    # opening the compressed file
    # defining variables
    file = open(name + '.lzw', "rb")
    compressed_data = []
    next_code = 256
    decompressed_data = ""
    string = ""

    # Reading the compressed file.
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data,) = unpack('>H', rec)
        compressed_data.append(data)

    # Building and initializing the dictionary.
    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

    # iterating through the codes.
    # LZW Decompression algorithm
    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + (string[0])
        decompressed_data += dictionary[code]
        if not (len(string) == 0):
            dictionary[next_code] = string + (dictionary[code][0])
            next_code += 1
        string = dictionary[code]

    # storing the decompressed string into a file.
    # out = input_file.split(".")[0]
    # output_file = open(out + "_decoded.txt", "w")
    # for data in decompressed_data:
    #     output_file.write(data)

    file.close()
    return decompressed_data
