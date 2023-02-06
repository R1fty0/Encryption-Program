# Python file open(fileName, access mode) access modes
# 'r' = read only mode
# 'w' = write only mode - erases everything that was there already!
# 'a' = append mode (write without replacing data)


# Python file functions
# read() - return whole file
# readline() - returns one line of the file
# readlines() = returns ALL lines in a list (1 line per entry)

# MBM = Made by me (Mohit).

class FileRead:

    def __init__(self):
        print('File reader created!')

    def readFirstLineFromFile(self, file):
        """ Print out the contents from the first line of a file. """
        try:
            with open(file, 'r') as reader:
                data = reader.readline()
                print(data)
        except IOError:
            print(f'Unable to read from file: ', {file})

    def readFileLineByLine(self, file):
        """ Prints out contents of the file line by line """
        with open(file, 'r') as reader:
            line = reader.readline()
            while line:  # loop as long as line is defined (stops after last line is read and returns null
                print(line)
                line = reader.readline()  # update line with next line data

    def getFileAllLines(self, file):
        """ Returns a list of file contents, 1 line per entry """
        data = list()

        with open(file, 'r') as reader:
            line = reader.readline()
            while line:  # loop as long as line is defined (stops after last line is read and returns null)
                data.append(line)  # add line to data
                line = reader.readline()  # update line with next line data

        return data     # return list containing all data after file reading complete

    def getAllDataFromFile(self, file):
        """ Returns a String containing all data from a file """
        try:
            with open(file, 'r') as reader:
                data = reader.read()
                return data
        except IOError:
            print('Unable to read from file: ', file)

    # Allows us to clean up a list of data to remove '\n' (newline) content from it
    def removeNewlinesFromData(self, data):
        """ Returns a file with all \n (newline) content removed """
        for i in range(len(data)):  # through all data
            data[i] = data[i].replace("\n", "")   # remove all references to new lines in data
            if len(data[i]) == 0:  # if there are now empty entries in the data, remove them!
                data.remove(data[i])
                i -= 1  # after removing an entry, we need to move back a step (the list is now 1 shorter)
        return data


"""
     My Utility Methods
     
"""


def get_total_number_of_lines(self, file):
    """ Returns the total number of lines of data in a file. """
    with open(file, 'r') as file:
        return sum(1 for line in file)
    pass


def get_total_characters(self):
    """ Returns the total number of characters in a file. """
    pass


def is_keyword_present(self, word):
    """ Returns whether a file contains a given word or phrase. """
    pass


def get_words_of_certain_length(self, length):
    """ Returns a list that only includes words of a certain length. """
    pass
