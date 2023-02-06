# write() - writes the listed string to the file

# Read more here! https://realpython.com/read-write-files-python/

class FileWrite:

    def __init__(self):
        print('File writer created!')

    def writeStringOverFile(self, fileName, stringData):
        """ Write String data to file, overwriting previous file contents """
        try:
            with open(fileName, 'w') as writer:
                writer.write(stringData)
        except IOError:
            print('Error writing to file: ', fileName)

    def writeStringToFile(self, fileName, stringData):
        """ Write String data to file, appending onto exiting file contents """
        try:
            with open(fileName, 'a') as writer:
                writer.write(stringData)
        except IOError:
            print('Error writing to file: ', fileName)

    def writeDataOverFile(self, fileName, data):
        """ Write list data to file, overwriting previous file contents """
        try:
            with open(fileName, 'w') as writer:
                for entry in data:
                    writer.write(entry + '\n')  # add each data entry on its own line
        except IOError:
            print('Error writing to file: ', fileName)

    def writeDataToFile(self, fileName, data):
        """ Write list data to file, appending onto existing file contents """
        try:
            with open(fileName, 'a') as writer:
                for entry in data:
                    writer.write(entry + '\n')  # add each data entry on its own line
        except IOError:
            print('Error writing to file: ', fileName)

    def writeDataOverFileCustom(self, fileName, data, delimiter):
        """ Write list data to file, overwriting previous file contents, using custom delimiter """
        try:
            with open(fileName, 'w') as writer:
                for entry in data:
                    writer.write(entry + delimiter)  # add each data entry separated by custom delimiter
        except IOError:
            print('Error writing to file: ', fileName)

    def writeDataToFileCustom(self, fileName, data, delimiter):
        """ Write list data to file, appending onto existing file contents, using custom delimiter """
        try:
            with open(fileName, 'a') as writer:
                for entry in data:
                    writer.write(entry + delimiter)  # add each data entry separated by custom delimiter
        except IOError:
            print('Error writing to file: ', fileName)

    def writeNumbersTo100ToFile(self, fileName, append):
        """ Write the numbers 1 to 100 to given file, appending or overwriting based in boolean input """

        # Begin by generating a string with the numbers 1 to 100 organized into 10 rows
        num = 1  # variable holding first number to be printed
        stringToWrite = ''  # variable to hold the String being built
        for a in range(10):  # loop for rows
            for b in range(10):  # loop for numbers in each row
                nextEntry = '\t' + str(num)
                stringToWrite += nextEntry  # add the next number to the master string
                num += 1  # increase number by 1
            stringToWrite += '\n'  # add a new line to string to create new row

        # Finally, write this string to a file in manner determined (write or append)
        if append:
            self.writeStringToFile(fileName, stringToWrite)
        else:
            self.writeStringOverFile(fileName, stringToWrite)

    def writeNumbersToFileAdvanced(self, fileName, append, maxNum, numsPerRow):
        """ Write a custom number of numbers using custom organization to file, appending or overwriting based on boolean input """
        numRows = int(
            maxNum / numsPerRow)  # determine number of rows that will fit custom organization with no remainder
        extraNums = maxNum % numsPerRow  # determine the number of overflow values (the final row) that need to be added
        num = 1  # value to start counting from
        customAligner = '            '  # Whitespace used to organize output alignment; make bigger if numbers expect to get large
        stringToWrite = ''  # variable to hold the String being built

        print(numRows)
        print(extraNums)

        # write all full rows to master String
        for row in range(numRows):
            for val in range(numsPerRow):
                stringLength = len(str(num))  # calculate the length of the number, for content organization
                nextEntry = str(num) + customAligner[
                                       stringLength:]  # Concatenate the number to the customAligner, adjusting aligner spaces in relation to number length
                stringToWrite += nextEntry  # add the next number to the master string
                num += 1
            stringToWrite += '\n'  # add a new line to string to create new row

        # writer overflow row to master String - if there is one!
        for val in range(extraNums):
            stringLength = len(str(num))  # calculate the length of the number, for content organization
            nextEntry = str(num) + customAligner[
                                   stringLength:]  # Concatenate the number to the customAligner, adjusting aligner spaces in relation to number length
            stringToWrite += nextEntry
            num += 1

        # Finally, write this string to a file in manner determined (write or append)
        if append:
            self.writeStringToFile(fileName, stringToWrite)
        else:
            self.writeStringOverFile(fileName, stringToWrite)

    """
        My Methods
    """

    # TODO

    # Create a method that can join 3 different files together into a single file

    def merge_files(self, files):
        """ Merges 3 different files together into a single file."""
        pass

    def create_copy_of_file_based_on_alphabetic_order(self, originalFile):
        """ Creates a copy of a given file that arranges the contents in alphabetical order."""
        pass

    def create_copy_of_file_based_on_word_length(self, originalFile):
        "Create a method that creates a new file with the contents of the ‘AllWords.txt’ file sorted by word length rather than alphabetically"
        pass


    def write_data_to_file(self, data, file):
        "Create a method that writes all sent data (either a String or a List) to a file with a common format decided by you"
        pass
