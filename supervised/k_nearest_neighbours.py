import math
import matplotlib.pyplot as pyplot
import numpy as np

#would need to be adjusted to work for higher-d space

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def assign_distances(point, data):
    data_w_dist = list(map(lambda p: (*p, round(distance(point, p), 3)), data))
    data_w_dist.sort(key=lambda x: x[-1])
    return data_w_dist

def k_n_neighbors(k, point, data):
    data_w_dist = assign_distances(point, data)
    k_distance = data_w_dist[:k][-1][-1]
    knn = list(filter(lambda x: x[-1] <= k_distance, data_w_dist))
    counts = {}
    majority_cat = None
    max_count = 0
    for neighbor in knn:
        category = neighbor[2]
        count = counts.get(category)
        if count == None:
            count = 1
            counts[category] = 1
        else:
            counts[category] += 1
        if counts[category] > max_count:
            majority_cat = category
            max_count = counts[category]
    
    highest_counts = list(filter(lambda item: item[1] == max_count, counts.items()))
    highest_count_cats = [x[0] for x in highest_counts]
    if len(highest_counts) == 1:
        return majority_cat
    
    min_total_dist = None
    result = None
    for category in highest_count_cats:
        points = filter(lambda x: x[-2] == category and x[-1] <= k_distance, data_w_dist)
        total_dist = sum(map(lambda x: x[-1], points))
        if min_total_dist == None or total_dist < min_total_dist:
            result = category
            min_total_dist = total_dist

    return result


def cross_validate(data, k):
    success = 0
    total_points =  len(data)
    for i in range(len(data)):
        left_one_out_data = data.copy()
        left_out_point = left_one_out_data.pop(i)
        prediction = k_n_neighbors(k, left_out_point, left_one_out_data)
        if prediction == left_out_point[2]:
            success += 1
    return success/total_points

def cross_validation_curve(data):
    x = []
    y = []
    for k in range(1, len(data)):
        x.append(k)
        accuracy = cross_validate(data, k)
        y.append(accuracy)

    ax = pyplot.subplot()
    ax.plot(x, y)
    pyplot.show()

if __name__ == "__main__":

    data = [(0.15, 0.2, 'Sh'),
        (0.15, 0.3, 'Sh'),
        (0.2, 0.25, 'Sh'),
        (0.25, 0.4, 'Sh'),
        (0.3, 0.35, 'Sh'),
        (0.05, 0.25, 'Su'),
        (0.05, 0.35, 'Su'),
        (0.1, 0.3, 'Su'),
        (0.15, 0.4, 'Su'),
        (0.25, 0.35, 'Su')
    ]

    unknown = (0.25, 0.3)
    for k in range(1, len(data) + 1):
        category = k_n_neighbors(k, unknown, data)
        print(f"For k = {k}, {unknown} categorized as {category}")

    cross_validation_curve(data)

    data = [
        (0.6, 200, 'Sh'),
        (0.6, 300, 'Sh'),
        (0.8, 250, 'Sh'),
        (1.0, 400, 'Sh'),
        (1.2, 350, 'Sh'),
        (0.2, 250, 'Su'),
        (0.2, 350, 'Su'),
        (0.4, 300, 'Su'),
        (0.6, 400, 'Su'),
        (1.0, 350, 'Su')
    ]

    # bad accuracy due to difference in scaling of variables
    cross_validation_curve(data)

    #min-max normalization of above data
    x = np.array([x[0] for x in data])
    y = np.array([x[1] for x in data])

    norm_x = (x - np.min(x)) / np.max((x - np.min(x)))
    norm_y = (y - np.min(y)) / np.max((y - np.min(y)))
    for i in range(len(data)):
        data[i] = (norm_x[i], norm_y[i], data[i][2])
        
    cross_validation_curve(data)