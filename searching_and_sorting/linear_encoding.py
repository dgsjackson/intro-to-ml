from warmup import simple

def encode_string(string, a, b):
    nums = simple.convert_to_numbers(string)
    encoded_nums = list(map(lambda x: a*x + b, nums))
    return encoded_nums

def decode_numbers(numbers, a, b):
    
    decoded = list(map(lambda y: (y - b)/a, numbers))
    if all(x >= 0 and x <= 26 and (int(x) == x) for x in decoded):
        decoded_ints = []
        decoded_ints = list(map(lambda x: int(x), decoded))
        return simple.convert_to_letters(decoded_ints)
    return False

encoded_message = [377, 717, 71,
    513, 105, 921, 581, 547, 547, 105, 377, 717,
    241, 71, 105, 547, 71, 377, 547, 717, 751, 683,
    785, 513, 241, 547, 751]

messages = []
parameters = []

for a in range(1, 101):
    for b in range(0, 101):
        decode = decode_numbers(encoded_message, a, b)
        if decode != False:
            messages.append(decode)
            parameters.append((a, b))

print(messages)
print(parameters)