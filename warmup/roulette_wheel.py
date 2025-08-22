import random

def random_draw(distribution): #distribution is a PDF f(x) where x is the index in the array
    cdf = []
    for p in distribution:
        if len(cdf) == 0:
            cdf.append(p)
        else:
            cdf.append(cdf[-1] + p)

    r = random.random()
    index = None
    for i in range (len(cdf)):
        if (cdf[i] >= r):
            index = i
            break

    return index

pdf = [0.1, 0.1, 0.5, 0.1, 0.1, 0.1]
draws = [0] * len(pdf)
proportions = [0] * len(pdf)

total_draws = 1000

for i in range(total_draws):
    draw_index = random_draw(pdf)
    draws[draw_index] += 1

for i in range(len(pdf)):
    proportions[i] = draws[i] / total_draws

print(proportions)