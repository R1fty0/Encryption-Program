class FileEncrypter:
    def __init__(self, character, number, message, key):
        self.character = character
        self.number = number
        self.message = message
        self.key = key
        print('File encrypter created!')

    def input_data(self, name=input("What variable are you looking to change? (Enter the name): "), newVar=input(f"What would you like the new value of the variable to be?: ")):
        """ Changes one of the class variables depending on user input """
        if name.upper() == "CHARACTER":
            print("Changing Character Variable")
            self.character = newVar
            print(self.character)
        elif name.upper() == "NUMBER":
            print("Changing number variable")
            self.number = newVar
            print(self.number)
        elif name.upper() == "MESSAGE":
            print("Changing message variable")
            self.message = newVar
            print(self.message)
        elif name.upper() == "KEY":
            print("changing key variable")
            self.key = newVar
            print(self.key)
        else:
            print("Error, you might have entered in a value incorrectly")
            pass

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


Bob = FileEncrypter(2, 2, "Life is like a dream", 1)

Bob.input_data()


