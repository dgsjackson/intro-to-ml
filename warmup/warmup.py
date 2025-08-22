def check_if_symmetric(string):
    if string == None:
        return True
    if len(string) == 0 or len(string) == 1:
        return True
    start = 0
    end = len(string) - 1
    while start < end:
        if (string[start] != string[end]):
            return False
        start += 1
        end -= 1
    return True

def convert_to_numbers(string):
    numbers = []
    for char in string:
        if char == ' ':
            numbers.append(0)
        else:
            numbers.append(ord(char) - 96)

    return numbers;            

def convert_to_letters(num_array):
    letters = ""
    for num in num_array:
        if num == 0:
            letters += ' '
        else:
            letters += chr(num + 96)

    return letters

def get_intersection(array1, array2):
    intersection = []
    for item1 in array1:
        for item2 in array2:
            if item1 == item2:
                if item1 in intersection:
                    break
                intersection.append(item1)

    return intersection

def get_union(array1, array2):
    union = []
    for item in array1:
        if item not in union:
            union.append(item)
    for item in array2:
        if item not in union:
            union.append(item)

    return union

def count_characters(string):
    dict = {}
    for char in string:
        lower = str.lower(char)
        if dict.get(lower) == None:
            dict[lower] = 1
        else:
            dict[lower] = dict[lower] + 1
    return dict

def is_prime(n):
    for i in range(2, (n // 2) + 1):
        if (n % i == 0):
            return False
        
    return True