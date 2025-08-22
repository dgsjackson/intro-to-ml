def calc_cartesian_product(ranges): #ranges is an array of arrays
    points = [[]]
    for coord_range in ranges:
        next_points = []
        for val in coord_range:
            for point in points:
                new_point = point.copy()
                new_point.append(val)
                next_points.append(new_point)
        points = next_points
    
    return points

print(calc_cartesian_product([['a', 'b', 'c'], [1, 2]]))