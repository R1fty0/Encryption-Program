class FileDecrypter:

    def __init__(self):
        print('File decrypter created!')

    def decrypt_string(self, string, cypher) -> str:
        """ Decrypts a string using a given cypher/shift and then returns the string. """
        decrypted_string = ''
        char_unicode = None

        data_list = list(string)  # list containing each character in the string

        try:
            for character in data_list:  # decrypts each character in the string
                char_unicode = ord(character)
                decrypted_char = chr(char_unicode - cypher)
                decrypted_string += decrypted_char

            print(f"Encrypted message: {decrypted_string}")  # prints the string
            return decrypted_string  # returns the decrypted string

        except TypeError:
            print("An error occurred.")
