import base64


def string_to_binary(input_string):
    return ''.join(format(ord(char), '08b') for char in input_string)


def binary_to_string(binary_string):
    char_array = [chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8)]
    return ''.join(char_array)


def invert_binary(binary_string):
    return ''.join('1' if bit == '0' else '0' for bit in binary_string)


def reverse_binary(binary_string):
    return binary_string[::-1]


def xor_with_fixed_vector(binary_string, fixed_vector):
    fixed_vector = fixed_vector[:len(binary_string)]
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(binary_string, fixed_vector))


def binary_to_base64(binary_string):
    byte_array = bytearray(int(binary_string[i:i + 8], 2) for i in range(0, len(binary_string), 8))
    return base64.b64encode(byte_array).decode()


def base64_to_binary(base64_string):
    byte_array = base64.b64decode(base64_string)
    return ''.join(format(byte, '08b') for byte in byte_array)


def decrypt(encrypted_base64, fixed_vector):
    binary_string = base64_to_binary(encrypted_base64)
    xored_binary = xor_with_fixed_vector(binary_string, fixed_vector)
    reversed_binary = reverse_binary(xored_binary)
    inverted_binary = invert_binary(reversed_binary)
    return binary_to_string(inverted_binary)


if __name__ == "__main__":
    encrypted_base64 = "o3Mj++dR0mOn"
    fixed_vector = "10101010101010101010101010101010" * 10

    decrypted = decrypt(encrypted_base64, fixed_vector)
    print("Decrypted message:", decrypted)
