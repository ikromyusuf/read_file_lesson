#Rread file and convert to list
def read_file(filename: str) -> list:
    """
    Reads a file and returns a list of lines.
    
    Args:
        filename (str): The name of the file to read.
    
    Returns:
        data (list): A list of lines from the file.
    """
    # Open the file
    f = open("data.txt").read()
    f = f.split(",")
    list_of_digits = []
    for i in f:
        list_of_digits.append(int(i))

    # Read the file
    return list_of_digits

#Print list from file
print(read_file("data.txt"))