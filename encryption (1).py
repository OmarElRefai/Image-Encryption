# FIRST FUNCTION
def encrypt(plain_text, key): # Accepts a plaintext and a key
    key_d = {} # Creating a dictionary for the key
    encoded_txt = [] # List for the plaintext
    for i, l in enumerate(key): # Converting data from key to key_dict
        key_d[i] = l

    for value in plain_text: # Encrypting the plain_text
        encoded_txt.append(
            key_d[value]
        )
    return bytes(encoded_txt) # Converting the content to a list of bytes before writing it to the file

# SECOND FUNCTION
def decrypt(cipher_text, key): # Accepts a ciphertext and a key
    key_d = {} # Creating a dictionary for the key
    decoded_txt = [] # list for the decoded text
    for i, l in enumerate(key):
        key_d[l] = i # reversing the dictionary from the encryption

    for value in cipher_text: # for loop to add the decryption into the list
        decoded_txt.append(
            key_d[value]
        )
    return bytes(decoded_txt) # Returns a plaintext that is the decryption of the ciphertext as a list of bytes

# THIRD FUNCTION
def read_file(file_name): # Accepts a filename
    file = open(file_name, "rb") # Opening the file in binary mode.
    content = file.read()
    file.close()
    return content # Returns the content of the file as a list of bytes

# FOURTH FUNCTION
def write_file(file_name, content): # Accepts a filename and a content
    file = open(file_name, "wb") # Opening the file in binary write mode
    file.write(content) # Writing the content into the file
    file.close()

# FIFTH FUNCTION (TEST)
def test_encryption():
    plain_text = read_file("plain_text") # Reading the plaintext
    key = read_file("key") # Reading the key
    cipher_text = encrypt(plain_text, key)  # Encrypting the plain_text
    write_file("cipher_text", cipher_text) # Writing the cipher_text
    cipher_text_opened = read_file("cipher_text") # Reading the cipher_text
    decoded = decrypt(cipher_text_opened, key) # Decrypting the cipher_text
    write_file("plain_text1", decoded) # Writing the plain_text from earlier to a file called plain_text1

test_encryption()
