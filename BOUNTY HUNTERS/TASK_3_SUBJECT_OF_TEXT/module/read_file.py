#!/usr/bin/env python


        
def read_text_file(file_path: str, start_line: int = None, number_line: int = None) -> str:
    """
        This function gets a string file and return the string
        representation of the text file.

        Text file that can be read: .txt

        Arguments
        ========
        file_path: the path to read the file
    """

    # the file text to return
    file_text = ''

    with open(file_path, 'r') as file:
        if start_line:
            buffer = file.readline()
            counter = 2 # because we already escaped one line and we want to start with the line asked by the user
            while counter < start_line and buffer:
                buffer = file.readline()
                counter += 1
        if number_line:
            counter = 1 # becuase we already escaped one line
            file_text = file.readline()
            while file_text and counter < number_line:
                file_text += file.readline()
                counter += 1
        else:
            file_text = file.read() 
 
    return file_text
