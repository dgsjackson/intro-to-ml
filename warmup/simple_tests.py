from warmup import simple

tests = [
    {
        'function': simple.check_if_symmetric,
        'unpack': False,
        'cases': [
            {'input': None, 'output': True},
            {'input': '', 'output': True},
            {'input': 'a', 'output': True},
            {'input': 'aba', 'output': True},
            {'input': 'abc', 'output': False},
            {'input': 'abdfsc', 'output': False},
            {'input': 'abcxcba', 'output': True}
        ]
    },
    {
        'function': simple.convert_to_numbers,
        'unpack': False,
        'cases': [
            {'input': 'abc', 'output': [1, 2, 3]},
            {'input': 'a c', 'output': [1, 0, 3]},
            {'input': '', 'output': []}
        ]
    },
    {
        'function': simple.convert_to_letters,
        'unpack': False,
        'cases': [
            {'input': [1, 2, 3], 'output': 'abc'},
            {'input': [1, 0, 3], 'output': 'a c'},
            {'input': [], 'output': ''},
            {'input': [5, 9, 22, 6, 12, 6, 9], 'output': 'eivflfi' }
        ]
    },
    {
        'function': simple.get_intersection,
        'unpack': True,
        'cases': [
            {'input': ([1, 2, 3], [2, 3, 4]), 'output': [2, 3]},
            {'input': ([1, 2], [3, 4]), 'output': []}
        ]
    },
    {
        'function': simple.get_union,
        'unpack': True,
        'cases': [
            {'input': ([1, 2, 3], [2, 3, 4]), 'output': [1, 2, 3, 4]},
            {'input': ([1, 2], [3, 4]), 'output': [1, 2, 3, 4]},
            {'input': ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 'output': [1, 2, 3, 4, 5]}
        ]
    },
    {
        'function': simple.count_characters,
        'unpack': False,
        'cases': [
            {'input': 'aabbc', 'output': {'a': 2, 'b': 2, 'c': 1}},
            {'input': 'A a', 'output': {'a': 2, ' ': 1}}
        ]
    },
    {
        'function': simple.is_prime,
        'unpack': False,
        'cases': [
            {'input': 2, 'output': True},
            {'input': 3, 'output': True},
            {'input': 4, 'output': False},
            {'input': 5, 'output': True},
            {'input': 6, 'output': False},
            {'input': 7, 'output': True},
        ]
    }
]

print("Running tests for simple.py ...\n")

for function_tests in tests:
    success = 0
    fail = 0

    failure_report = ""

    function = function_tests['function']
    for case in function_tests['cases']:
        if (function_tests['unpack'] == True):
            output = function(*case['input'])
        else:
            output = function(case['input'])
            
        if output == case['output']:
            success += 1
        else:
            fail += 1
            failure_report += f"Failed case Input: {case['input']}. Output: {output}. Expected output: {case['output']}.\n"
        
    print(f"{function.__name__}\nSUCCESS: {success}\nFAIL: {fail}\n{failure_report}")