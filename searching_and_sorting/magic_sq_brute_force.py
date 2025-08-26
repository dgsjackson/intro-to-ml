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

for num1 in digits:
    chosen.append(num1)
    for num2 in digits:
        if num2 not in chosen:
            chosen.append(num2)
            for num3 in digits:
                if num3 not in chosen:
                    chosen.append(num3)
                    for num4 in digits:
                        if num4 not in chosen:
                            chosen.append(num4)
                            for num5 in digits:
                                if num5 not in chosen:
                                    chosen.append(num5)
                                    for num6 in digits:
                                        if num6 not in chosen:
                                            chosen.append(num6)
                                            for num7 in digits:
                                                if num7 not in chosen:
                                                    chosen.append(num7)
                                                    for num8 in digits:
                                                        if num8 not in chosen:
                                                            chosen.append(num8)
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
