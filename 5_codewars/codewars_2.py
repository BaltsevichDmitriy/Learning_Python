def find_nb(m):
    """
    # Your task is to construct a building which will be a pile of n cubes.
    # The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3
    # and so on until the top which will have a volume of 1^3.
    """
    n = 0
    result = 0
    while m > result:
        n += 1
        result += n ** 3
    if result == m:
        return n
    else:
        return -1


# alternative
def find_nb(m):
    a = int((2 * m ** 0.5) ** 0.5)
    if (a * (a + 1) / 2) ** 2 == m:
        return a
    return -1


# print(find_nb(1071225))№№№№№№№№№№№№№::::::::::::::::::::::::::::::::::???????????????


def longest_consec(strarr, k):
    """
    You are given an array(list) strarr of strings and an integer k.
    Your task is to return the first longest string consisting of k consecutive strings taken in the array.
    """
    if k < 1:
        k = 1
    else:
        k = k
    max_len_word = 0
    for i in range(len(strarr)):
        for ii in range(k):
            return ii


# longest_consec()


def wave(people):
    result = []
    for i in range(len(people)):
        w = list(people.lower())
        if w[i].isalpha():
            w[i] = w[i].upper()
            ww = "".join(w)
            result.append(ww)
    return result


# print(wave('hellod#@$ , g'))


def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if s.lower().count(i) == 0:
            return False
    return True


# print(is_pangram("The quick brown fox jumps over the lzy dog"))


def is_valid_walk(walk):
    n, s, e, w = 0, 0, 0, 0
    for i in walk:
        if i == 'n':
            n += 1
        elif i == 's':
            s += 1
        elif i == 'e':
            e += 1
        elif i == 'w':
            w += 1
    if (n + s + e + w) == 10 and (n - s) == 0 and (w - e) == 0:
        return True
    else:
        return False


# print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))


def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(0)
    return array


# print(move_zeros([1, 0, 1, 2, 0, 1, 3]))


def likes(names):
    if len(names) > 3:
        return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " " + "and" + " " + names[2] + " like this"
    elif len(names) == 2:
        return names[0] + " " + "and" + " " + names[1] + " like this"
    elif len(names) == 1:
        return names[0] + " likes this"
    else:
        return "no one likes this"


# альтернативный подход
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n - 2)


# print(likes(["Alex", "Jacob", "Mark", "Jacob", "Mark", "Mark", "Jacob", "Mark"]))

def find_missing_letter(chars):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    counter = 0
    flag = False
    for i in alphabet:
        if i == chars[0].lower():
            flag = True
        if flag:
            if i != chars[counter].lower():
                if chars[counter].isupper():
                    return i.upper()
                else:
                    return i
            counter += 1


# print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))


def anagrams(word, words):
    result = []
    for ii in words:
        if len(ii) == len(word):
            for i in word:
                if word.count(i) != ii.count(i):
                    break
            else:
                result.append(ii)
    return result


# alternative variant
def anagrams(word, words): return [item for item in words if sorted(item) == sorted(word)]

# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
