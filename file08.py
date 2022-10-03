def main(data: str):
    a = 0
    for i in data:
        if (i.isdigit() == True):
            if (a < int(i)):
                a = int(i)
    return a
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """


# Read data from file
f = open('./txt_file/data08.txt')
data = f.read()
f.close()
print(main(data))
