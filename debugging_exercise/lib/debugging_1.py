def encode(text, key):
    # print(f"{text} is text")
    # print(f"{key} is key")
    cipher = make_cipher(key) 
    print(f"cipher is{cipher} ")

    ciphertext_chars = []
    print(f"loop iteration started")
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        # print(f"looping through {text}")
        # print(f"{ciphered_char} is ciphered_char")
        ciphertext_chars.append(ciphered_char)
        # print(f"{ciphered_char} appended to {ciphertext_chars}")
        # print(f" loop iteration ended")

    return "".join(ciphertext_chars)



def decode(encrypted, key):
    cipher = make_cipher(key)
    print(f"{encrypted} is encrypted")
    print(f'{key} is key')
    print(f"cipher is {cipher}")

    plaintext_chars = []
    print(f"{plaintext_chars} is plaintext_chars")
    print(f"loop iteration started")
    for i in encrypted:
        print(f"looping through {encrypted}")
        plain_char = cipher[ord(i)-65]
        print(f"{plain_char} is plain_char")
        plaintext_chars.append(plain_char)
        print(f"{plain_char} appended to {plaintext_chars}")

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(0, 26)]
    print(f"alphabet is {alphabet}")
    cipher_with_duplicates = list(key) + alphabet
    
    print(f"cipher_with_duplicates is= {key} + {alphabet}")

    cipher = []
    print(f"cipher is {cipher}")
    print(f"loop iteration started")
    for i in range(0, len(cipher_with_duplicates)):
        print(f"looping through {i}")
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
            print(f"this line {cipher_with_duplicates[:i]}")
            print(f"{cipher_with_duplicates[i]} appended to {cipher}")

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
