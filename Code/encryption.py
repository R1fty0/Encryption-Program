import sys
from reader import FileRead
from writer import FileWrite


class FileEncrypter:
    def __init__(self):
        print("File encrypter created!")

    def get_char_unicode_val(self, character):
        """ Returns the Unicode code point for the given character in the ASCII encoding. """
        return ord(character)

    def convert_back_to_char(self, number):
        return chr(number)

    def encode_string(self, message: str, cipher_key: int) -> str:
        """ Encodes a given string using a Cesarean cipher and returns the encoded string. """
        encrypted_string = ''
        try:
            messageList = list(message)

            for character in messageList:
                char_unicode = ord(character)  # Gets the character's unicode code point

                # Checks to see if character's unicode is not a unicode representing a letter
                if char_unicode > 126:
                    char_unicode -= 95
                elif char_unicode < 32:
                    char_unicode += 95
                else:
                    # encrypts the character based on the cipher's key
                    new_encoded_char = chr(char_unicode + cipher_key)
                    encrypted_string += new_encoded_char

            print(f"Encrypted message: {encrypted_string}")  # prints the encoded string
            return encrypted_string  # returns the encoded string

        except TypeError:
            print("An error occurred.")

    def encode_to_file(self, new_file_name, data, encryption_key):
        # TypeError: FileWrite.writeStringToFile() missing 1 required positional argument: 'data' (Line 46)
        """ Data given will be encoded as well as written to a custom file. """

        if isinstance(data, str):  # if data is a string
            data = self.encode_string(data, encryption_key)  # Encode data
            FileWrite.writeStringToFile(new_file_name, data)  # Write data to file

        elif isinstance(data, list):  # if data is a list
            data = self.encode_list_of_data(data, encryption_key)  # Encodes data
            FileWrite.writeListDataToFile(new_file_name, data)  # Writes data to file

    def encode_list_of_data(self, data: list, cipher_key) -> list:
        """ Accepts a list of Strings, encodes all of them, and returns a list of the encoded content. """
        encoded_content = list()
        try:
            for string in data:  # Encodes each string in list of data
                encoded_data = self.encode_string(string, cipher_key)
                encoded_content.append(encoded_data)
            return encoded_content  # Returns list containing encoded data
        except TypeError:
            print("The data or cipher key you inputted is invalid. Please try again and enter a proper value for both attributes.")
