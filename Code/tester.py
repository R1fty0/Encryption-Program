from encryption import FileEncrypter
from decryption import FileDecrypter
from reader import FileRead
from writer import FileWrite

encoder = FileEncrypter()
decoder = FileDecrypter()

decoder.decrypt_string("csvi", 1)


