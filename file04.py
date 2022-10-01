def main(data: str):
    a = []
    for i in data:
        if i.isdigit() == False:
            a.append(i)
    return a
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """


# Read data from file
f = open('./txt_file/data04.txt')
x = f.read()
f.close()
print(main(x))
