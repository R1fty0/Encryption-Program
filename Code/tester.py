from reader import FileRead
from writer import FileWrite
Border = "_____________________________________________"


FR = None  # File Read
FW = None  # File Write

random_list = ["Hello", "Cool", "World"]


def test_beginning():
    """ Sets up the things need for the test."""
    global FR, FW
    FR = FileRead()
    FW = FileWrite()
    print("T1 passed")
    test()


def test():
    """ Testing occurs here. """
    FW.write_data_to_file(random_list, "A.txt")
    print("T2 passed")






if __name__ == "__main__":
    test_beginning()
