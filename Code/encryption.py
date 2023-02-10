class FileEncrypter:
    def __init__(self, character, number, message, key):
        self.character = character
        self.number = number
        self.message = message
        self.key = key
        print('File encrypter created!')

    def characterCast(self, character):
        return ord(character)

    def convertBackToChar(self, number):
        return chr(number)

    def encryptString(self, message, key):
        ''' Change the value of the given String to one shifted using a Cesarean cipher '''
        encryptedString = ''

        messageList = list(message)

        for character in messageList:
            intVal = ord(character)
            newChar = chr(intVal + key)
            encryptedString += newChar

        print("Encrypted message: " + encryptedString)
