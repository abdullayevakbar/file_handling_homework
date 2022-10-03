def main(data: str):
    x = data
    a = 0
    for i in x:
        if (len(i) > a):
            a = len(i)
    return a
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """


# Read data from file
f = open('./txt_file/data10.txt')
x = f.read()
x = x.split('\n')
f.close()
print(main(x))
