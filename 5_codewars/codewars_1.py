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


# print(alphabet_position("The sunset sets at twelve o' clock."))
example = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


def duplicate_encode(word):
    """
    This function is to convert a string to a new string where each character in the new string
     is "(" if that character appears only once in the original string,
     or ")" if that character appears more than once in the original string.
    """
    list_word = list(word.lower())
    end_word = ""
    for counter in range(len(list_word)):
        count_more_one = 0
        for i in list_word:
            if i == list_word[counter]:
                count_more_one += 1
                if count_more_one > 1:
                    break
        if count_more_one > 1:
            end_word += ")"
        else:
            end_word += "("
    return end_word


# print(duplicate_encode(f"is \")\" if that"))


# Мой вариант, математика без рекурсии##########################################
def nb_year(p0, percent, aug, p):
    habits = p0
    count_year = 0
    while habits < p:
        habits = habits + habits * (percent / 100) + aug
        count_year += 1
    return count_year


# Альтернативный подход математика с рекурсией, разобраться!
def nb_year(p0, percent, aug, p):
    p0 = p0 + (p0 * (percent / 100)) + aug
    if p0 < p:
        return 1 + nb_year(p0, percent, aug, p)
    else:
        return 1


def nb_year(p0, percent, aug, p, i=0):
    return i if p0 >= p else nb_year(int(p0 + p0 * (percent / 100) + aug), percent, aug, p, i + 1)


# print(nb_year(1000, 2, 50, 12000))
##################################################################################
# суть задачи определить, что сумма двух меньших сторон треугольника больше большей стороны
def is_triangle(a, b, c):
    """
    Function that accepts 3 integer values a, b, c.
    The function should return true if a triangle can be built with the sides of given length
     and false in any other case.
    """
    list_arg = [a, b, c]
    sum_args = 0
    if min(list_arg) <= 0:
        return False
    if sum(list_arg) - max(list_arg) > max(list_arg):
        return True
    else:
        return False
