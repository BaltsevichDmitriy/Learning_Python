def digital_root(n):
    if n < 10:
        print(n)
        return n
    temp = str(n)
    temp = list(temp)
    res = []
    for i in temp:
        res.append(int(i))
    n = sum(res)

    digital_root(n)


# digital_root(32253465746)


def alphabet_position(text):
    """
    This function in a string, replace every letter with its position in the alphabet.
    "The narwhal bacons at midnight.", 20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20
    :param text:
    :return:
    """
    dirty_alphabet = "A b c d e f g h i j k l m n o p q r s t u v w x y z"

    def sort(t):
        f = filter(str.isalpha, t.lower())
        alphabet = "".join(f)
        return list(alphabet)

    # make a dictionary with position letters
    array_alphabet = {}
    array_num = []
    position_let = 0
    for i in sort(dirty_alphabet):
        position_let += 1
        array_alphabet[i] = position_let
    # make array_num
    for n in sort(text):
        array_num.append(str(array_alphabet[n]))
    str_num = " ".join(array_num)
    return str_num


print(alphabet_position("The sunset sets at twelve o' clock."))
example = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


def duplicate_encode(word):
    pass