from FileRead import FileRead
from FileWrite import FileWrite
Border = "_____________________________________________"


FR = None  # File Read
FW = None  # File Write


def start_test():
    global FR, FW
    FR = FileRead()
    FW = FileWrite()

    test_method()

    alternate_method("readingFile", "total")


def test_method():   # Look at automating this
    num = FR.get_total_number_of_lines("readingFile")
    print(f"There is {num} line(s) in the file.")


def alternate_method(file, word):
    if FR.is_keyword_present(file, word):
        print("True")
    elif FR.is_keyword_present(file, word) == False:
        print("False")


if __name__ == "__main__":
    start_test()
