def basic_array(n):
    result = [5]
    while (len(result) < n):
        next = (result[-1] * 3) - 4
        result.append(next)

    return result

def basic_recursive(n):
    if n == 1:
        return 5
    
    return (basic_recursive(n - 1) * 3) - 4

def collatz_array(n):
    result = [25]
    while len(result) < n:
        next = result[-1] / 2 if result[-1] % 2 == 0 else (result[-1] * 3) + 1
        result.append(next)

    return result

def collatz_recursive(n):
    if (n == 1):
        return 25
    
    last = collatz_recursive(n - 1)
    return last / 2 if last % 2 == 0 else (last * 3) + 1

def fibonacci_array(n):
    result = [0]
    if (n == 1): 
        return result
    result.append(1)
    if (n == 2): 
        return result
    while len(result) < n:
        result.append(result[-1] + result[-2])

    return result

def fibonacci_recursive(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)