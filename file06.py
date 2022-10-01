def main(data: str):
    x = data.split('\n')
    a = []
    for i in x:
        a.append(len(i))
    return a
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """


# Read data from file
f = open('./txt_file/data06.txt')
data = f.read()
f.close()
print(main(data))
