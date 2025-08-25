import numpy as np

data = [
    [0.14 , 0.14 , 0.28 , 0.44] ,
    [0.22 , 0.1 , 0.45 , 0.33] ,
    [0.1 , 0.19 , 0.25 , 0.4 ] ,
    [0.02 , 0.08 , 0.43 , 0.45] ,
    [0.16 , 0.08 , 0.35 , 0.3 ],
    [0.14 , 0.17 , 0.31 , 0.38] ,
    [0.05 , 0.14 , 0.35 , 0.5 ],
    [0.1 , 0.21 , 0.28 , 0.44] ,
    [0.04 , 0.08 , 0.35 , 0.47] ,
    [0.11 , 0.13 , 0.28 , 0.45] ,
    [0.0 , 0.07 , 0.34 , 0.65] ,
    [0.2 , 0.05 , 0.4 , 0.37] ,
    [0.12 , 0.15 , 0.33 , 0.45] ,
    [0.25 , 0.1 , 0.3 , 0.35] ,
    [0.0 , 0.1 , 0.4 , 0.5 ],
    [0.15 , 0.2 , 0.3 , 0.37] ,
    [0.0 , 0.13 , 0.4 , 0.49] ,
    [0.22 , 0.07 , 0.4 , 0.38] ,
    [0.2 , 0.18 , 0.3 , 0.4 ]
]

#create new column for cluster id
for point in data:
    point.insert(0, 0)

centers = {}

def assign_initial_clusters(k):
    cluster = 1
    for point in data:
        #point.insert(0, cluster)
        point[0] = cluster
        cluster += 1
        if cluster > k:
            cluster = 1

def compute_centers():
    groups = set(map(lambda x: x[0], data))
    for i in groups:
        group = np.array(list(filter(lambda x: x[0] == i, data)))
        #mean = group.sum(axis=0)/len(group)
        mean = group.mean(axis = 0)
        centers[i] = mean

def reassign_clusters():
    reassigned = False
    for point in data:
        min = None
        current = point[0] #current cluster
        new = None #new cluster
        for k, v in centers.items():
            distance = np.linalg.vector_norm(np.array(point[1:]) - np.array(v[1:]))
            if min == None or distance < min:
                min = distance
                new = k
        if new != current:
            point[0] = new
            reassigned = True

    if (reassigned):
        compute_centers()

    return reassigned

def compute_total_distance():
    total_distance = 0.0
    for point in data:
        distance = np.linalg.vector_norm(np.array(point[1:]) - np.array(centers[point[0]][1:]))
        total_distance += distance.item()
    return total_distance

def k_means_clustering(k):
    assign_initial_clusters(k)
    compute_centers()
    recompute = True

    while (recompute):
        recompute = reassign_clusters()

    total_distance = compute_total_distance()

    return total_distance

distance_v_k = []
for k in range (1, 21):
    total_distance = k_means_clustering(k)
    distance_v_k.append([k, total_distance])

print(distance_v_k)