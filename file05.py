def main(data: str):
    a = 0
    for i in data:
        if i.isdigit() == False:
            a += 1
    return [a, len(data)-a]
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """


# Read data from file
f = open('./txt_file/data05.txt')
x = f.read()
f.close()
print(main(x))
