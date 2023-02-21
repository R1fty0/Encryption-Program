from encryption import FileEncrypter
from reader import FileRead
from writer import FileWrite

encoder = FileEncrypter()

encoder.encode_string("Bruh", 1) # CSVI (+1)
print("----------------------------------")
encoder.encode_string("Bruh", -1) # AQTG (-1)


