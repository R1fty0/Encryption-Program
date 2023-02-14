from reader import FileRead
from writer import FileWrite



reader = FileRead()
num = reader.get_total_characters("A.txt")
print(str(num) + " words (1)")

string = "99 bottles of beer."  # 19
num_of_char = len(string)
print(str(num_of_char) + " words (2)")