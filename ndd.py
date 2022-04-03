import cv2
import logging
import numpy

def binary_array_to_hex(arr):
    """
    internal function to make a hex string out of a binary array.
    """
    bit_string = ''.join(str(b) for b in 1 * arr.flatten())
    width = int(numpy.ceil(len(bit_string)/4))
    return '{:0>{width}x}'.format(int(bit_string, 2), width=width)

def dhash(image, hash_size=8):
    """
    Performs Difference Hash computation.
    see: http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html
    """
    if hash_size < 2:
        raise ValueError("Hash size must be greater than or equal to 2")
    image = cv2.resize(image, (hash_size, hash_size + 1), interpolation = cv2.INTER_AREA)
    diff = image[:, 1:] > image[:, :-1] # differences horizontally
    logging.debug('hash: {}'.format(binary_array_to_hex(diff)))
    return numpy.packbits(diff.flatten())

def similarity(hash1, hash2, hash_size):
    hd = sum(numpy.bitwise_xor(numpy.unpackbits(hash1), 
                               numpy.unpackbits(hash2)))
    similarity = (hash_size**2 - hd) / hash_size**2
    return similarity
