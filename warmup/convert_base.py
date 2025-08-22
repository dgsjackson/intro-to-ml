def binary_to_decimal(string):
    result = 0
    for i in range(0, len(string)):
        pow = i
        index = (i + 1) * -1
        digit_char = string[index]
        digit = int(digit_char)
        value = digit * (2 ** pow)
        result += value
    
    return str(result)

def hexadecimal_to_decimal(string):
    result = 0
    for i in range(0, len(string)):
        pow = i
        index = (i + 1) * - 1
        digit_char = string[index]
        digit = None
        if str.isdigit(digit_char):
            digit = int(digit_char)
        else:
            digit = ord(digit_char) - 55
            
        value = digit * (16 ** pow)
        result += value
    
    return str(result)

def decimal_to_binary(string):
    if string == "0":
        return "0"

    result = ""
    dict = {}
    total_val = int(string)

    while total_val > 0:
        deduct = 1
        pow = 0
        multiple = 1

        while deduct * 2 <= total_val:
            deduct *= 2
            pow += 1

        pow_result = deduct

        while deduct + pow_result <= total_val:
            deduct += pow_result
            multiple += 1

        total_val -= deduct
        dict[pow] = multiple

    index = 0
    while len(dict) > 0:
        if dict.get(index) == None:
            result += '0'
        else:
            result += str(dict[index])
            dict.pop(index)
        index += 1

    return result[::-1]
        


def decimal_to_hexadecimal(string):
    if string == "0":
        return "0"

    result = ""
    dict = {}
    total_val = int(string)

    while total_val > 0:
        deduct = 1
        pow = 0
        multiple = 1

        while deduct * 16 <= total_val:
            deduct *= 16
            pow += 1

        pow_result = deduct

        while deduct + pow_result <= total_val:
            deduct += pow_result
            multiple += 1

        total_val -= deduct
        dict[pow] = multiple

    index = 0
    while len(dict) > 0:
        if dict.get(index) == None:
            result += '0'
        else:
            val = dict[index]
            if val < 10:
                result += str(val)
            else:
                result += chr(val + 55)
            dict.pop(index)

        index += 1

    return result[::-1]

def binary_to_hexadecimal(str):
    return decimal_to_hexadecimal(binary_to_decimal(str))

def hexadecimal_to_binary(str):
    return decimal_to_binary(hexadecimal_to_decimal(str))