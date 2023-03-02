class FileDecrypter:
    def __init__(self, file_basics, file_reader, file_writer):
        self.basics = file_basics
        self.reader = file_reader
        self.writer = file_writer

    def decrypt_string(self, data, cypher) -> str:
        """ Decrypts a string using a given cypher/shift and then returns the encrypted data."""
        # Need to remove space symbols...
        decrypted_string = ''

        data_list = list(data)  # list containing each character in the string

        try:
            for character in data_list:  # decrypts each character in the string
                char_unicode = ord(character)
                decrypted_char = chr(char_unicode - cypher)
                decrypted_string += decrypted_char

            print(f"Decrypted message: {decrypted_string}\nOriginal Encrypted Message: {string}")  # prints the string
            return decrypted_string  # returns the decrypted string

        except TypeError:
            print("An error occurred.")
