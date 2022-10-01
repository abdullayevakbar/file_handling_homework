def main(data: str):
    a = 0
    for i in data:
        if (i.isdigit()):
            a += int(i)
    return a
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """


# Read data from file
f = open('./txt_file/data07.txt')
data = f.read()
f.close()
print(main(data))
