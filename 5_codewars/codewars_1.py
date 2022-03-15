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

###################################################
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


###################################################
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

##################________________#################################
# Мой вариант, математика без рекурсии######
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


# альтернотивное решение
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c


################################################################################
def create_phone_number(n):
    counter = 0
    result = "("
    for i in n:
        result += str(i)
        if counter == 2:
            result += ")"
            result += " "
        if counter == 5:
            result += "-"
        counter += 1
    return result


# альтернотивный способ
def create_phone_number(n):
    n = list(map(str, n))
    return "({}) {}-{}".format("".join(n[:3]), "".join(n[3:6]), "".join(n[6:10]))


# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

##################________________#################################

# Write a function that takes an integer as input, and returns the number
# of bits that are equal to one in the binary representation of that number.
# You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
def countBits(n):
    bin_nom = bin(n)
    result = 0
    for i in bin_nom[2:]:
        result += int(i)
    return result


# print(countBits(1234))
#################################################################

def rot13(message):
    """
    nROT13 is a simple letter substitution cipher that replaces a letter with
    the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
    """
    dirty_alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    f = filter(str.isalpha, dirty_alphabet)
    alphabet = "".join(f)
    result = ""
    for w in message:
        counter = 0
        for i in alphabet:

            if i == w.lower() and counter <= 13:
                if w.isupper():
                    result += alphabet[counter + 13].upper()
                    break
                else:
                    result += alphabet[counter + 13]
                    break
            elif i == w.lower() and counter > 13:
                if w.isupper():
                    result += alphabet[counter - 13].upper()
                    break
                else:
                    result += alphabet[counter - 13]
                    break
            elif counter == len(alphabet) - 1:
                result += w
            counter += 1
    return result


# print(rot13('Test'))###############################################


def count_smileys(arr):
    result = 0
    for i in arr:
        if len(i) == 2:
            if (i[0] == ':' or i[0] == ";") and (i[1] == ')' or i[1] == "D"):
                result += 1
        if len(i) == 3:
            if (i[0] == ':' or i[0] == ";") and (i[1] == '-' or i[1] == "~") and (i[2] == ')' or i[2] == "D"):
                result += 1
    return result


# print(count_smileys([':D', ':~)', ';~D', ':)']))


def find_uniq(arr):
    temp = sorted(arr)
    if temp[len(temp) - 1] == temp[len(temp) - 2]:
        return temp[0]
    else:
        return temp[len(temp) - 1]


# print(find_uniq([1, 1, 1, 0.5, 1, 1]))

def generate_primes(n):
    yield (2)
    primes = [(2, 4)]
    for m in range(3, n, 2):
        for prime, square in primes:
            if square > m:
                yield (m)
                primes.append((m, m * m))
                break
            if m % prime == 0:
                break


def prime_factors(n):
    string = ""
    i = 2
    for i in generate_primes(int(n ** 0.5) + 1):
        c = 0
        while True:
            product, remainder = divmod(n, i)
            if remainder != 0:
                break
            n = product
            c += 1
        if c == 1:
            string += f"({i})"
        elif c > 1:
            string += f"({i}**{c})"
    if n > 1:
        string += f"({n})"

    return string


# print(primeFactors(86240))


def productFib(prod):
    n = 1
    n_previous = 0
    if prod == 0:
        return [0, 1, True]
    while n * n_previous < prod:
        n += n_previous
        n_previous = n - n_previous
        print(n)
        if n * n_previous == prod:
            return[n_previous, n, True]
        elif n * n_previous >= prod:
            return[n_previous, n, False]



print(productFib(0))
