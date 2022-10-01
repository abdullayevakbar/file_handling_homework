def main(data: str):
    return len(data)
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """


# Read data from file
f = open('./txt_file/data02.txt')
x = f.read()
f.close()
main(x)
