def main(data: str):
    a = 1000000
    for i in data:
        if (i.isdigit() == True):
            if (a > int(i)):
                a = int(i)
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
