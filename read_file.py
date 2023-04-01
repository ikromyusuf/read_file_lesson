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
    f = open(filename).read()
    l = 0
    print(f.split(","))
    for i in f.split(","):
        l+=int(i)
    # Read the file
    return l
print(read_file("data.txt"))