def main(data: str):
    a = 0
    for i in data:
        if (i.islower()):
            a += 1
    return a
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """


# Read data from file
f = open('./txt_file/data09.txt')
data = f.read()
f.close()
print(main(data))
