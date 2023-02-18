import numpy as np

def encode_message(message, matrix):
    n = matrix.shape[0]
    if len(message) % n != 0:
        message += ' '*(n - len(message) % n)
    encoded = ''
    for i in range(0, len(message), n):
        chunk = message[i:i+n]
        chunk_vec = np.array([ord(c) for c in chunk]).reshape((n,1))
        encoded_vec = matrix.dot(chunk_vec)
        encoded_chunk = ''.join([chr(int(x)) for x in encoded_vec])
        encoded += encoded_chunk
    return encoded

def decode_message(encoded, matrix):
    n = matrix.shape[0]
    decoded = ''
    for i in range(0, len(encoded), n):
        chunk = encoded[i:i+n]
        chunk_vec = np.array([ord(c) for c in chunk]).reshape((n,1))
        decoded_vec = np.linalg.inv(matrix).dot(chunk_vec)
        decoded_chunk = ''.join([chr(int(x)) for x in decoded_vec])
        decoded += decoded_chunk
    return decoded.strip()

# example usage
matrix = np.array([[2, 3], [5, 7]])
message = 'hello world'
print("Original message:", message)

# encode message
encoded = encode_message(message, matrix)
print("Encoded message:", encoded)

# decode message
decoded = decode_message(encoded, matrix)
print("Decoded message:", decoded)
