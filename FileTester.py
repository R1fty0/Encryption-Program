from FileRead import FileRead
from FileWrite import FileWrite
import Decryption
import Encryption


FR = FileRead()

contents = FR.readFileLineByLine("FileToTestOn.txt")
print(f"{contents}")