digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chosen = []

def is_valid(square):
    for row in square:
        if sum(row) != 15:
            return False
    for i in range(len(square)):
        if sum(map(lambda row: row[i], square)) != 15:
            return False
    if sum(square[i][i] for i in range(len(square))) != 15:
        return False
    if sum(square[i][2 - i] for i in range(len(square))) != 15:
        return False
    return True

def is_hopeless(square):
    for row in square:
        if is_sequence_hopeless(row):
            return True
    for i in range(len(square)):
        col = list(map(lambda row: row[i], square))
        if is_sequence_hopeless(col):
            return True
    diag1 = list(square[i][i] for i in range(len(square)))
    if is_sequence_hopeless(diag1):
        return True
    diag2 = list(square[i][2 - i] for i in range(len(square)))
    if is_sequence_hopeless(diag2):
        return True
    
    return False

def is_sequence_hopeless(seq):
    seqSum = sum(seq)
    if seqSum > 15:
        return True
    if seqSum == 15 and 0 in seq:
        return True
    if seqSum < 15 and 0 not in seq:
        return True
    #there are more cases that would prune hopeless paths
    #can implement this by checking for remaining sum needed in the set of remaining available digits with help of a Set
    #but this is fine for now
    #if (seqSum == 14 and 1 in chosen):
        #return True
    return False

for num1 in digits:
    chosen.append(num1)
    square = [[num1, 0, 0],[0, 0, 0],[0, 0, 0]]
    if is_hopeless(square):
        chosen.pop()
        continue
    for num2 in digits:
        if num2 not in chosen:
            chosen.append(num2)
            square = [[num1, num2, 0],[0, 0, 0],[0, 0, 0]]
            if is_hopeless(square):
                chosen.pop()
                continue
            for num3 in digits:
                if num3 not in chosen:
                    chosen.append(num3)
                    square = [[num1, num2, num3],[0, 0, 0],[0, 0, 0]]
                    if is_hopeless(square):
                        chosen.pop()
                        continue
                    for num4 in digits:
                        if num4 not in chosen:
                            chosen.append(num4)
                            square = [[num1, num2, num3],[num4, 0, 0],[0, 0, 0]]
                            if is_hopeless(square):
                                chosen.pop()
                                continue
                            for num5 in digits:
                                if num5 not in chosen:
                                    chosen.append(num5)
                                    square = [[num1, num2, num3],[num4, num5, 0],[0, 0, 0]]
                                    if is_hopeless(square):
                                        chosen.pop()
                                        continue
                                    for num6 in digits:
                                        if num6 not in chosen:
                                            chosen.append(num6)
                                            square = [[num1, num2, num3],[num4, num5, num6],[0, 0, 0]]
                                            if is_hopeless(square):
                                                chosen.pop()
                                                continue
                                            for num7 in digits:
                                                if num7 not in chosen:
                                                    chosen.append(num7)
                                                    square = [[num1, num2, num3],[num4, num5, num6],[num7, 0, 0]]
                                                    if is_hopeless(square):
                                                        chosen.pop()
                                                        continue
                                                    for num8 in digits:
                                                        if num8 not in chosen:
                                                            chosen.append(num8)
                                                            square = [[num1, num2, num3],[num4, num5, num6],[num7, num8, 0]]
                                                            if is_hopeless(square):
                                                                chosen.pop()
                                                                continue
                                                            for num9 in digits:
                                                                if num9 not in chosen:
                                                                    chosen.append(num9)
                                                                    square = [[num1, num2, num3],[num4, num5, num6],[num7, num8, num9]]
                                                                    if is_valid(square):
                                                                        print(square)
                                                                    chosen.pop()
                                                            chosen.pop()
                                                    chosen.pop()
                                            chosen.pop()
                                    chosen.pop()
                            chosen.pop()
                    chosen.pop()
            chosen.pop()
    chosen.pop()
