from curses.ascii import isdigit


def main(data: str):
    a = []
    for i in data:
        if i.isdigit():
            a.append(i)
    return a
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """


# Read data from file
f = open('./txt_file/data03.txt')
x = f.read()
f.close()
main(x)
